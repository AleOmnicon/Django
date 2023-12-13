from django.urls import path

from . import views

app_name = "data_display"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
