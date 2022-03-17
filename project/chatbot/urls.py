"""chatbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from urllib import response
from django.contrib import admin
from django.urls import path

def response (request, slug=None):
    return HttpResponse("<h1>Ttile</h1>")

from backend import views as backend_views
from frontend import views as frontend_views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path("",frontend_views.frontend),
    path("sever/", backend_views.backend), #from which url do we want the function to run 
    path("server/get_chat_response",backend_views.get_chat_response),
]
