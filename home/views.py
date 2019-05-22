from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Stone
# Create your views here.

class Homepageview(TemplateView):
    template_name='home.html'

def stone_detail(request, pk):
    stone = Stone.objects.get(pk=pk)
    context ={
        'stone':stone
    }
    return render(request, 'stone_detail.html', context)

class Aboutpageview(TemplateView):
    template_name = 'about.html'

def stone_index(request):
    stones=Stone.objects.all()
    context = {
        'stones':stones
    }
    return render(request, 'stones.html',context)


