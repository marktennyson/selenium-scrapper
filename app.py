from fastapi import FastAPI, Request
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from components import Fetcher, Scrapper

app:FastAPI = FastAPI()
app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
@app.get('/')
def index(request:Request):
    return {'status':'online', 'host':request.headers.get('host')}

@app.get('/scrap')
async def scrap():
    url = 'https://cointelegraph.com'
    resp = Fetcher(url)
    html_data = await resp.html()
    scrapper = Scrapper(html_data)
    data = scrapper.data()
    return {'data':data}
    

if __name__ == '__main__':
    run('app:app', host='0.0.0.0',port=8000, log_level='info')