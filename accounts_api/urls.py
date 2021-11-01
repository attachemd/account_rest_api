from django.urls import path

from accounts_api import views


urlpatterns = [
    path('hello-apiview/', views.HelloApiView.as_view()),
]
