import csv, requests

API = "http://127.0.0.1:5000/query"

with open("queries.csv") as f:
    rows = list(csv.reader(f))

out = [rows[0]]

for qid, q, cat, _, _ in rows[1:]:
    r = requests.post(API, json={"query": q}).json()
    out.append([
        qid,
        q,
        cat,
        f"{r['answer']} | Evidence: {','.join(r['evidence_call_ids'])}",
        ""
    ])

with open("final_queries.csv","w",newline="") as f:
    csv.writer(f).writerows(out)
