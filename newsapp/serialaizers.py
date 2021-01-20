from datetime import datetime

from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.Serializer):
    """Serialaizer for Post Model"""
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=30)
    link = serializers.URLField()
    creation_date = serializers.DateField(required=False)
    amount_of_upvotes = serializers.IntegerField(required=False)
    author_name = serializers.CharField(max_length=40)

    def create(self, validated_data):
        """Setting votes and date automatically"""
        # print(validated_data)
        validated_data["creation_date"] = datetime.now().date()
        validated_data["amount_of_upvotes"] = 0
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Method for put requests"""
        instance.title = validated_data.get("title", instance.title)
        instance.link = validated_data.get("link", instance.link)
        instance.author_name = validated_data.get("author_name",
                                                  instance.author_name)

        instance.save()
        return instance


class CommentSerializer(serializers.Serializer):
    """Serializer for Comment Model"""
    id = serializers.IntegerField(required=False)
    author_name = serializers.CharField(max_length=40)
    content = serializers.CharField()
    creation_date = serializers.DateField(required=False)
    post_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """Setting user ForeignKey by his id"""
        # print(validated_data)
        validated_data["creation_date"] = datetime.now().date()
        validated_data["post"] = Post.objects.get(pk=validated_data["post_id"])
        validated_data.pop("post_id")

        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """Method for put requests"""
        instance.author_name = validated_data.get("author_name ",
                                                  instance.author_name)
        instance.content = validated_data.get("content", instance.content)

        instance.save()
        return instance
