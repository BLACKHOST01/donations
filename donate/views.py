from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import (TemplateView)


class home_View(TemplateView):
    template_name = "base.html"
