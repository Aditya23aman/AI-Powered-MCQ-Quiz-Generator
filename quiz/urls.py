from django.urls import path

from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("test/", views.test, name="text"),
# ]

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('history', views.history, name="history"),
]