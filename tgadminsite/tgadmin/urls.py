from django.urls import path

from . import views

app_name = 'tgadmin'
urlpatterns = [
    path("", views.IndexView.as_view(), name="book"),
]