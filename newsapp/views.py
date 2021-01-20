from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponsePermanentRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    get_object_or_404,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Post, Comment
from .serialaizers import PostSerializer, CommentSerializer


class NewsView(ListView):
    """Home page view with list of news"""

    model = Post

    def get_queryset(self):
        return Post.objects.all().order_by("-amount_of_upvotes")


class CommentView(View):
    """Comment page view with comments to some post"""

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        comments = Comment.objects.filter(post=post)
        return render(
            request,
            "newsapp/comment.html",
            context={"post": post, "com_list": comments},
        )


class RateView(View):
    """View for rate some post and than redirect to home page"""

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        post.amount_of_upvotes += 1
        post.save()
        return HttpResponsePermanentRedirect("/")


class PostAPIView(ListCreateAPIView):
    """Generic api view for post`s(get/post)"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SinglePostAPIView(RetrieveUpdateDestroyAPIView):
    """Generic api view for post`s(get(but one)/put/delete)"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# For comment view i used APIView, because it`s more flexible
# I want that when a GET request is made, not all objects are returned,
# but only comments for a post with a specific ID
# I cant realize it with Generic`s, that the reason of using APIView here

class CommentAPIView(APIView):
    """API View for Comments"""

    def get(self, request, id_post):
        """Returns list of comments of post with some pk(id)"""
        comments = Comment.objects.filter(post__pk=id_post)
        serialaizer = CommentSerializer(comments, many=True)

        return Response({"post pk": id_post, "comments": serialaizer.data})

    def post(self, request, id_post):
        """Creating comment for some post(write id on url)"""
        comment = request.data.get("comment")
        comment["post_id"] = id_post

        serializer = CommentSerializer(data=comment)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()

        return Response(
            {
                "success": "Comment '{0}' for post pk {1} created".format(
                    comment_saved.creation_date, id_post
                )
            }
        )

    def put(self, request, id_post, id_comment):
        """Editing of comments, it`s flexible, u can change not all fields"""
        saved_comment = get_object_or_404(Comment.objects.all(), pk=id_comment)
        data = request.data.get("comment")

        serializer = CommentSerializer(instance=saved_comment,
                                       data=data,
                                       partial=True)
        if serializer.is_valid(raise_exception=True):
            comment_saved = serializer.save()

        return Response(
            {
                "success": "Comment '{}' updated successfully".format(
                    comment_saved.creation_date
                )
            }
        )

    def delete(self, request, id_post, id_comment):
        """Deleting comment by it id and post id"""
        comment = get_object_or_404(Comment.objects.all(), pk=id_comment)
        comment.delete()

        return Response(
            {"message": "Comment > id `{}` was deleted.".format(id_comment)},
            status=204,
        )


class RateAPIView(APIView):
    """Same to RateView, but for API"""

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        post.amount_of_upvotes += 1
        post.save()

        return Response(
            {
                "message": "Post with id `{}` has been rated.".format(id)},
            status=204
        )
