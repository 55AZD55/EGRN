from django.shortcuts import render
from .models import Road, LandPlot
from django.db.models import Q


def index(request):
    return render(request, 'roads/index.html')


def roads(request):
    context = {"roads": Road.objects.all()}
    return render(request, 'roads/roads.html', context)


def land_plots(request):
    context = {"land_plots": LandPlot.objects.all()}
    return render(request, 'roads/land_plots.html', context)


def search_road(request):
    query = request.GET.get('q').capitalize()
    resault_q = Road.objects.filter(Q(ident_number__contains = query) | Q(name__contains = query))
    print(resault_q)
    resault = []
    if len(resault_q) == 0:
        resault.append('Ничего не найдено')
    else:
        resault_sort = sorted(((i.ident_number, i.name) for i in resault_q), key=lambda x: int(x[0].split('-')[1]))
        resault = (' '.join(i) for i in resault_sort)
    context = {"resault": resault}
    return render(request, 'roads/search_road_result.html', context)