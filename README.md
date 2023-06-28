# elevators_svc
An elevator system, which can be initialised with N elevators and maintains the elevator states as well.

## base requirements
1. python - 3.7.6

## setup steps
1. Create a virtual environment using command `virtualenv -p python3 venvElevators` and activate it. 
2. Install django and django rest framework using : `pip install django djangorestframework`
3. Add requirements into requirements.txt
4. Setup Django using  `django-admin startproject elevators_svc .`
5. Create apps `users` and `elevators` using `python manage.py startapp <app_name>`
6. For setting it database connection : `pip install psycopg2-binary`
7. Add `DB_NAME`, `DB_USERNAME`, `DB_PORT`, `DB_PASSWORD` `DB_HOST` variables into .env
8. Run `pip install python-decouple`