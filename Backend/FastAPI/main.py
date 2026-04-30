#Instala FastAPI: pip install "fastapi[standard]"
from fastapi import FastAPI

# Importa routers modularizados
from Routers import products, users

# Importa módulo para servir archivos estáticos (imágenes, CSS, JS)
from fastapi.staticfiles import StaticFiles

# Crea la aplicación principal
app  = FastAPI() 

#Inicia Server: uvicorn main:app --reload

# Integra routers (conecta módulos a la app)
app.include_router(products.router)
app.include_router(users.router)
#
app.mount("/static", StaticFiles(directory="static"), name="static")


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
