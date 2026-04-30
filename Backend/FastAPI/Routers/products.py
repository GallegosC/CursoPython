# IMPORTACIONES
from fastapi import APIRouter


# Router para agrupar endpoints relacionados a productos
router = APIRouter(prefix="/products",
                   tags=["Products"], #esto es para la documentacion 
                   responses={404: {"message":"No encontrado"}})

#Inicia Server: uvicorn products:app --reload

products_list=["Producto_01","Producto_02",
               "Producto_03","Producto_04","Producto_05"]


@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]