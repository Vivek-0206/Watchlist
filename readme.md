Learning rest API from Pure Django

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
