# Learning `RestAPI` using `Django`

CRUD application with basic authentication.

## MOVIE

-   Create: POST `/api/movies/add_movie/` **requires authentication**
-   Read:
    -   GET `/api/movies/` **Public API**
    -   GET `/api/movies/<id>/` **Public API**
-   Update: POST `/api/movies/edit_movie/<id>/` **requires authentication**
-   Delete: DELETE `/api/movies/delete_movie/<id>/` **requires authentication**

## USER

-   Create: POST `/api/register/`
-   Read:
    -   POST `/api/login/`

## WATCHLIST

-   Create: POST `/api/create_watchlist/` **requires authentication**
-   Read:
    -   POST `/api/get_user_watchlists/` **requires authentication**


>Start Project locally:
1. `python -m venv venv`
2. `source venv/bin/activate` | `venv/Scripts/activate`
3. `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py runserver --settings=config.settings.local`


> Deploy to Heroku:
1. `Create heroku account and donwload the cli`
2. `heroki login`
3. `Create Procfile`  add this in the file `web: gunicorn <PROJECT_NAME>.wsgi` where <PROJECT_NAME> is the folder that contains the `wsgi.py` file
4. `Install require packages`
   1. django-heroku
   2. gunicorn
   3. psycopg2
   4. python-decouple
   5. whitenoise
5. `pip freeze > requirements.txt`
6. `git push heroku master`
7. `heroku run --app <APP_NAME> python manage.py migrate`
8. `heroku run --app <APP_NAME> python manage.py collectstatic`
9. `heroku run --app <APP_NAME> python manage.py createsuperuser`