from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="inicio"),
    path('user',views.user, name="user"),
    path('fastapi/',views.fastapi,name="fastapi"),
]
