## URL Shortener API

Project consists to allow a user to transform a long web url into a pattern-consistent (encoded) small url easy to share and remember.

At the same time the user is allowed to transform back (decode) the small url into the original url

It is partly tested as only and was developed as showcase only.

How Url Shortener API Works:

You can send (POST) a full url and retrieve a small encoded one with tier.app as the base web service url.

Eg. POST http://127.0.0.1:8000/api/short-url/ with https://www.google.com/search?q=google&oq=google+&aqs result: http://127.0.0.1:8000/api/upxFJp (6 digits id)

You can get the original url with the encoded url on a GET request (done in previous step)

Eg. GET http://127.0.0.1:8000/api/upxFJp result: https://www.google.com/search?q=google&oq=google+&aq


## Installation:
1) Clone repository and go inside the repository folder "url-shortener-api"

```
git clone https://github.com/sandrikkk/URL-Shortener-API.git
```

2) Create you virtualenv and install the packages

```
pip install -r requirements.txt
```

3) Initialize database and create the database mapping used for persistance in the url shortener API.

```
python manage.py makemigrations
```

4) Apply the database mapping from the app to the database; migrate the database.

```
python manage.py migrate
```

5)Run the application.
```
python manage.py runserver
```

<br>

## USAGE
#### 1. Endpoint List
URI Example: `http://127.0.0.1:8000/api/short-url/`


| | Available Methods | URI | Example URL |
| -: | :- | :- | -: |
| | | | |
| | **Project Endpoints** | | |
| 1. | `POST` | `/api/short-url/` | `http://127.0.0.1:8000/api/short-url/` |
| 2. | `GET`  | `/api/short-url/<id>/` | `http://127.0.0.1:8000/api/short-url/<id>/` |
| 2. | `DELETE`  | `/api/short-url/<id>/` | `http://127.0.0.1:8000/api/short-url/<id>` |


<br>
