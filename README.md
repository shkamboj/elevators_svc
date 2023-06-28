# elevators_svc
An elevator system, which can be initialised with N elevators and maintains the elevator states as well.

## Base Requirements
1. Python - 3.7.6
2. PostgreSQL - psql (PostgreSQL) 10.22 (Ubuntu 10.22-0ubuntu0.18.04.1)

## Setup Steps
1. Create a virtual environment using command `virtualenv -p python3 venvElevators` and activate it. 
2. Install django and django rest framework using : `pip install django djangorestframework`
3. Add requirements into requirements.txt
4. Setup Django using  `django-admin startproject elevators_svc .`
5. Create apps `users` and `elevators` using `python manage.py startapp <app_name>`
6. For setting it database connection : `pip install psycopg2-binary`
7. Add `DB_NAME`, `DB_USERNAME`, `DB_PORT`, `DB_PASSWORD` `DB_HOST` variables into .env
8. Run `pip install python-decouple`


## Demo Run
1. Run the application on port 8000.
2. To create n elevators in system : `curl -X POST -H "Content-Type: application/json" -d '{"num_elevators" : 10}' http://localhost:8000/create-elevators/`
3. To save and serve an elevator request : `curl -X POST -H "Content-Type: application/json" -d '{"current_floor": 1, "destination_floor": 5}' http://localhost:8000/api/elevator-requests/`
4. To fetch all the requests of an elevator : `curl -X GET -H "Content-Type: application/json" -d '{}' http://localhost:8000/api/elevators/<elevator_id>/elevator-requests/`
5. To fetch the next destination/direction/door state : `curl -X GET -H "Content-Type: application/json" -d '{}' http://localhost:8000/api/elevators/<elevator_id>/`
6. Mark elevator as not working : `curl -X PATCH -H "Content-Type: application/json" -d '{}' http://localhost:8000/api/elevators/<elevator_id>/mark-not-working/`
7. Mark elevator in maintenance : `curl -X PATCH -H "Content-Type: application/json" -d '{}' http://localhost:8000/api/elevators/<elevator_id>/mark-in-maintenance/`
8. Open the elevator door : `curl -X GET -H "Content-Type: application/json" -d '{}' http://localhost:8000/api/elevators/<elevator_id>/open-door/`
9. CLose the elevator door : `curl -X GET -H "Content-Type: application/json" -d '{}' http://localhost:8000/api/elevators/<elevator_id>/close-door/`



## Assumptions made 
1. As soon as request comes, it gets served, so only one destination at a time. 
2. No floor limit added.
