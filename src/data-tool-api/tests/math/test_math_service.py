import pytest
from app.math.business.math_service import MathService

@pytest.fixture
def math_service() -> MathService:
    return MathService()

def test_addition_WithValidInput_ShouldReturnSum(math_service: MathService) -> None:
    # Arrange
    a: float = 3.0
    b: float = 4.0

    # Act
    result: float = math_service.addition(a, b)

    # Assert
    assert result == 7.0

def test_addition_WithNegativeNumbers_ShouldReturnCorrectSum(math_service: MathService) -> None:
    # Arrange
    a: float = -2.0
    b: float = -5.0

    # Act
    result: float = math_service.addition(a, b)

    # Assert
    assert result == -7.0

def test_addition_WithZero_ShouldReturnOtherOperand(math_service: MathService) -> None:
    # Arrange
    a: float = 0.0
    b: float = 5.5

    # Act
    result: float = math_service.addition(a, b)

    # Assert
    assert result == 5.5
