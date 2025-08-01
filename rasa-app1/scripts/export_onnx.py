import os
from rasa.model import get_latest_model

def export_diet_to_onnx(model_dir, onnx_dir):
    import tensorflow as tf
    import tf2onnx

    model_path = os.path.join(model_dir, "nlu", "DIETClassifier")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"DIETClassifier not found at {model_path}")

    model = tf.keras.models.load_model(model_path)
    os.makedirs(onnx_dir, exist_ok=True)
    onnx_path = os.path.join(onnx_dir, "diet_classifier.onnx")

    spec = (tf.TensorSpec((None, 128, 768), tf.float32, name="input"),)
    model_proto, _ = tf2onnx.convert.from_keras(
        model, input_signature=spec, opset=13, output_path=onnx_path
    )
    print(f"ONNX exported: {onnx_path}")

if __name__ == "__main__":
    model_dir = get_latest_model("models")
    onnx_dir = os.path.join(model_dir, "onnx")
    export_diet_to_onnx(model_dir, onnx_dir)
