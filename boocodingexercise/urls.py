from django.urls import path, re_path
from . import views

app_name = "boocodingexercise"

urlpatterns = [
    path('user/create', views.create_profile_api, name='create_profile_api'),
    path('user/<int:id>', views.get_profile_api, name='get_profile_api'),
    path('post/comment', views.create_comment_api, name='create_comment_api'),
    path('get/comment/<int:id>', views.get_comment_api, name='get_comment_api'),
    path('get/comments', views.get_all_comments_api, name='get_all_comments_api'),
    path('comment/<int:id>/like', views.like_comment, name='like_comment'),
    path('comment/<int:id>/dislike', views.dislike_comment, name='dislike_comment'),
]
