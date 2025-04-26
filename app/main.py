from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.models import model_inference
from app.models.model_inference import predict_strategy
app = FastAPI(title="Plateforme de Synchronisation IA avec modèle ML")

# Modèle de données pour l'endpoint IA
class NetworkData(BaseModel):
    bandwidth: float  # en Mbps
    usage: float      # en Mo
    latency: float    # en ms

@app.post("/recommend-ia")
async def recommend_strategy_ia(network_data: NetworkData):
    """
    Prédit la stratégie de synchronisation à partir des paramètres réseau.
    """
    try:
        recommendation = model_inference.predict_strategy(
            network_data.bandwidth,
            network_data.usage,
            network_data.latency
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"recommendation": recommendation}


@app.post("/recommend-ia")
async def recommend_strategy_ia(network_data: NetworkData):
    try:
        recommendation = predict_strategy(
            network_data.bandwidth,
            network_data.usage,
            network_data.latency
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"recommendation": recommendation}