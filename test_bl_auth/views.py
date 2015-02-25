from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import requests


def get_id(request):
    return render(request, 'template.html')


def give_id(request):
    username = request.POST['username']
    ip = request.META['REMOTE_ADDR']
    
    url = 'http://auth.blockland.us/authQuery.php'
    payload = {'NAME': username, 'IP': ip}
    r = requests.post(url, data=payload)

    """context = RequestContext(request, {
        'name': request.POST
    })
    return render(request, 'result.html', context)"""

    if r.text[0] == 'Y':
        id = r.text[4:]
        return HttpResponse(content='Success! Your Blockland ID is ' + id.strip() + '!')
    else:
        return HttpResponse(content='Nope, try again.')