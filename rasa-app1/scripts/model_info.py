import json
import hashlib
import os
import datetime

NLU_FILES = ["data/nlu.yml", "config.yml", "domain.yml", "data/stories.yml", "data/rules.yml"]

def hash_files(files):
    m = hashlib.sha256()
    for file in sorted(files):
        with open(file, "rb") as f:
            m.update(f.read())
    return m.hexdigest()

def get_latest_model_file():
    models = [f for f in os.listdir("models") if f.endswith(".tar.gz")]
    if not models:
        raise FileNotFoundError("No model files found in models/")
    return max(models, key=lambda x: os.path.getmtime(os.path.join("models", x)))

if __name__ == "__main__":
    model_file = get_latest_model_file()
    nlu_hash = hash_files(NLU_FILES)
    info = {
        "model": model_file,
        "nlu_hash": nlu_hash,
        "trained_at": datetime.datetime.utcnow().isoformat() + "Z",
    }
    os.makedirs("model-info", exist_ok=True)
    info_file = os.path.join("model-info", f"{model_file}.info.json")
    with open(info_file, "w") as f:
        json.dump(info, f, indent=2)
    print(f"Model info written: {info_file}")
