from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_recommend_ia():
    # Exemple de données pour tester l'endpoint IA
    payload = {
        "bandwidth": 30,  # en Mbps
        "usage": 500,     # en Mo
        "latency": 100    # en ms
    }
    response = client.post("/recommend-ia", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "recommendation" in data
