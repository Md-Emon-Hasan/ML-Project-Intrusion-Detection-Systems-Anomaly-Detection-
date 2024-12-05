import pytest
from app import app  # Import the Flask app for testing
import json

@pytest.fixture
def client():
    """Fixture to provide a test client for Flask application."""
    with app.test_client() as client:
        yield client

@pytest.fixture
def valid_data():
    """Fixture to provide valid form data for prediction."""
    return {
        'src_bytes': 1000,
        'dst_bytes': 2000,
        'count': 10,
        'same_srv_rate': 0.8,
        'dst_host_srv_count': 5,
        'dst_host_same_srv_rate': 0.9,
        'dst_host_same_src_port_rate': 0.7,
        'protocol_type': 'tcp',
        'service': 'http',
        'flag': 'SF'
    }

@pytest.fixture
def invalid_data():
    """Fixture to provide invalid form data for testing error handling."""
    return {
        'src_bytes': '',
        'dst_bytes': 2000,
        'count': 10,
        'same_srv_rate': 0.8,
        'dst_host_srv_count': 5,
        'dst_host_same_srv_rate': 0.9,
        'dst_host_same_src_port_rate': 0.7,
        'protocol_type': 'tcp',
        'service': 'http',
        'flag': 'SF'
    }

def test_homepage(client):
    """Test that the homepage loads correctly and contains required elements."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Anomaly Detection' in response.data
    assert b'Predict Anomaly' in response.data

def test_predict_valid(client, valid_data):
    """Test the /predict route with valid form data and check if the response contains a prediction."""
    response = client.post('/predict', data=valid_data)
    assert response.status_code == 200
    assert b'Prediction:' in response.data

def test_predict_invalid(client, invalid_data):
    """Test the /predict route with invalid form data (empty value) and verify error handling."""
    response = client.post('/predict', data=invalid_data)
    assert response.status_code == 200
    assert b'An error occurred' in response.data

def test_missing_fields(client):
    """Test the /predict route with missing form fields and verify error handling."""
    incomplete_data = {key: value for key, value in valid_data.items() if key != 'src_bytes'}
    response = client.post('/predict', data=incomplete_data)
    assert response.status_code == 200
    assert b'An error occurred' in response.data

def test_prediction_output_format(client, valid_data):
    """Test that the prediction response is formatted correctly."""
    response = client.post('/predict', data=valid_data)
    assert response.status_code == 200
    assert b'Prediction:' in response.data
    # Additional check to ensure the format of prediction is expected
    assert b'Normal' in response.data or b'Anomalous' in response.data

def test_invalid_url(client):
    """Test accessing an invalid URL."""
    response = client.get('/invalid-url')
    assert response.status_code == 404