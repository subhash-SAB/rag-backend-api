
from flask import Flask, request, jsonify
from src.pipeline import run_pipeline
import time

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query_system():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Empty request body"}), 400

    # -------------------------
    # Batch query support
    # -------------------------
    if isinstance(data, list):

        responses = []

        for item in data:

            if "query" not in item:
                responses.append({"error": "Missing query"})
                continue

            start = time.time()

            answer, call_ids = run_pipeline(item["query"])

            latency = round(time.time() - start, 3)

            responses.append({
                "query": item["query"],
                "answer": answer,
                "evidence_call_ids": call_ids,
                "latency_seconds": latency
            })

        return jsonify(responses)

    # -------------------------
    # Single query
    # -------------------------
    if "query" not in data:
        return jsonify({"error": "Missing query"}), 400

    start = time.time()

    answer, call_ids = run_pipeline(data["query"])

    latency = round(time.time() - start, 3)

    return jsonify({
        "query": data["query"],
        "answer": answer,
        "evidence_call_ids": call_ids,
        "latency_seconds": latency
    })


# -------------------------
# Health check endpoint
# -------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "running"})


if __name__ == "__main__":
    app.run(debug=True)
