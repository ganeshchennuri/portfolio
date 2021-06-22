from django.conf import settings
from django.urls import path
from .views import (
    blogs_list_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view,
)

app_name = 'blogapp'

urlpatterns = [
    # path('',BlogListView.as_view()),
    path('', blogs_list_view),
    path('<str:slug>/',blog_post_detail_view, name='detail'),
    path('<str:slug>/edit',blog_post_update_view, name='update'),
    path('<str:slug>/delete',blog_post_delete_view, name='delete'),
]

