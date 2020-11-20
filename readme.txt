Steps to test the project.

Clone the repo using : git clone https://github.com/dipesh2597/TaskScheduler.git

Install python in case if you don't have it.

create a virtual environment: virtualenv <you_environment_name>

activate venv: source ./<virtual_env_name>bin/activate

Install requirements: pip install -r requirements.txt

Run makemigrations and migrate: python manage.py makemigratiosn && python manage.py migrate

Runserver: python manage.py runserver

Register: localhost:8000/register

Login: localhost:8000/login

View your tasks: localhost:8000/task
