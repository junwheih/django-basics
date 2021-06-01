from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

# from django.http import HttpResponse
# def homePageView(request):
#     return HttpResponse('home.html')