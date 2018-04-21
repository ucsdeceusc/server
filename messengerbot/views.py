from django.shortcuts import render
from django.http import HttpResponse
import os

from TokenManager import TokenManager
tm = TokenManager()
VERIFY_TOKEN = tm.get('MESSENGER_VERIFY_TOKEN')

def index(request):
    return HttpResponse('Front page of ECEUSC Messenger Bot should go here! Heroku 2....')

def webhook(request):
    if request.method == 'GET':
        verify_token = request.GET.get('hub.verify_token')
        
        if verify_token == VERIFY_TOKEN:
            hub_challenge = request.GET.get('hub.challenge')
            print(hub_challenge)
            return HttpResponse(hub_challenge)
        else:
            return HttpResponse('ERROR')
            
            
    return HttpResponse('Lol lets do this')

