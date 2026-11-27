import pytest

from PortFlow.models.asset import Asset
from PortFlow.models.enums import AssetType


def test_name():
    with pytest.raises(ValueError):
        Asset("", "NVDA", AssetType.STOCK, "USD")
def test_nametype():
    with pytest.raises(TypeError):
        Asset(12, "2", AssetType.STOCK, "USD")

def test_ticker():
    with pytest.raises(ValueError):
        Asset("23", "", AssetType.STOCK, "USD")
def test_tickertype():
    with pytest.raises(TypeError):
        Asset("32", 32, AssetType.STOCK, "USD")

def test_currency():
    with pytest.raises(ValueError):
        Asset("2223", "NVDA", AssetType.STOCK, "")
def test_currencytype():
    with pytest.raises(TypeError):
        Asset("12", "NVdssdDA", AssetType.STOCK, 12)
        
