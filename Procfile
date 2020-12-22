web: gunicorn news.wsgi --log-file -
worker: celery -A news worker -B --loglevel=info