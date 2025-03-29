from django.urls import path, include
from django.views.static import serve
from .views import BlogListView, LikeBlogView, AddCommentView, ProjectListView, LikeProjectView, AddProjectCommentView
urlpatterns = [
    path('api/blogs/', BlogListView.as_view(), name='blog-list'),
    path('api/blogs/<int:pk>/like/', LikeBlogView.as_view(), name='like-blog'),
    path('api/blogs/<int:pk>/comment/', AddCommentView.as_view(), name='add-comment'),

    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/like/', LikeProjectView.as_view(), name='like-project'),
    path('api/projects/<int:pk>/comment/', AddProjectCommentView.as_view(), name='add-comment'),
]
