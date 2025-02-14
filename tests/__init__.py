from fastapi.testclient import TestClient
from main import app

# Removed base_url to use relative paths consistently
client = TestClient(app)
