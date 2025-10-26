import os

def run():
    data = {"suspect_files": []}
    paths = ["C:\\Users", "/home"]
    keywords = ["password", "secret", "key"]

    for base in paths:
        if os.path.exists(base):
            for root, _, files in os.walk(base):
                for f in files:
                    if any(k in f.lower() for k in keywords):
                        data["suspect_files"].append(os.path.join(root, f))
    return data
