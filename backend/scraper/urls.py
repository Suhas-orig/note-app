# scraper/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scraper_view, name='scrape-news'),
     path('summarize/', views.summarize_view, name='summarize-news'),
]
