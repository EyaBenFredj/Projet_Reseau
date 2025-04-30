import joblib
import numpy as np
import os

# Chemins vers le modèle et le scaler (à adapter si nécessaire)
MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "model", "model.pkl")
SCALER_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "model", "scaler.pkl")

# Charg
# er le modèle et le scaler au démarrage
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
except Exception as e:
    print("Erreur lors du chargement du modèle ou du scaler:", e)
    model = None
    scaler = None


def predict_strategy(bandwidth: float, usage: float, latency: float) -> str:
    """
    Prédit la stratégie de synchronisation.
    """
    if model is None or scaler is None:
        raise Exception("Modèle ou scaler non disponible")

    # Préparer les données pour la prédiction
    input_features = np.array([[bandwidth, usage, latency]])
    input_scaled = scaler.transform(input_features)
    prediction = model.predict(input_scaled)
    return prediction[0]
