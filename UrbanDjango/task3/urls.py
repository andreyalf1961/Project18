from django.urls import path
from .views import *

urlpatterns = [
    path('', platform),
    path('games/', shop),
    path('cart/', cart),
]
