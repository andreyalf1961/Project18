from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', index),
    path('index/', TemplateView.as_view(template_name='second_task/class_template.html')),
]


