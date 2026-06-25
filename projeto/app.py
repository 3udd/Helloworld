import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()
DATABASE_URL = os.getEnv('DATABASE_URL')

@app.get("/")
def home():
    return "Projetinho fellas"

@app.get("/teste-banco")
def testeBanco():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = 'SELECT * FROM USERS'
            result = con.execute(text(sql))
            usuarios = result.fetchall()
            return usuarios._mapping
    
    except:
        return "Banco indisposto"

if __name__ == '__main__':
    uvicorn.run(
        'app:app',
        port = 80,
        reload=True
    )