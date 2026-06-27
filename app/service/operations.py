from app.repository import wallets as wallets_repository
from app.schemas import OperationRequest
from fastapi import HTTPException


def add_income(operation: OperationRequest):
    if not wallets_repository.is_wallet_exists(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet {operation.wallet_name} not found"
        )

    new_balance = wallets_repository.add_income
    return {
        "status": 200,
        "message": "Income added",
        "new_balance": new_balance,
        "description": operation.description
    }


def add_expense(operation: OperationRequest):
    if wallets_repository.is_wallet_exists(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet {operation.wallet_name} not found"
        )
    balance = wallets_repository.get_wallet_balance_by_name(
        operation.wallet_name
    )
    if balance < operation.amount:
        raise HTTPException(
            status_code=400,
            detail=f"В кошельке {balance} недостаточно средств"
        )
    new_balance = wallets_repository.add_expense(operation.wallet_name)
    return {
        "message": "Средства успешно списаны",
        "new_balnce": new_balance,
        "description": operation.description
    }
