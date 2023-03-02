from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('html/', views.html),
    path('f_str/<str:str_value>', views.f_str),
    path('f_int/<int:int_value>', views.f_int),
    path('f_slug/<slug:slug_value>', views.f_slug),
    path('f_path/<path:path_value>', views.f_path),
    path('f_str_int_slug/<str:str_value>/<int:int_value>/<slug:slug_value>', views.f_str_int_slug),
]
