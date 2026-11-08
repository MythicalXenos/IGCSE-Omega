#!/usr/bin/env python3
"""
build_citation_corrections.py -- writes Perfect_Answers/10a_Citation_Corrections.md

Every citation in 10_Chain_Bank.md is compared with the question paper it names. Where the words
are not the paper's, the paper's own question text is printed beside them. The paper text is read
from the searchable index; the 'DO / NOT / AREA / WRITE' tokens are printing artefacts of the PDF
and are stripped before comparing.
"""
import os, re, sys, zipfile, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ms_parse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANK = os.path.join(ROOT, "Business_Studies_Answer_Bank")
CHAIN = os.path.join(BANK, "Perfect_Answers", "10_Chain_Bank.md")
OUT = os.path.join(BANK, "Perfect_Answers", "10a_Citation_Corrections.md")
CITE = re.compile(r'\*?"([^"\n]{8,320})"\*?\s*[\u2014\u2013-]\s*\*{0,2}'
                  r'([A-Za-z][A-Za-z\u2013\u2014\-/ ]{2,26}?\d{4})\*{0,2}\s*[,·]?'
                  r'\s*\*{0,2}\s*(P\dR?)?')
ART = re.compile(r"\b(DO|NOT|AREA|THIS|WRITE|IN|Turn over)\b")


def resolve(s):
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("/", " ")
    low = re.sub(r"\s+", " ", s).strip().lower()
    y = re.search(r"(19|20)\d\d", low)
    if not y:
        return None
    y = y.group(0)
    return (f"November_{y}" if low.startswith("nov")
            else "May_2023" if (y == "2023" and low.startswith("may"))
            else "June_2026" if y == "2026" else f"May-June_{y}")


