import json
import pytest
from src.lambda_function import lambda_handler  # Import the function

def test_lambda_handler():
    event = {}  # Empty test event
    context = {}  # Mock context
    
    response = lambda_handler(event, context)
    
    # Validate response type
    assert isinstance(response, dict), "Response should be a dictionary"
    
    # Validate status code
    assert "statusCode" in response, "Response should have a statusCode"
    assert response["statusCode"] == 200, "Status code should be 200"

    # Validate response body
    assert "body" in response, "Response should have a body"
    body = json.loads(response["body"])  # Convert JSON string back to object
    assert body == "Hello from Lambda! From Github Actions!", "Unexpected body response"
