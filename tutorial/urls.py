from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('api/', views.TutorialApi.as_view()),
]
