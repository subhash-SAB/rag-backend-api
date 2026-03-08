import pandas as pd
import requests
import time

API_URL = "http://127.0.0.1:5000/query"

# load the queries
df = pd.read_csv("queries.csv")

system_outputs = []
latencies = []
remarks = []

for _, row in df.iterrows():

    query = row["Query"]

    payload = {
        "query": query
    }

    try:
        start = time.time()

        response = requests.post(API_URL, json=payload)

        latency = round(time.time() - start, 3)

        if response.status_code == 200:

            result = response.json()

            answer = result.get("answer", "")
            system_outputs.append(answer)

            latencies.append(latency)
            remarks.append("OK")

        else:

            system_outputs.append("API_ERROR")
            latencies.append(None)
            remarks.append("Bad status")

    except Exception as e:

        system_outputs.append("FAILED")
        latencies.append(None)
        remarks.append(str(e))


# store results
df["System_Output"] = system_outputs
df["Latency_seconds"] = latencies
df["Remarks"] = remarks

df.to_csv("evaluation_results.csv", index=False)

print("Evaluation complete.")
print("Results saved to evaluation_results.csv")
