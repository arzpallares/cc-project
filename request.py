import pandas as pd

from utils import STOCK_NAME_URL, TICKER_PATH

df = pd.read_csv(STOCK_NAME_URL, encoding='utf-8')
df2 = df.rename(columns={'ACT Symbol': 'ticker', 'Company Name': 'company'})

df2.to_csv(TICKER_PATH, index=False)