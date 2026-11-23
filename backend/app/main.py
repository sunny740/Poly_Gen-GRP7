from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
backend/app/main.py :
app = FastAPI(title='PolyGen API')
app.add_middleware(CORSMiddleware, allow_origins=['http://localhost:5173'],
allow_methods=['*'], allow_headers=['*'])
@app.get('/health')
def health():
return {'status': 'ok'}
