from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def backend(request, slug=None):
    return HTTPResponse("<p>Hello from the backend-side</p>")