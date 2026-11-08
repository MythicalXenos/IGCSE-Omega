#!/usr/bin/env python3
"""
qp_stems.py -- read the real question stems out of the question papers.

The By_Paper files carry a "**Question:**" line taken from the *mark scheme's* narrow
question column. That column is cut to its width, so the line frequently stops mid-sentence
("Which one of the following is a task carried out by the"), and on some items it holds the
scheme's own column header instead of a question at all ("Indicative content",
"Answer Additional guidance"). A student revising from those lines is reading half a question.

This module reads the stem from Pearson's question paper instead, where it is printed in full.

Marker forms seen in the papers:
    1    (a)    (i)    Which one of the following ...
    2    (b)    State one reason why ...
    (e)    Calculate Crumb's total revenue ...
The stem runs to the mark tariff, printed on its own line as "(2)".

Usage:
    from qp_stems import stems_for            # dict "1(a)(i)" -> full stem
    python3 audits/qp_stems.py 4BS1_June_2026_P1
"""
import os
import re
import sys

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVE = os.path.join(os.path.dirname(ROOT), "Paperlords_Archive", "IGCSE", "4BS1_Business_Studies")

WATERMARK = re.compile(r"^\s*(DO NOT WRITE IN THIS AREA|Turn over|\*?P\d{5}[A-Z]{0,3}\d*\*?|"
                       r"\d{1,2}\s*$)", re.I)
MARK = re.compile(r"^\s*\((\d{1,2})\)\s*$")
# 1   (a)   (i)   stem        |   (e)   stem        |   2 (b) stem
QSTART = re.compile(r"^\s*(?:(\d)\s*)?\(([a-g])\)\s*(?:\(([ivx]+)\))?\s*(.*)$")
# a bare "(ii)" continues part (a) of the question already open -- the papers print the
# roman numerals of a multiple-choice block without repeating "1 (a)" on every line
ROMAN = re.compile(r"^\s*\(([ivx]+)\)\s*(.*)$")
OPTION = re.compile(r"^\s*Option\s*(\d)\s*[:\-]\s*(.+)$")
DOTS = re.compile(r"^\.{10,}|^£|^\.+")


def paper_text(md_name):
    """4BS1_June_2026_P1 -> the QP pdf's text"""
    m = re.match(r"4BS1_(.+?)_(P\d\s?R?)", md_name)
    if not m:
        return None
    folder = os.path.join(ARCHIVE, m.group(1))
    pdf = os.path.join(folder, f"4BS1_Business_Studies_{m.group(1)}_{m.group(2).replace(' ', '')}_QP.pdf")
    if not os.path.exists(pdf):
        return None
    doc = pymupdf.open(pdf)
    lines = []
    for pg in doc:
        for ln in pg.get_text().split("\n"):
            if WATERMARK.match(ln) or not ln.strip():
                continue
            lines.append(ln.rstrip())
    return lines


def stems_for(md_name):
    lines = paper_text(md_name)
    if lines is None:
        return {}
    out, cur_q, cur_part, cur_roman = {}, 1, None, ""
    seen_parts = set()
    tariffs = {}
    pending_options = []
    buf = None

    def flush():
        nonlocal buf, cur_q, cur_part, cur_roman, pending_options
        if buf and cur_q and cur_part:
            txt = re.sub(r"\s+", " ", " ".join(buf)).strip()
            txt = txt.replace("\ufffc", "").strip()
            txt = re.sub(r"\s+([,.;:?])", r"\1", txt)
            key = f"{cur_q}({cur_part})" + (f"({cur_roman})" if cur_roman else "")
            out.setdefault(key, {"stem": txt, "options": list(pending_options)})
            seen_parts.add((cur_q, cur_part))
            pending_options = []
        buf = None

    for ln in lines:
        om = OPTION.match(ln)
        if om:
            pending_options.append(f"Option {om.group(1)} \u00b7 {om.group(2).strip()}")
            continue
        mk = MARK.match(ln)
        if mk:
            flush()
            if cur_q and cur_part:
                key = f"{cur_q}({cur_part})" + (f"({cur_roman})" if cur_roman else "")
                tariffs.setdefault(key, int(mk.group(1)))
            continue
        rm = ROMAN.match(ln)
        if rm and buf is None:
            flush()
            cur_roman = rm.group(1)
            buf = [rm.group(2).strip()] if rm.group(2).strip() else []
            continue
        qs = QSTART.match(ln)
        if qs and qs.group(2):
            # The papers do not always repeat the question number: P2 prints "1  IKEA is..."
            # once as a scenario heading and then only "(a) (i)", "(ii)"... So the number is
            # tracked by the part letter resetting to (a), which never happens inside a question.
            if qs.group(1):
                new_q = qs.group(1)
            elif qs.group(2) == "a" and (cur_q, "a") in seen_parts:
                new_q = str(int(cur_q) + 1)
            else:
                new_q = cur_q
            # "1 (a) (ii) ..." keeps the part letter; a bare "(e)" starts a new part
            if qs.group(1):
                part = qs.group(2)
            elif qs.group(2) == cur_part and rm is None and qs.group(3):
                part = cur_part
            else:
                part = qs.group(2)
            flush()
            cur_q, cur_part, cur_roman = new_q, part, (qs.group(3) or "")
            rest = qs.group(4).strip()
            buf = [rest] if rest else []
            continue
        if buf is not None:
            if DOTS.match(ln) or ln.strip().lower().startswith(("select one answer", "total for question")):
                flush()
                continue
            buf.append(ln.strip())
    flush()
    return {k: {"stem": v["stem"], "options": v["options"], "marks": tariffs.get(k)}
            for k, v in out.items() if v["stem"]}


if __name__ == "__main__":
    for k, v in stems_for(sys.argv[1]).items():
        print(f"{k:<10} ({v['marks']})  {v['stem']}")
