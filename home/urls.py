from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = "home"),
    path('add_transaction/', add_transaction, name = "add_transaction")
]