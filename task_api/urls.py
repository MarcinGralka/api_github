from django.urls import path
from . import views

urlpatterns = [
    # Providing endpoint
    path('search/', views.search_repositories, name='search_repositories')
]