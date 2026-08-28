# -*- coding: utf-8 -*-
import json, os, sys
OUT = os.path.dirname(os.path.abspath(__file__))
from more_data import MORE

data = json.load(open(f"{OUT}/eli5-egzamin.json", encoding="utf-8"))
terms = []
missing = []
for sec in data["sections"]:
    for it in sec["items"]:
        terms.append(it["term"])
        if it["term"] in MORE:
            it["more"] = MORE[it["term"]]
        else:
            missing.append(it["term"])

extra = [k for k in MORE if k not in terms]
json.dump(data, open(f"{OUT}/eli5-egzamin.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("terms total:", len(terms))
print("with more   :", sum(1 for s in data['sections'] for it in s['items'] if 'more' in it))
print("MISSING more:", len(missing))
for m in missing: print("   -", m)
print("EXTRA keys (no matching term):", len(extra))
for e in extra: print("   +", e)
