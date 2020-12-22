from django.db import models


class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=30)
    link = models.URLField()
    creation_date = models.DateField()
    amount_of_upvotes = models.IntegerField()
    author_name = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment model"""

    author_name = models.CharField(max_length=40)
    content = models.TextField()
    creation_date = models.DateField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return "/".join(
            [str(self.post), str(self.author_name), str(self.creation_date)]
        )
