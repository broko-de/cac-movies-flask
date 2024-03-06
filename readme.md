# Proyecto cac-movies-flask

Este es un proyecto de software desarrollado en python 🐍 por medio del framework Flask, con la finalidad de implementar el backend del proyecto cac-movies. Se trabaja con una entidad Movies y una conexión a una base de datos Mysql.

El proyecto requiere la implementación de un entorno virtual de python y trabaja con variables de entorno para la manipulación de las credencias de conexión con la base de datos.

### Instalacion
Para poder correr el proyecto, vas a tener que seguir los siguientes pasos (para sistema operativo Windows):

1. Clonar el repositorio del repositorio
```
git clone https://github.com/broko-de/cac-movies-flask.git
```
2. Crear un entorno virtual para el proyecto y activarlo
```
python -m venv env
env/Script/activate
```
3. Instalar las dependencias del proyecto
```
cd cac-movies-flask
pip install -r requirements.txt
```
4. Crear un archivo .env en el directorio raiz y completar con los datos de configuración segun lo indica .env.example
5. Por último, correr el proyecto por medio del servidor de desarrollo de flask. Lo podemos hacer desde la terminal ejecutando el siguiente comando
```
python run.py
```