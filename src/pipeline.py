
from src.retriever import retrieve
from src.evidence import extract_spans
from src.causal import detect_factors
from src.explain import generate_explanation



def run_pipeline(query, session_id=None):

    docs = retrieve(query, top_k=5)

    if not docs:
        return "Not found in records", []

    combined_text = ""
    call_ids = []

    for d in docs:
        combined_text += d["conversation"] + "\n"
        call_ids.append(d["call_id"])

    answer = generate_explanation(query, combined_text)

    return answer, list(set(call_ids))



