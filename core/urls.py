# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.equities, name='equities'), # Home page route
    path('about/', views.about, name='about'),
    path('predictor/', views.predictor, name='predictor'),
]