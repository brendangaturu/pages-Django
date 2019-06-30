from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    """A Home page for the pages webapp"""
    template_name = 'home.html'


class AboutPageView(TemplateView):
    """about page for the pages webapp"""
    template_name = 'about.html'
