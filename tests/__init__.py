from fastapi.testclient import TestClient
from main import app

# Use base_url without the API_PREFIX
client = TestClient(app, base_url="http://test")
