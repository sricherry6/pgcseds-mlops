from fastapi.testclient import TestClient
from main import app
import json


def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        assert response.status_code == 200
        assert response.json() == {"ping":"pong"}

def test_pred_virginica():
    payload = {
      "sepal_length": 3,
      "sepal_width": 5,
      "petal_length": 3.2,
      "petal_width": 4.4
    }
    with TestClient(app) as client:
        response = client.post('/predict_flower', json=payload)
        assert response.status_code == 200
        assert response.json() == {'flower_class': "Iris Virginica"}

# Added the 2 test cases

def test_pred_setosa():
    payload = {
      "sepal_length": 4.7,
      "sepal_width": 3.2,
      "petal_length": 1.3,
      "petal_width": 0.2
    }
    with TestClient(app) as client:
        response = client.post('/predict_flower', json=payload)
        assert response.status_code == 200
        assert response.json() == {'flower_class': "Iris Setosa"}
        

def test_pred_setosa2():
    payload = {
      "sepal_length": 5.0,
      "sepal_width": 3.2,
      "petal_length": 1.2,
      "petal_width": 0.2
    }
    with TestClient(app) as client:
        response = client.post('/predict_flower', json=payload) 
        assert response.status_code == 200
        assert response.json() == {'flower_class': "Iris Setosa"}
        