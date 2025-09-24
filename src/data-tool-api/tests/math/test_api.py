from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import pytest
from app.main import app, container
from app.math.business.math_service import MathService

@pytest.fixture
def client() -> TestClient:
    return TestClient(app)

def test_calculate_add_WithValidInput_ShouldReturnSum(client: TestClient) -> None:
    # Act
    response = client.get("/calculate/add?a=2&b=3")
    # Assert
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_calculate_add_WithNegativeNumbers_ShouldReturnCorrectSum(client: TestClient) -> None:
    # Act
    response = client.get("/calculate/add?a=-2&b=-3")
    # Assert
    assert response.status_code == 200
    assert response.json() == {"result": -5.0}

def test_calculate_add_WithZero_ShouldReturnOtherOperand(client: TestClient) -> None:
    # Act
    response = client.get("/calculate/add?a=0&b=7.5")
    # Assert
    assert response.status_code == 200
    assert response.json() == {"result": 7.5}

def test_calculate_add_WithMockedService_ShouldReturnMockedResult(client: TestClient) -> None:
    mock_service: MagicMock = MagicMock(spec=MathService)
    mock_service.addition.return_value = 42.0
    # Override the dependency in the IoC container
    with container.math_service.override(mock_service):
        response = client.get("/calculate/add?a=1&b=2")
        assert response.status_code == 200
        assert response.json() == {"result": 42.0}
