import os
from datetime import datetime

import numpy as np
import pandas as pd

from utils import STOCKS_PATH, RESULT_PATH, TICKER_PATH

"""
Load CSV files into a DataFrame and transform it into a common structure
"""

STOCK_PATHS = [file for file in os.listdir(STOCKS_PATH) if file.endswith('.csv')]
STOCK_FILES = [os.path.join(STOCKS_PATH, file) for file in STOCK_PATHS]

def cast_dtypes(df:pd.DataFrame) -> pd.DataFrame:

    df['ticker'] = df['ticker'].astype('category')
    df['date'] = pd.to_datetime(df['date'])
    df['open'] = df['open'].astype(np.float16)
    df['high'] = df['high'].astype(np.float16)
    df['low'] = df['low'].astype(np.float16)
    df['close'] = df['close'].astype(np.float16)

    return df

df = pd.concat([cast_dtypes(pd.read_csv(file)) for file in STOCK_FILES])

tickers = pd.read_csv(TICKER_PATH)

res_df = df.merge(tickers, how='inner', right_on='ticker', left_on='ticker')

res_df.to_csv(RESULT_PATH, index=False)