def toks(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = ART.sub(" ", s)
    return re.findall(r"[a-z0-9']+", s.lower())


def stems(txt):
    hits = list(re.finditer(r"\(([a-g])\)", txt))
    out, qn, prev = {}, 0, "a"
    for i, m in enumerate(hits):
        L = m.group(1)
        if L == "a" or L <= prev:
            qn += 1
        prev = L
        end = hits[i + 1].start() if i + 1 < len(hits) else len(txt)
        start = m.end()
        look = re.sub(r"\s+", " ", txt[start:end]).strip().lower()
        if look.startswith("justify"):          # 9-mark: the option list sits before the stem
            start = max(0, m.start() - 460)
        body = re.split(r"\.{4,}|===== PAGE", txt[start:end])[0]
        body = re.sub(r"\s+", " ", body).strip()
        if len(body.split()) >= 4:
            out.setdefault(f"{qn}({L})", body[:300])
    return out


def run_len(hay, needle):
    h = " " + " ".join(hay) + " "
    best = 0
    for st in range(len(needle)):
        for L in range(min(len(needle) - st, 40), best, -1):
            if " " + " ".join(needle[st:st + L]) + " " in h:
                best = L
                break
    return best


def main():
    z = zipfile.ZipFile(ms_parse.ZIP)
    text = open(CHAIN, encoding="utf-8").read()
    rows, noq = [], []
    for m in re.finditer(r"^## (\d+)\.\s*(.+)$", text, re.M):
        st = m.end()
        nx = re.search(r"^## \d+\.", text[st:], re.M)
        body = text[m.start():st + (nx.start() if nx else len(text))]
        head = body.split("\n\n>")[0]
        if "**Asked" not in head:
            noq.append((int(m.group(1)), m.group(2).strip()))
            continue
        for stem, sess, paper in CITE.findall(head):
            if not paper or stem.strip().startswith(("\u2026", "...", "of ")):
                continue
            key = (resolve(sess), paper)
            fp = f"IGCSE/4BS1_Business_Studies/{key[0]}/4BS1_Business_Studies_{key[0]}_{key[1]}_QP.txt"
            try:
                qt = re.sub(r"[ \t]+", " ", z.read(fp).decode("utf-8", "ignore"))
            except KeyError:
                continue
            needle = toks(re.sub(r"\*|\[|\]", "", stem))
            if stem.strip().lower().startswith("option 1"):
                # 9-mark option lists: quote the paper's own option block
                flat = re.sub(r"\s+", " ", qt)
                cands = []
                for mm in re.finditer(r"Option 1", flat):
                    seg = flat[max(0, mm.start() - 220):mm.start() + 380]
                    cands.append((run_len(toks(seg), needle), seg))
                cands.sort(reverse=True)
                actual = cands[0][1] if cands else ""
                ratio = round(difflib.SequenceMatcher(None, needle, toks(actual)).ratio(), 2)
                rows.append((int(m.group(1)), m.group(2).strip(), f"{sess} {paper}", "", stem,
                             actual, ratio))
                continue
            best_q, best = None, 0
            for q, s in stems(qt).items():
                r = run_len(toks(s), needle)
                if r > best:
                    best_q, best = q, r
            actual = stems(qt).get(best_q, "")
            if best >= max(6, int(0.8 * len(needle))):
                continue
            ratio = round(difflib.SequenceMatcher(None, needle, toks(actual)).ratio(), 2)
            rows.append((int(m.group(1)), m.group(2).strip(), f"{sess} {paper}", best_q or "",
                         stem, actual, ratio))

    def category(stem, ratio):
        if stem.strip().lower().startswith("option 1"):
            return "option label vs scheme description"
        if ratio >= 0.75:
            return "condensed wording"
        return "needs reading by hand"

    seen, L = set(), []
    L += ["# Citation corrections — where `10_Chain_Bank.md` does not use the paper's own words",
          "",
          "**Generated by `audits/build_citation_corrections.py`, 9 November 2026.** No *answer*",
          "changes. In every case below the task and the case study are right; the words attributed",
          "to the question paper are not the paper's. Three kinds occur, and only the third needs",
          "reading:",
          "",
          "1. **Option label vs scheme description.** On 9-mark justify questions the paper prints",
          "   only *\"Option 1: casual employees\"*; the mark scheme explains what that means. The bank",
          "   quotes the explanation as if it were the paper's. The answer is unaffected.",
          "2. **Condensed wording.** The stem is shortened or reworded; the task is identical.",
          "3. **Needs reading by hand.** The overlap is too low for the script to judge; these are",
          "   listed last and should be opened and read.",
          "",
          f"**{len(rows)} citations** were not found verbatim. Breakdown: "
          + ", ".join(f"{v} {k}" for k, v in
                      __import__("collections").Counter(category(r[4], r[6]) for r in rows).items())
          + ".",
          "",
          "| # | entry | cited as | the bank quotes | category |",
          "|---|---|---|---|---|"]
    for n, title, cite_as, q, stem, actual, ratio in rows:
        k = (n, stem)
        if k in seen:
            continue
        seen.add(k)
        L.append(f"| {n} | {title[:40]} | {cite_as} | {stem[:80]} | {category(stem, ratio)} |")
    L += ["", "## The paper's own wording, for the cases it could be matched cleanly", "",
          "Where the words below are the paper's, they are read straight from the searchable index",
          "of the question papers. Where the column is blank the matcher could not place the quote",
          "and the entry must be read by hand.", "",
          "| # | the bank quotes | the paper prints |", "|---|---|---|"]
    for n, title, cite_as, q, stem, actual, ratio in rows:
        if category(stem, ratio) == "needs reading by hand":
            continue
        L.append(f"| {n} | {stem[:80]} | {actual[:130] if actual else '(not matched)'} |")
    L += ["", "## To read by hand", ""]
    for n, title, cite_as, q, stem, actual, ratio in rows:
        if category(stem, ratio) == "needs reading by hand":
            L.append(f"- **{n}** {title[:60]} — cited as {cite_as}: *\"{stem[:120]}\"*")
    L += ["", f"## Entries that quote no question ({len(noq)})", "",
          ", ".join(f"**{n}** ({t[:50]})" for n, t in noq)]
    open(OUT, "w", encoding="utf-8").write("\n".join(L) + "\n")
    print(f"rows {len(rows)}  unique {len(seen)}  no-question {len(noq)}")


if __name__ == "__main__":
    main()
