from fastapi import APIRouter
from app.service import operations
from app.schemas import OperationRequest

router = APIRouter()


@router.post("/operations/income")
def add_income(operation: OperationRequest):
    return operations.add_income(operation)


@router.post("/operations/expense")
def add_expense(operation: OperationRequest):
    return operations.add_expense(operation)
