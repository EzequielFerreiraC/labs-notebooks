"""Helpers for sales analysis."""
import pandas as pd


def total_revenue(df: pd.DataFrame, price_col: str = "price", qty_col: str = "qty") -> float:
    return float((df[price_col] * df[qty_col]).sum())
