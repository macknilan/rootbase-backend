# Rootbase-backend

Proyecto API que sirve de base con la administración de usuarios para diferentes tipos de proyectos realizado con   
:link: :octocat: [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

La documentación :notebook: del API esta realizada con _Postman_ ![POSTMAN](https://github.com/postmanlabs/postman-docs/blob/develop/src/images/favicon.png "POSTMAN") :link: [Rootbase-backend :notebook:](https://documenter.getpostman.com/view/8810189/TVCh1Tmu)

![https://github.com/pydanny/cookiecutter-django/](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg "Built with Cookiecutter Django")
![https://github.com/ambv/black](https://img.shields.io/badge/code%20style-black-000000.svg "Black code style")

|   	License|   	MIT|
|---	|---	|

El objetivo de este proyecto es tener una API con Django que sirva inicialmente para la administración de usuarios (CRUD) y posteriormente se impemente la logica del negocio,que requiera administración de usuarios.


### :house: Cookiecutter Django Settings

#### Settings

:link: [Moved to settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html)

#### Basic Commands

##### Setting Up Your Users
+ To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.
+ To create an **superuser account**, use this command
```bash
$ python manage.py createsuperuser
```
For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

#### Type checks
Running type checks with mypy:
```bash
mypy rootbase
```

#### Test coverage
To run the tests, check your test coverage, and generate an HTML coverage report:
```bash
$ coverage run -m pytest
$ coverage html
$ open htmlcov/index.html
```
#### Running tests with py.test
```bash
$ pytest
```

#### Live reloading and Sass CSS compilation
Moved to [Live reloading and SASS compilation.](http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html)


### Celery
This app comes with Celery.   
To run a celery worker:
```bash
cd rootbase
celery -A config.celery_app worker -l info
```
Please note: For Celery's import magic to work, it is _important where_ the celery commands are run. If you are in the same folder with `manage.py`, you should be right.

#### Email Server
In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server [MailHog](https://github.com/mailhog/MailHog) with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers. Please check [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html) for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to `http://127.0.0.1:8025`

#### Sentry
Sentry is an error logging aggregator service. You can sign up for a free account at [https://sentry.io/signup/?code=cookiecutter](https://sentry.io/signup/?code=cookiecutter) or download and host it yourself. The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

#### Deployment
The following details how to deploy this application.

#### Docker
See detailed [cookiecutter-django Docker documentation.](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html)

```bash
```

#### Commands for Docker :whale2: to work with :link: :octocat: [cookiecutter-django](https://github.com/pydanny/cookiecutter-django)

#### Basic Docker
```bash
$ docker images
$ docker container
$ docker volume
$ docker network
# PARA CADA UNO
ls
rm
prune
-a
-q
```
#### Docker images
Listar todos las imagenes
```bash
docker images -a
```

#### Docker containers

List all containers
```bash
$ docker container ls -a
```
Stop all containers
```bash
$ docker container stop $(docker container ls -aq)
```
Stop and delete all containers
```bash
$ docker container rm $(docker container ls -aq)
```
Delete all containers stoped, images and networks unused
```bash
$ docker system prune
```
Delete all volumes unused
```bash
$ docker system prune --volumes
```

#### Some commands of `docker-compose`
```bash
# COMPOSE_FILE
$ export COMPOSE_FILE=local.yml

$ docker-compose build
$ docker-compose up
$ docker-compose ps
$ docker-compose down
```

#### Docker-compose imagenes
```bash
# Para construir las imagenes
$ docker-compose -f local.yml build

# Para correr el stack
$ docker-compose -f local.yml up

# Para ver el estado de los procesos de Docker
$ docker-compose -f local.yml ps

# Para detener la ejecución
$ docker-compose -f local.yml down
```

#### Administration commands
La bandera `--rm` lo que hace es que crea un contenedor solo para el fin indicado y cuando acabe de ejecutarse el comando **mata el contenedor**
```bash
# Para correr comandos de Django usamos
docker-compose run --rm django COMMAND
# 
# Por ejemplo para crear un super usuario
docker-compose run --rm django python manage.py createsuperuser
```
#### Make debugger
```bash
# 1 Para correr el stack de contenedores
# -f, --file FILE             Specify an alternate compose file
$ docker-compose -f local.yml up
```
```bash
# 2 Saber con que nombre esta el contenedor
# -f, --file FILE             Specify an alternate compose file
# ps List containers
$ docker-compose -f local.yml ps
```

```bash
# 3 MATAR EL DOCKER DJANGO
# -f, --force     Force the removal of a running container (uses SIGKILL)
# -l, --link      Remove the specified link
# -v, --volumes   Remove anonymous volumes associated with the container
$ docker rm -f <ID>
```
```bash
# 4 DESPUES DE SACAR/MATAR EL DOCKER DE django PARA LEVANTAR LO DE NUEVO ES
# run Run a one-off command
# rm Remove stopped containers
$ docker-compose -f local.yml run --rm --service-ports django
# Hacer migraciones
$ docker-compose -f local.yml run --rm django python manage.py makemigrations
# Migrar a la BD
$ docker-compose -f local.yml run --rm django python manage.py migrate
# EJEMPLO PARA CREAR SUPER-USUARIO
$ docker-compose -f local.yml run --rm django python manage.py createsuperuser
# 
$ 
# 
$ 
# 
$ 
# 
$ 
# Cuando se presentan problemas con las migraciones y una opción es que se elimine el "volumen" de la BD donde se almacena la data tiene la terminación NOMBRE DEL PROYECTO_postgres_data
#Primero se tiene que detener la ejecucion de docker-compose
$ docker-compose -f local.yml down
# Mostrar los volunenes de docker
$ docker volume ls
# Eliminar el volimen NOMBRE DEL PROYECTO_postgres_data
$ docker volume rm NOMBRE DEL PROYECTO_postgres_data
```






















































































