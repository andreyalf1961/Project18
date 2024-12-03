from django.urls import path
from .views import *

urlpatterns = [
    path('', platform),
    path('platform', platform),
    path('platform/games/', shop),
    path('platform/cart/', cart),
]
