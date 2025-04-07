from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Initialisation de l'application FastAPI
app = FastAPI(title="Plateforme de Synchronisation IA")


# 1. Analyse et déduplication des flux de données
class DataFlow(BaseModel):
    data: list  # liste de données reçues


@app.post("/analyze")
async def analyze_data(data_flow: DataFlow):
    """
    Analyse le flux de données et supprime les doublons.
    Pour simplifier, nous utilisons l'ensemble pour extraire les valeurs uniques.
    """
    if not data_flow.data:
        raise HTTPException(status_code=400, detail="Le flux de données est vide")

    # Déduplication simple
    unique_data = list(set(data_flow.data))

    return {
        "unique_data": unique_data,
        "original_length": len(data_flow.data),
        "unique_length": len(unique_data)
    }


# 2. Détection et résolution des conflits de synchronisation
class ConflictData(BaseModel):
    data_versions: dict  # dictionnaire des versions, ex: {"clé": [version1, version2, ...]}


@app.post("/resolve")
async def resolve_conflicts(conflict_data: ConflictData):
    """
    Résout les conflits de versions.
    Ici, pour simplifier, on choisit la version "maximale" (peut être adaptée à une logique métier plus fine).
    """
    if not conflict_data.data_versions:
        raise HTTPException(status_code=400, detail="Aucune donnée de conflit fournie")

    resolved = {}
    for key, versions in conflict_data.data_versions.items():
        # Pour l'exemple, on choisit la version avec la plus grande valeur
        resolved[key] = max(versions)

    return {"resolved_data": resolved}


# 3. Recommandation de stratégies de communication en fonction de la bande passante
class BandwidthData(BaseModel):
    usage: float  # utilisation (en MB par exemple)
    bandwidth: float  # bande passante disponible (en Mbps par exemple)


@app.post("/recommend")
async def recommend_strategy(bandwidth_data: BandwidthData):
    """
    Recommande une stratégie de synchronisation en fonction de la bande passante.
    - Faible bande passante : transfert en batch.
    - Bande passante moyenne : synchronisation incrémentale.
    - Forte bande passante : synchronisation en temps réel.
    """
    if bandwidth_data.bandwidth < 10:
        strategy = "Batch transfers"
    elif 10 <= bandwidth_data.bandwidth < 50:
        strategy = "Incremental sync"
    else:
        strategy = "Real-time sync"

    return {"recommendation": strategy}

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API de synchronisation IA !"}

# Point d'entrée de l'application
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
