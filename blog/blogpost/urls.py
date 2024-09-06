from django.urls import path
from .views import home, post_list, post_create, post_detail, delete_comment, post_update, post_delete

app_name = 'blogpost'

urlpatterns = [
    path('', home, name='home'),
    path('post_list/',post_list, name='post_list'),
    path('post_create/', post_create, name='post_create'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post_update/<int:post_id>', post_update, name='post_update'),
    path('post/<int:post_id>/delete', post_delete, name='post_delete'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
