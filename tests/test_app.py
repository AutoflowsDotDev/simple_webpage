"""
Tests for the SimpleWeb FastAPI application
"""

import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from app import app

# Create a test client
client = TestClient(app)

def test_home_page():
    """Test that the home page returns a 200 status code"""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    
    # Check for key elements in the HTML
    html_content = response.text
    assert "<title>Simple Web Page</title>" in html_content
    assert "Welcome to SimpleWeb" in html_content

def test_static_css():
    """Test that the CSS file is accessible"""
    response = client.get("/static/css/styles.css")
    assert response.status_code == 200
    assert "text/css" in response.headers["content-type"]

def test_static_js():
    """Test that the JavaScript file is accessible"""
    response = client.get("/static/js/main.js")
    assert response.status_code == 200
    assert "application/javascript" in response.headers["content-type"] or "text/javascript" in response.headers["content-type"]

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_contact_form_valid():
    """Test the contact form endpoint with valid data"""
    response = client.post(
        "/api/contact",
        json={
            "name": "Test User",
            "email": "test@example.com",
            "message": "This is a test message"
        }
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "Thank you for your message" in response.json()["message"]

def test_contact_form_invalid_email():
    """Test the contact form endpoint with invalid email"""
    response = client.post(
        "/api/contact",
        json={
            "name": "Test User",
            "email": "invalid-email",
            "message": "This is a test message"
        }
    )
    assert response.status_code == 422  # Validation error

if __name__ == "__main__":
    pytest.main(["-v", __file__])