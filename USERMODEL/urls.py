from django.urls import path
from . import views
from .views import *

app_name="USERMODEL"

urlpatterns = [
    path('', Home, name='Home')
]