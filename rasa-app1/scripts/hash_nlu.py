import hashlib

NLU_FILES = ["data/nlu.yml", "config.yml", "domain.yml", "data/stories.yml", "data/rules.yml"]

def hash_files(files):
    m = hashlib.sha256()
    for file in sorted(files):
        with open(file, "rb") as f:
            m.update(f.read())
    return m.hexdigest()

if __name__ == "__main__":
    nlu_hash = hash_files(NLU_FILES)
    print(f"NLU data hash: {nlu_hash}")
    with open(".last_nlu_hash", "w") as f:
        f.write(nlu_hash)
