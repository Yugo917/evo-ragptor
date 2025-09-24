from fastapi import APIRouter, Query, Depends
from dependency_injector.wiring import inject, Provide
from app.math.business.math_service import MathService
from app.math.api.request_models import AdditionResult
from app.container import Container

router = APIRouter(prefix="/math")

@router.get(
    "/add",
    response_model=AdditionResult,
    summary="Add two numbers and return the sum",
)
@inject
def calculate_add(
    a: float = Query(..., description="First operand."),
    b: float = Query(..., description="Second operand."),
    math_service: MathService = Depends(Provide[Container.math_service]),
) -> AdditionResult:
    """
    Compute the addition of two floating-point numbers.

    Args:
        a: First operand taken from the query string.
        b: Second operand taken from the query string.
        math_service: Dependency-injected domain service responsible for math operations.

    Returns:
        AdditionResult: Pydantic schema wrapping the computed sum as `result`.
    """
    result: float = math_service.addition(a, b)
    return AdditionResult(result=result)

