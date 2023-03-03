from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("category/<str:slug>/", views.college_category_landing, name = "category_landing"),
    path("college/<str:slug>/", views.college_landing, name = "college_landing"),
]