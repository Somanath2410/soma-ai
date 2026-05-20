"""API tests."""

import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


class TestHealthEndpoints:
    """Test health check endpoints."""
    
    def test_health_check(self):
        """Test health endpoint."""
        response = client.get("/api/health/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert data["version"] == "0.1.0"
    
    def test_readiness_check(self):
        """Test readiness endpoint."""
        response = client.get("/api/health/ready")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ready"
    
    def test_liveness_check(self):
        """Test liveness endpoint."""
        response = client.get("/api/health/live")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "alive"


class TestChatEndpoints:
    """Test chat endpoints."""
    
    def test_process_prompt(self):
        """Test process endpoint."""
        response = client.post(
            "/api/chat/process",
            json={
                "prompt": "Hello, how are you?",
                "temperature": 0.7
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "response" in data
        assert "model" in data
    
    def test_process_prompt_invalid(self):
        """Test process endpoint with invalid data."""
        response = client.post(
            "/api/chat/process",
            json={
                "prompt": "",  # Empty prompt
                "temperature": 0.7
            }
        )
        assert response.status_code == 422  # Validation error
    
    def test_chat_endpoint(self):
        """Test chat endpoint."""
        response = client.post(
            "/api/chat/chat",
            json={
                "prompt": "Test message",
                "temperature": 0.5
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "response" in data
    
    def test_list_models(self):
        """Test list models endpoint."""
        response = client.get("/api/chat/models")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "models" in data
        assert len(data["models"]) > 0
        assert "current_model" in data
