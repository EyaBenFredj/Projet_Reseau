from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyze_endpoint():
    payload = {"data": ["a", "b", "a", "c"]}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "unique_data" in data
    assert data["original_length"] == 4
    assert data["unique_length"] <= 4

def test_resolve_endpoint():
    payload = {"data_versions": {"item1": [1, 2, 3], "item2": [10, 5]}}
    response = client.post("/resolve", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "resolved_data" in data
    # Pour item1, la version max doit être 3
    assert data["resolved_data"]["item1"] == 3

def test_recommend_endpoint():
    # Test avec bande passante faible
    payload_low = {"usage": 500, "bandwidth": 5}
    response_low = client.post("/recommend", json=payload_low)
    assert response_low.status_code == 200
    data_low = response_low.json()
    assert data_low["recommendation"] == "Batch transfers"

    # Test avec bande passante moyenne
    payload_mid = {"usage": 500, "bandwidth": 20}
    response_mid = client.post("/recommend", json=payload_mid)
    assert response_mid.status_code == 200
    data_mid = response_mid.json()
    assert data_mid["recommendation"] == "Incremental sync"

    # Test avec bande passante élevée
    payload_high = {"usage": 500, "bandwidth": 80}
    response_high = client.post("/recommend", json=payload_high)
    assert response_high.status_code == 200
    data_high = response_high.json()
    assert data_high["recommendation"] == "Real-time sync"
