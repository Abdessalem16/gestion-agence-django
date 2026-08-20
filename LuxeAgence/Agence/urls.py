
from django.urls import path

from Agence import views
urlpatterns = [
    path('',views.home,name="home"),
    
]
