from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


BALANCE = {}
DATABASE_URL = "sqlite:///./finance.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def is_wallet_exists(wallet_name: str):
    return wallet_name in BALANCE


def add_income(wallet_name: str, amount: float) -> float:
    BALANCE[wallet_name] += amount
    return BALANCE[wallet_name]


def add_expense(wallet_name: str, amount: float) -> float:
    BALANCE[wallet_name] -= amount
    return BALANCE[wallet_name]


def get_wallet_balance_by_name(wallet_name: str) -> float:
    return BALANCE[wallet_name]


def get_all_wallets() -> dict:
    return BALANCE.copy()


def create_wallet(wallet_name: str, amount: float) -> float:
    BALANCE[wallet_name] = amount
    return BALANCE[wallet_name]