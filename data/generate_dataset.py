import pandas as pd
import numpy as np

import os

# Pour assurer la reproductibilité
np.random.seed(42)

n = 100  # Nombre d'exemples simulés
data = {
    "bandwidth": np.random.uniform(5, 100, n),   # Bande passante entre 5 et 100 Mbps
    "usage": np.random.uniform(100, 1000, n),      # Utilisation entre 100 et 1000 Mo
    "latency": np.random.uniform(20, 200, n)       # Latence entre 20 et 200 ms
}

df = pd.DataFrame(data)

def assign_strategy(row):
    if row["bandwidth"] < 20 or row["latency"] > 150:
        return "Batch transfers"
    elif row["bandwidth"] < 50 or row["latency"] > 80:
        return "Incremental sync"
    else:
        return "Real-time sync"

df["strategy"] = df.apply(assign_strategy, axis=1)

# Créer le dossier data s'il n'existe pas
os.makedirs(os.path.dirname(__file__), exist_ok=True)

# Sauvegarder le jeu de données dans un fichier CSV
csv_path = os.path.join(os.path.dirname(__file__), "dataset.csv")
df.to_csv(csv_path, index=False)

print(f"Jeu de données généré et sauvegardé dans {csv_path}")
