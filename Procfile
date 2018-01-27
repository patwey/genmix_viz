web: gunicorn genmix_viz.wsgi --log-file -
worker: celery -A genmix_viz worker -l info
