# blog/serializers.py
from rest_framework import serializers
from .models import Blog, BlogImage, Comment, Project, ProjectImage, ProjectComment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']
        read_only_fields = ['created_at']  # Automatically set

class BlogImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # Returns full URL

    class Meta:
        model = BlogImage
        fields = ['id', 'image', 'alt_text']

class BlogSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'date', 'description', 'likes', 'images', 'comments', 'total_comments']

    def get_total_comments(self, obj):
        return obj.total_comments()
    


class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = ['id', 'author', 'text', 'created_at', 'is_demo_request', 'demo_type']
        read_only_fields = ['created_at', 'is_demo_request', 'demo_type']  # Set automatically

class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)  # Returns full URL

    class Meta:
        model = ProjectImage
        fields = ['id', 'image', 'alt_text']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    comments = ProjectCommentSerializer(many=True, read_only=True)
    total_comments = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'title', 'date', 'description', 'likes', 'images', 'comments', 'total_comments']

    def get_total_comments(self, obj):
        return obj.total_comments()