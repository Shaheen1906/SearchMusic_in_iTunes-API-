from django.urls import path
from searchapp.views import search

urlpatterns = [
    path('search/', search, name='search'),
]