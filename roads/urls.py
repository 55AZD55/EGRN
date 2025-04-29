from django.urls import path
from . import views


urlpatterns = [
    path('roads/', views.index, name='index'),
    path('roads_base/', views.roads, name='roads'),
    path('land_plots/', views.land_plots, name='lands')
]
