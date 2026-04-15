#Instala FastAPI: pip install "fastapi[standard]"
from fastapi import FastAPI
from Routers import products, users

app  = FastAPI() 


#Inicia Server: uvicorn main:app --reload


#Routers
app.include_router(products.router)
app.include_router(users.router)



#Url local: https://127.0.0.1.8000
@app.get("/")
async def root():
    return "Hola Fastapi"

#Url local: https://127.0.0.1.8000/url
@app.get("/url")
async def url():
    return { "url_curso":"https://mouredev.com/python" }

#Inicia Server: uvicorn main:app --reload
#Detener Server: Ctrl + C
