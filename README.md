# NewsAPI

## documented with Postman collection
https://documenter.getpostman.com/view/13378615/TVsvg6Sr

## Deployed on Heroku
https://newsposts-api.herokuapp.com

## How to install local
- clone or download `clone https://github.com/tvoi-kotik/NewsAPI`
- install env `virtualenv venv`
- activate it `source myenv/bin/activate`
- set requirements `pip install -r requirements.txt`
- make migrations `python manage.py makemigrations`, `python manage.py migrate`
- run `python manage.py runserver`

If u want to run celery task:
- open two new cmd
- activate env
- in first `celery -A news worker -l info`
- in second `celery -A news beat -l info`


## About app
There are two pages.

1st - Home - List of News with rate.

2nd - Comment of any news - News and list of comments.
