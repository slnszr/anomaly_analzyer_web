import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import RandomOverSampler, SMOTE
from collections import Counter

# ───────────────────── Helper Function ─────────────────────
def get_model_path(filename="model.pkl"):
    """Generates the absolute path to the model file."""
    return os.path.join(os.path.dirname(__file__), filename)

# ──────────────────────── Load Data ────────────────────────
def load_data(csv_file):
    df = pd.read_csv(csv_file)
    df = df[["Packet Size", "Local Label"]]
    df["Label"] = df["Local Label"].map({"Normal": 0, "Anomalous": 1})
    X = df[["Packet Size"]]
    y = df["Label"]
    return X, y

# ─────────────────────── Train Model ───────────────────────
def train_model(csv_file, model_path=None):
    if model_path is None:
        model_path = get_model_path()

    X, y = load_data(csv_file)
    counts = Counter(y)
    minority = counts[1]  # 1 = Anomalous

    sampler = (
        RandomOverSampler(random_state=42)
        if minority < 2
        else SMOTE(random_state=42)
    )

    X_res, y_res = sampler.fit_resample(X, y)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_res, y_res)

    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"✅ Model balanced and saved to '{model_path}'.")

# ─────────────────────── Simple Prediction ───────────────────────
def predict_packet(size, model_path=None):
    if model_path is None:
        model_path = get_model_path()

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    pred = model.predict([[size]])[0]
    return "Anomalous" if pred == 1 else "Normal"

# ─────────────── Prediction with Confidence Score ───────────────
def predict_packet_with_confidence(size, model_path=None):
    """
    Returns:
        label (str): 'Normal' or 'Anomalous'
        confidence (float): probability between 0 and 1
    """
    if model_path is None:
        model_path = get_model_path()

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    proba = model.predict_proba([[size]])[0]        # [normal_prob, anomalous_prob]
    pred_index = model.predict([[size]])[0]         # 0 or 1
    label = "Anomalous" if pred_index == 1 else "Normal"
    confidence = proba[pred_index]                  # confidence score for predicted label

    return label, confidence
