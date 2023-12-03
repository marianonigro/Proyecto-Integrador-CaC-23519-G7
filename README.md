## CRUD con Python y MySQL

##### CRUD utilizando Python Flask y MySQL

Virtual Environment Coco a Codo
cd ~
cd mkd proyecto_name
code .
python3 -m venv venv
source ./venv/bin/activate
git init
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy pymysql -U flask-cors 
pip freeze
pip freeze > requirements.txt
pip install requirements
pip install -r requirements.txt

crear .gitignore

**/venv
.vscode
uploads
__pycache__
*.py[cod]
.pytest_cache
.env

www.toptal.com/developers/gitignore
(python macos windows linux venv)


Shortcut Bash:

cmd + shift + punto (muestra ocultos macos)
mkdir nombre_de_la_carpeta && touch nombre_del_archivo

### Requerimientos 📋

    Servidor Web (Apache)
    MySQL 5 o superior
    phpMyAdmin (opcional)
    Puedes usar un todo en uno como XAMPP, WAMPP u otro.

    Incorpora los datos del sql a tu mysql, crea el environment virtual,
    activalo, instala los requerimientos, el .gitignore ya esta oculto y por ultimo corre el app.py
    Si esta todo ok te va a dar un mensaje con la direccion de localhost puerto 5000 y ahí te vas a
    encontrar con una leyenda API Ok!!! 



