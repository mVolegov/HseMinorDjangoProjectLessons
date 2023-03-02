from django.urls import path
from . import views

app_name = "renderApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("greet/<str:name>", views.greet, name="renderApp-greet"),
    path("page_01/<path:path_value>", views.page_01, name="renderApp-page_01"),
    path("page_02/<path:path_value>", views.page_02, name="renderApp-page_02"),
    path("page_03/<path:path_value>", views.page_03, name="ABC"),
]
