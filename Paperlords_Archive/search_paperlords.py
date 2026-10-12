#!/usr/bin/env python3
"""Search the extracted text for the Paperlords IGCSE paper archive."""
import argparse, csv, io, re, zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEXT_ZIP = HERE / "Paperlords_Searchable_Text_Index.zip"

def main():
    ap = argparse.ArgumentParser(description="Search question papers, mark schemes, and examiner reports.")
    ap.add_argument("terms", nargs="+", help="word or phrase to find (case-insensitive)")
    ap.add_argument("--subject", choices=["Economics", "Business", "Business Studies", "English Language B"])
    ap.add_argument("--session", help="filter to a session containing this text, e.g. 2022 or June 2026")
    ap.add_argument("--type", choices=["QP", "MS", "ER"])
    ap.add_argument("--limit", type=int, default=40, help="maximum matching snippets (default: 40)")
    args = ap.parse_args()
    subject = "Business Studies" if args.subject == "Business" else args.subject
    matches = 0
    with zipfile.ZipFile(TEXT_ZIP) as z:
        rows = csv.DictReader(io.TextIOWrapper(z.open("index.csv"), encoding="utf-8-sig"))
        for row in rows:
            if subject and row["subject"] != subject: continue
            if args.session and args.session.lower() not in row["session"].lower(): continue
            if args.type and row["type"] != args.type: continue
            text = z.read(row["text_path"]).decode("utf-8", "replace")
            for term in args.terms:
                m = re.search(re.escape(term), text, re.IGNORECASE)
                if not m: continue
                page = re.findall(r"===== PAGE (\d+) /", text[:m.start()])
                page = page[-1] if page else "?"
                start, end = max(0, m.start()-170), min(len(text), m.end()+230)
                snippet = " ".join(text[start:end].split())
                print(f"{row['subject']} | {row['session']} | {row['paper']} {row['type']} | p.{page}")
                print(f"  {snippet}\n")
                matches += 1
                break
            if matches >= args.limit: break
    if not matches: print("No text matches found; try a shorter term or inspect the PDF directly.")

if __name__ == "__main__": main()
