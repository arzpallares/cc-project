from fastapi import FastAPI, Response
import pandas as pd

from utils import RESULT_PATH

app = FastAPI()

@app.get('/')
async def home():

    message = {'message': 'Welcome to NYSE historic data API. To request data of stocks go to /ticker/[ticker]'}
    return Response(content=str(message), media_type='application/json')

@app.get('/ticker/{ticker}')
async def retrieve_data(ticker:str):
    """
    Search stock history of company using ACT Symbol (ticker) as reference.
    """
    ticker = ticker.upper()
    df = pd.read_csv(RESULT_PATH).query('ticker == @ticker')

    if not df.empty:
        # Split DataFrame into column and data lists
        cols = df.columns.values.tolist()
        data = df.values.tolist()

        # Insert column list at the beginning of the data list
        data.insert(0, cols)

        # Combine list of list into a single text
        cont = '\n'.join([','.join(map(str, row)) for row in data])

        return Response(content=cont, media_type='text/csv')
    
    message = {'message': f'We could not find {ticker} in the NYSE stock list.'}
    return Response(content=str(message), media_type='application/json')