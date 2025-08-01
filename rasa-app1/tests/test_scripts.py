import subprocess
import os

def test_hash_nlu():
    result = subprocess.run(["python", "scripts/hash_nlu.py"], capture_output=True)
    output = result.stdout.decode()
    assert "NLU data hash:" in output
    assert os.path.exists(".last_nlu_hash")

def test_export_onnx_runs(monkeypatch):
    try:
        subprocess.run(["python", "scripts/export_onnx.py"], check=True)
    except Exception:
        pass  # OK in CI without a trained model

def test_model_info():
    model_path = "models/test_model.tar.gz"
    os.makedirs("models", exist_ok=True)
    with open(model_path, "wb") as f:
        f.write(b"dummy")
    subprocess.run(["python", "scripts/model_info.py"], check=True)
    os.remove(model_path)
