# stockosaurus-api

Setup
----

>Prerequisites: Install python3.9, https://www.python.org/downloads/

Create and activate venv

Install dependencies ```pip install -r requirements.txt```

>Prerequisites: Install docker / docker-compose, https://docs.docker.com/compose/install/

Start Postgres database: ```docker-compose up ```

Run database migration ```python manage.py migrate```

Run Django server ```python manage.py runserver```

Access application http://127.0.0.1:8000/
