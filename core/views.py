from django.shortcuts import render
# We used this to server a simple HttpResponse to our site.
# from django.http import HttpResponse
# Now we are going to use something to render HTMl instead
from django.views.generic import TemplateView
# Create your views here.

"""
def TestView(request, **kwargs):
    return HttpResponse("Hello World")
"""
class SplashView(TemplateView):
    template_name = 'index.html'
