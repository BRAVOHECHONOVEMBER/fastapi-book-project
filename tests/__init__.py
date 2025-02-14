from fastapi.testclient import TestClient
from main import app

# Initialize TestClient without base_url
client = TestClient(app)
