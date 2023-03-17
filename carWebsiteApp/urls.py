from django.urls import path
from . import views

# http://localhost:8000/carWebsiteApp/home/

app_name = "carWebsiteApp"

urlpatterns = [
    path("home/", views.home, name="carWebsiteApp-home"),
    path("bmw_history/", views.bmw_history, name="carWebsiteApp-bmw_history"),
    path("audi_history/", views.audi_history, name="carWebsiteApp-audi_history"),
    path("mercedes_history/", views.mercedes_history, name="carWebsiteApp-mercedes_history"),
    path("volkswagen_history/", views.volkswagen_history, name="carWebsiteApp-volkswagen_history"),
    path("edit_history_form/", views.edit_history_form, name="carWebsiteApp-edit_history_form"),
    path("calculate_loan_form/", views.calculate_loan_form, name="carWebsiteApp-calculate_loan_form"),
]
