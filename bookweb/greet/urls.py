from django.urls import path

from greet import views

urlpatterns = [
    path('', views.hello),
]