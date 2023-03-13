from django.urls import path
from . import views

app_name = "websiteApp"
urlpatterns = [
    path("index/", views.index),
    path("", views.home),
    path("home/", views.home, name="websiteApp-home"),
    path("form/", views.form, name="websiteApp-form"),
    path("form_abc/", views.form_abc, name="websiteApp-form_abc"),
    path("store/", views.store, name="websiteApp-store"),
    path("store_result/", views.store_result, name="websiteApp-store_result"),
    # path("page_01/<path:queryStr>", views.page_01, name="websiteApp-page_01"),
]
