from django.urls import path
from .views import *

urlpatterns = [
    path('', sign_up_by_django, name='sign_up_by_django'),
    path('django_sign_up', sign_up_by_html, name='sign_up_by_html' ),
]