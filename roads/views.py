from django.shortcuts import render
from .models import Road, LandPlot


def index(request):
    return render(request, 'roads/index.html')


def roads(request):
    context = {"roads": Road.objects.all()}
    return render(request, 'roads/roads.html', context)


def land_plots(request):
    context = {"land_plots": LandPlot.objects.all()}
    return render(request, 'roads/land_plots.html', context)