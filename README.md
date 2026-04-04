```
INICIO
cd ~/Desktop/EstudioT/CursoPython/Backend
source .venv/Scripts/activate
code .
DESACTIVAR .VENV
deactivate
```
```
CREAR RAMA , UNIR RAMA Y SUBIR A GIHUB
Crear rama
git switch -c nombre-rama

Trabajar y guardar cambios
git add .
git commit -m "mensaje corto claro"

Volver a main
git switch main

Unir rama a main
git merge nombre-rama

Subir a GitHub
git push

ACTUALIZAR COMMIT
git commit --amend --no-edit
git push --force-with-lease
```
```
TIPO COMMITS
feat: → nueva funcionalidad
fix: → corrección
chore: → cosas internas
```
```
Uvicorn 
Inicia Server: uvicorn main:app --reload
Detener Server: Ctrl + C

DOCUMENTACION
/docs
/redoc
```
```
HTTP Methods (CRUD básico)
GET → leer datos → READ
POST → crear datos → CREATE
PUT → actualizar datos → UPDATE
DELETE → eliminar datos → DELETE
```

```
02:05:10 | 09 - Path y Query
PATH → identifica exactamente qué recurso quieres / obligatorio, estructura la API
QUERY → modifica o filtra la búsqueda de recursos / opcional, agrega filtros

Ejemplo:

GET /users/1
→ un usuario específico

GET /users?age=24
→ usuarios con edad 24
```
