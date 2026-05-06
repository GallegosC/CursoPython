# Importaciones nuevas para OAuth2
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router  = APIRouter()

# Configura OAuth2: especifica dónde se obtiene el token (/login)
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
 
# User: estructura PÚBLICA (sin password) - lo que se muestra al cliente
class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# UserDB: estructura INTERNA (incluye password) - solo para validación
class UserDB(User):
    password: str


# "Base de datos" en memoria - KEY debe ser igual al username
users_db = {
    "JesusG": {
        "username": "JesusG",
        "full_name": "Jesus Gallegos",
        "email": "jesus.gallegos@upsjb.edu.pe",
        "disabled": False,
        "password": "123456"
    } ,
    "AylinP": {
        "username": "AylinP",
        "full_name": "Aylin Ponce",
        "email": "aylinpS@256.com",
        "disabled": True,
        "password": "654321"
    }
}

# Busca usuario por username (KEY del diccionario)
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
# Busca usuario y retorna tipo User (sin password)
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
# Verifica token Bearer y valida usuario
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)

    # Si no existe el usuario
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de atenticacion invalidas", 
            headers={"WWW-Authenticate": "Bearer"})
    
    # Si el usuario está desactivado    
    if user.disabled:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="Usuario Inactivo")

    return user


# LOGIN: valida credenciales y genera token
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    # Busca usuario en "BD"
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El usuario no es correcto")
    
    # Verifica password
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="El contraseña no es correcta")
    
    # Retorna token (username como token simplificado)
    return {"access_token": user.username, "token_type": "bearer"}


# RUTA PROTEGIDA: requiere token válido
@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

