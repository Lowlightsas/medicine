from django.urls import path
from . import views

app_name = 'medic'

urlpatterns = [
    path('',views.base,name='base'),
    path('news/',views.news,name='news'),
]
