import json, joblib

with open("data/clean_dataset.json","r",encoding="utf-8") as f:
    data = json.load(f)

docs = []

for i, item in enumerate(data):

    # If item already dict
    if isinstance(item, dict):
        call_id = item.get("call_id", f"CALL_{i}")
        text = item.get("conversation", "")
    else:
        # item is string
        call_id = f"CALL_{i}"
        text = item

    docs.append({
        "call_id": call_id,
        "conversation": text
    })

joblib.dump(docs, "models/docs.pkl")
print("Saved docs.pkl with", len(docs), "records")
