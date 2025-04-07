import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Charger le jeu de données
data_path = os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
df = pd.read_csv(data_path)

# Séparation des features et de la cible
X = df[["bandwidth", "usage", "latency"]]
y = df["strategy"]

# Division en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Normalisation des données
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entraînement du modèle
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Évaluation du modèle
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy du modèle: {accuracy:.2f}")

# Créer le dossier model s'il n'existe pas déjà
output_dir = os.path.join(os.path.dirname(__file__))
os.makedirs(output_dir, exist_ok=True)

# Sauvegarder le modèle et le scaler
joblib.dump(model, os.path.join(output_dir, "model.pkl"))
joblib.dump(scaler, os.path.join(output_dir, "scaler.pkl"))

print("Modèle et scaler sauvegardés dans le dossier 'model'")
