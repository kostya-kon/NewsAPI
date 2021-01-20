from __future__ import absolute_import, unicode_literals
from news.celery import app

from .models import Post


@app.task()
def reset():
    """Celery Task for reseting votes of posts"""
    posts = Post.objects.all()
    for post in posts:
        post.amount_of_upvotes = 0
        post.save()
    return "RESET"
