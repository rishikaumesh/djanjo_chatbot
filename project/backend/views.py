from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def backend(request, slug=None):
    return HttpResponse("<p>Hello from the backend-side</p>")

import json
from .bot import bot_response #importing a function from a different file. 

def get_chat_response(request, slug=None):
    data = request.GET
    message=data.get("message")
    print(message)

    response= {
        "message":bot_response(message)
    }

    return HttpResponse(json.dumps(response))

    