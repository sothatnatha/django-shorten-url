from django.urls import path
from urlshort import views

urlpatterns = [
    path('', views.url_converter, name="url-converter")
]
