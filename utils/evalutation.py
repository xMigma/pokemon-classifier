from tensorflow.keras.models import load_model

def evaluate_model(model_path, test_data):
    test_model = load_model(model_path)
    return test_model.evaluate(test_data)
    