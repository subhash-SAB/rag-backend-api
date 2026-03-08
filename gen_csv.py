import csv
import requests

API_URL = "http://127.0.0.1:5000/query"

with open("queries.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data = rows[1:]

output = [header]

for qid, query, cat, _, _ in data:
    res = requests.post(API_URL, json={"query": query}).json()

    system_output = (
        res["answer"]
        + " | Evidence: "
        + ",".join(res["evidence_call_ids"])
    )

    output.append([qid, query, cat, system_output, ""])

with open("final_queries.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(output)

print("final_queries.csv generated")
