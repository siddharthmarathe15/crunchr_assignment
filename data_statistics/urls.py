from django.urls import path
from . import views

urlpatterns = [
    path('location/', views.search_by_location),
    path('age/', views.search_by_age),
]
