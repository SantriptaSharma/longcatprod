from django.urls import path, include
from . import views

app_name = "linkextender"
urlpatterns = [
    path('', views.homepage, name = 'index'),
    path('create', views.extendlink, name = 'create'),
    path('<slug:longlink>', views.longlink, name = "long link head"),
    path('<slug:longlink>/<int:segno>', views.longlinkseg, name = "long link segment")
]
