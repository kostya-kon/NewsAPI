from django.urls import path
from .views import PostAPIView, CommentAPIView, SinglePostAPIView, RateAPIView

app_name = "newsapp"

urlpatterns = [
    path("posts/", PostAPIView.as_view()),  # get/post
    path("posts/<int:pk>", SinglePostAPIView.as_view()),  # get/put/delete
    path("comments/<int:id_post>", CommentAPIView.as_view()),  # get/post
    path("comments/<int:id_post>/<int:id_comment>", CommentAPIView.as_view()),  # put/delete
    path("rate/<int:id>", RateAPIView.as_view()),  # get
]
