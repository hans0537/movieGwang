from django.urls import path
from . import views

urlpatterns = [
    path('findUsername/', views.findUsername),
    path('findPw/', views.findPw),

    path('getUser/', views.getUser),
    path('userdelete/',views.userdelete),
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
