from fastapi import FastAPI, HTTPException
from app.repository import wallets as wallets_repository
from app.schemas import CreateWalletRequest

app = FastAPI()


def get_wallet(wallet_name: str | None = None):
    if wallet_name is None:
        wallets = wallets_repository.get_all_wallets()
        return {"tootal_balance": sum(wallets).values}
    if not wallets_repository.is_wallet_exists(wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet {wallet_name} not found"
        )
    balance = wallets_repository.get_wallet_balance_by_name(wallet_name)
    return {
        "wallet": wallet_name,
        "balance": balance
    }


def create_wallet(wallet: CreateWalletRequest):
    if not wallets_repository.is_wallet_exists(wallet.wallet_name):
        raise HTTPException(
            status_code=400,
            detail=f"Wallet {wallet.wallet_name} already exists"
        )
    else:
        new_balance = wallets_repository.create_wallet(
            wallet.wallet_name,
            wallet.initial_balance
        )
        return {
            "status": 200,
            "message": f"Wallet {wallet.wallet_name} created",
            "wallet": wallet.wallet_name,
            "balance": new_balance
        }
