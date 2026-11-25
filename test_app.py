from app import app


def test_health_status_code():
    with app.test_client() as client:
        response = client.get("/health")
    assert response.status_code == 500


def test_health_response():
    with app.test_client() as client:
        response = client.get("/health")
    assert response.get_json() == {"status": "ok"}
