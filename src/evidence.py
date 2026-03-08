def extract_spans(turns, keywords):
    evidence = []

    for t in turns:
        if any(k in t["text"].lower() for k in keywords):
            evidence.append(t)

    return evidence
