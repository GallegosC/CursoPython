from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pwdlib import PasswordHash
from pydantic import BaseModel


#1. antes ya estaba la libreria jwt , la pognog nuevamenete
from jose import jwt, JWTError

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
#3. PARA SER HONESTO NOE ENTENDI BIEN ESTA PARTE
SECRET = "11c0ea3ecee0190ed294138092e14f934af844df972055ab1275b071838c93a8"
#4. el secret se scao con "openssl rand -hex 32"
#5. DESPUES DE ESTO SE SIGUIO CON EL VER QUE BOTA EN EL THUNDER Y DEJO AL FINAL LO MISO PERO CODIFIcado 


router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = PasswordHash.recommended()


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "JesusG": {
        "username": "JesusG",
        "full_name": "Jesus Gallegos",
        "email": "jesus.gallegos@upsjb.edu.pe",
        "disabled": False,
        "password": crypt.hash("123456")
    },
    "AylinP": {
        "username": "AylinP",
        "full_name": "Aylin Ponce",
        "email": "aylinpS@256.com",
        "disabled": True,
        "password": crypt.hash("654321")
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])



async def auth_user(token:str = Depends(oauth2)):

    exception =  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticacion invalidas", 
            headers={"WWW-Authenticate": "Bearer"})


    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None :
            raise exception
            

    except JWTError:
        raise exception
    
    return search_user(username)
        

async def current_user(user: User = Depends(auth_user)):
    # Si el usuario está desactivado    
    if user.disabled:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail="Usuario Inactivo")

    return user



@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)

    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto"
        )

    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta"
        )

    access_token = {
        "sub": user.username,
        "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }



#2. se cambio esta parte
    return {
        "access_token": jwt.encode(access_token,SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }



@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

