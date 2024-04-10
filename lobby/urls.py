from django.urls import path
from lobby import views


urlpatterns = [
    path('', views.home),
    path('login/', views.login, name="lobby_login"),
    path('games/', views.show_games)
]
