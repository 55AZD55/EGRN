from django.urls import path
from . import views


urlpatterns = [
    path('catalog/', views.index, name='index'),
    path('roads_base/', views.roads, name='roads'),
    path('land_plots/', views.land_plots, name='lands'),
    path('search_road/', views.search_road, name='search_road')
]
