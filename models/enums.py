from enum import Enum

class AssetType(Enum):
    STOCK = "STOCK"
    ETF = "ETF"

class TransactionType(Enum):
    BUY = "BUY"
    SELL = "SELL"