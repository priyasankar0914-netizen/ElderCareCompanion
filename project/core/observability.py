import json, time

LOG_PATH = "project/logs.jsonl"

def log(event: str, data: dict):
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps({"time": time.time(), "event": event, "data": data}) + "\n")
