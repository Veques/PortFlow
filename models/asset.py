from dataclasses import dataclass
from .enums import AssetType

@dataclass
class Asset:
    name: str
    ticker: str
    asset_type: AssetType
    currency: str
    id: int | None = None
    
    def __post_init__(self):
        if not isinstance(self.name, str):
            raise TypeError("Name must be a text value")
        if self.name == "":
            raise ValueError("Please enter text value for name")
        
        if not isinstance(self.ticker, str):
            raise TypeError("Ticker must be a text value")
        if self.ticker == "":
            raise ValueError("Please enter text value for ticker")
        
        if not isinstance(self.currency, str):
            raise TypeError("Currency must be a text value")
        if self.currency == "":
            raise ValueError("Please enter text value for currency")


