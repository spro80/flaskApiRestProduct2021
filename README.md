# flaskApiRestProduct2021
api python flask


# RUN in local:
<!-- 
Ejecutar API localmente:
FLASK_ENV=development flask run
export FLASK_APP=app
flask run
-->


# ACTIVAR EL ENTORNO VIRTUAL LOCALMENTE:
<!--
python3 -m venv venv  : con esto se crea directorio venv
. venv/bin/activate   : activa entorno virtual
pip freeze            : podemos ver las librerias instaladas (luego de instalar cualquier libreria se debe actualizar este archivo)
-->



# DEPLOY TO HEROKU:
<!--
guia subir a heroku:
https://realpython.com/flask-by-example-part-1-project-setup/
-->



# INSTALL LIBRARY:
<!--

Teniendo activado el entorno virtual, instalaremos las siguientes librerias:

~/Escritorio/HEROKU/PYTHON/FLASK/SapFlask$ python --version
(venv) david@dNitro:~/Escritorio/SapFlask$ python -m pip install flask

(venv) david@dNitro:~/Escritorio/SapFlask$ python -m pip install flask-sqlalchemy

(venv) david@dNitro:~/Escritorio/SapFlask$ python -m pip install flask-migrate

(venv) david@dNitro:~/Escritorio/SapFlask$ python -m pip install psycopg2    : (extension de postgress)


venv) david@dNitro:~/Escr/flaskApiRestProduct2021$ pip3 install -U setuptools

venv) david@dNitro:~/Escr/flaskApiRestProduct2021$ pip3 install flasgger

-->



# UPDATE requirements:
<!--
Luego de instalar cualquier libreria, se debe actualizar el archivo con las librerias:

(venv) david@dNit:~/Escr/flaskApiRestProduct2021$ pip freeze > requirements.txt
-->

# SQL Alchemy
<!--
Crearemos una BD llamada:   sap_flask_db 

(venv) david@dNitro:~/Escritorio/SapFlask$ flask db init
Con este comando se crea el directorio: migrations

(venv) david@dNitro:~/Escritorio/SapFlask$ flask db migrate
Con este comando se crea archivo py, con instrucciones listas para actualizar la base de datos.

(venv) david@dNitro:~/Escritorio/SapFlask$ flask db upgrade
Con este comando se actualiza la BD, creando los archivos que tenemos en nuestro model.

(venv) david@dNitro:~/Escritorio/SapFlask$ flask db stamp head
-->


<!--
Sql alchemy es una lib de tipo orm, nos va a permitir crear clases de modelo y nos va permitir mapear estas clases de modelo 
hacia la BD. En Flask no tenemos disponible la extension como en Dyango, es por eso que usaremos SQL Alchemy que es bastante similars 

Una de las ventajas de trabajar con flask es que existen integraciones, por ejemplo SQL Alchemy es una libreria por separado,
pero para integrarlo con Flask existe flask-SQLAlchemy y con esto se facilita el trabajo con flask 

flask-migrate, es muy similar a lo visto con Dyango, sin embargo, con Dyango tenemos disponible el concepto de migraciones 
de manera inmediata tanto el ORM de Dyango y tambien el concepto de migraciones. En Flask no es asi por lo tanto vamos a instalar tambien 
este plugin de flask migrate . Asi que damos enter y podemos ver que similar a SQL Alchemy el proyecto que se usa de base es el proyecto alembic
Installing collected packages: six, python-editor, python-dateutil, Mako, alembic, flask-migrate

Este es el proyecto que nos va a permitir realizar las migraciones

Asi que por un lado SqL Alchemy nos permite el mapeo de nuestras clases de modelos ahacia la Base de datos y el proyecto de 
alembic lo que nos va a hacer es crear los archivos de migraciones y poderlas ejecutar para que finalmente podamos 
observar la creacion de las tablas sobre nuestra base de datos 

Cualquier duda se puede ir a la documentacion de alembic o sqlalchemy
Por ultimo dado que vamos a trabajar con Postgres vamos a trabajar con Postgres vamos a instalar la extension de postgres 



-->


# Refactorizar modelo
<!-- 
Creamos: models.py en la raiz del proyecto
-->