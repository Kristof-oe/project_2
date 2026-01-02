from fastapi.testclient import TestClient
from app.main import app

m = TestClient(app)

def test_health():
    response = m.get("/health")
    assert response.status_code == 200


# def test_process():
#     response = m.post("/task/")
#     assert response.status_code== 200


