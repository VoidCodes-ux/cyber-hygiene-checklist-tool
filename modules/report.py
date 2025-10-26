import json
from datetime import datetime

def generate(results, filename):
    results["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)
