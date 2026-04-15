# IMPORTACIONES
from fastapi import FastAPI, HTTPException  #Crea la app/API
from pydantic import BaseModel #Define la estructura de datos


# CREAR LA APP
## Crea la aplicacion web/API  
## Todo lo que tenga @app.get(...) cuelga de esta app.
app  = FastAPI()  


#Inicia Server: uvicorn users:app --reload

# Entidad User 
## Define como verse el usuario 
## Todo User debe tener esos campos
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


# LISTA DE USUARIOS
users_list = [User(id=1 , name= "Brais", surname= "moure", url= "https://moure.dev", age= 35), 
              User(id=2 , name= "Jesus", surname= "G", url= "https://Jess.G", age= 24), 
              User(id=3 , name= "Haakon", surname= "Dahlberg", url= "https://haakon.com", age= 33) ]



# Endpoint /usersjson
## Crea un endpoint GET que devuelve JSON escrito a mano.
@app.get("/usersjson") 
async def usersjson():
    return [{ "name": "Brais", "surname": "moure", "url": "https://moure.dev", "age":35},
            { "name": "Jesus", "surname": "G", "url": "https://jesus.G", "age":24},
            { "name": "Haakon", "surname": "Dahlberg", "url": "https://haakon.com", "age":33}]


# Endpoint /users
## Devuelve la lista completa de usuarios.

@app.get("/users")
async def users():
    return users_list


# Endpoint PATH
## Busca un usuario usando el id dentro de la URL.
## Ejemplo: ..../user/1

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Endpoint QUERY
## Recibe datos por query string. 
## Ejemplo: ..../user/?id=1


## GET
@app.get("/user/")
async def user(id: int):
    return search_user(id)

## POST
## response_model=User -> define la estructura de la respuesta exitosa
## status_code=201 -> indica que el usuario fue creado correctamente
@app.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    
    
    users_list.append(user)
    return user 
    

## PUT
@app.put("/user/")
async def user(user:User):

    found = False


    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return{"error": "No se ha actualizado el usuario"}
    else:
        return user
    

## DELETE
@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
            return{"error": "No se ha eliminado el usuario"}



# Función search_user
## Busca dentro de users_list el usuario cuyo id coincida.

def search_user(id=int):
    users = filter(lambda user: user.id == id, users_list) #Filtra la lista y se queda solo con los usuarios cuyo id sea igual al que enviaste.

    try:
        return list(users)[0] #convierte el resultado filtrado en lista y agarra el primer elemento
    except:
        return {"Error":"No se ha encontrado el usuario"}
    




