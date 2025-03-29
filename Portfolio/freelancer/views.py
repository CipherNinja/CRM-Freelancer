from django.shortcuts import render
from .serializers import BlogSerializer, CommentSerializer, ProjectSerializer, ProjectCommentSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog, Project
# Create your views here.


# List all blogs
class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Like a blog
class LikeBlogView(APIView):
    def post(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog.likes += 1
            blog.save()
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)

# Add a comment to a blog
class AddCommentView(APIView):
    def post(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(blog=blog)  # Explicitly set the blog instance
                blog_serializer = BlogSerializer(blog)
                return Response(blog_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blog.DoesNotExist:
            return Response({"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)



# List all projects
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Like a project
class LikeProjectView(APIView):
    def post(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            project.likes += 1
            project.save()
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

# Add a comment to a project
class AddProjectCommentView(APIView):
    def post(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
            serializer = ProjectCommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(project=project)  # Explicitly set the project instance
                project_serializer = ProjectSerializer(project)
                return Response(project_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)