```
24/03/2026
Primero creo la carpeta principal del proyecto (CursoPython) y ahí inicializo Git con git init, porque ese será
el repositorio que abarque todo. Luego creo el archivo .gitignore, donde defino qué cosas no quiero que Git
registre (como .venv o __pycache__).

Después, dentro de esa carpeta principal, creo subcarpetas para proyectos específicos (por ejemplo Backend) y en
cada una creo su entorno virtual con python -m venv .venv y lo activo.

Una vez listo eso, trabajo en local (instalo librerías, escribo código, etc.). Luego uso git add, git commit y
git push para subir los cambios a GitHub.

Solo uso git pull cuando hay cambios en GitHub que necesito traer a mi entorno local (por ejemplo, si edité el
README desde la web).
```

```
INICIO
cd ~/Desktop/EstudioT/CursoPython/Backend
source .venv/Scripts/activate
code .

SUBIR A GITHUB
git add .
git commit -m "mensaje corto claro"
git push

DESACTIVAR .VENV
deactivate

TIPO COMMITS
feat: -> nueva funcionalidad
fix: -> corrección
chore: -> cosas internas

DOCUMENTACION
http://xxx.x.x.x:xxxx/docs
http://xxx.x.x.x:xxxx/redoc
```
```
31/03/2026
Se implementa la base de FastAPI, incluyendo creación de endpoints ("/" y "/url") y ejecución del
servidor con uvicorn para pruebas locales.
```
