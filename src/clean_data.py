import json
import re

INPUT = "data/Conversational_Transcript_Dataset.json"
OUTPUT = "data/clean_dataset.json"

with open(INPUT, "r", encoding="utf-8", errors="ignore") as f:
    raw = f.read()

# split when transcript_id appears
blocks = re.split(r"transcript_id", raw)

records = []

for block in blocks[1:]:
    text = block.strip()

    # extract call id (first number sequence)
    m = re.search(r"(\d+)", text)
    if not m:
        continue

    call_id = "CALL_" + m.group(1)

    # remove weird markers
    cleaned = re.sub(r"[^\x20-\x7E]+", " ", text)
    cleaned = cleaned.replace(",", " ")

    records.append({
        "call_id": call_id,
        "conversation": cleaned
    })

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)

print("Saved", len(records), "clean records")
