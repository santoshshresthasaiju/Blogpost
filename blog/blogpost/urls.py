from django.urls import path
from .views import home, post_list, post_create, post_detail, delete_comment

app_name = 'blogpost'

urlpatterns = [
    path('', home, name='home'),
    path('post_list/',post_list, name='post_list'),
    path('post_create/', post_create, name='post_create'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
