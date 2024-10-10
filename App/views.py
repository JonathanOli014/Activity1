from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = 'application/home.html'

class About(TemplateView):
    template_name = 'application/about.html'

class Schedule(TemplateView):
    template_name = 'application/schedule.html'

class Portfolio(TemplateView):
    template_name = 'application/portfolio.html'

