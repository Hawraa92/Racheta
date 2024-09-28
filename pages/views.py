from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'  # مسار صفحة الـ home

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'  # مسار صفحة الـ about
