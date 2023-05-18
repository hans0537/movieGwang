from django.urls import path
from . import views

urlpatterns = [
    # 자유게시판
    path('', views.articles_list_create),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/create_all/', views.comment_create_all, name='create_comment'),
    path('<int:article_pk>/like/', views.like, name='like'),
]
