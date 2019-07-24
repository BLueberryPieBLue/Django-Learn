import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import Zone

from App.models import User


def login(request):
    user = request.POST.get('user')
    psd = request.POST.get('psd')
    try:
        per = User.objects.get(username=user)
        if per.password == psd:
            response = HttpResponse(json.dumps({'code': 1}))
        else:
            response = HttpResponse(json.dumps({'code': 2}))
    except:
        response = HttpResponse(json.dumps({'code': 0}))
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response



def register(request):
    print('register')
    try:
        per = User()
        user = request.POST.get('user')
        per.username = user
        psd = request.POST.get('psd')
        per.password = psd
        per.save()
        response = HttpResponse(json.dumps({'code': 1}))
    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({'code': 0}))
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response


def getregister(request):
    return render(request, 'register.html')


def getlogin(request):
    return render(request, 'login.html')


def getzone(request):
    return render(request, 'zone.html')


def sendZone(request):
    try:

        zone = Zone()
        zone.username = request.POST.get('username')
        zone.times = request.POST.get('times')
        zone.sendtime = request.POST.get('sendtime')
        zone.sendtxt = request.POST.get('sendtxt')
        zone.musicname = request.FILES.get('musicfile')
        zone.photoname = request.FILES.get('imgfile')
        zone.save()
        zonedict = {'code': '1', 'username': zone.username, 'times': zone.times,
                    'sendtime': zone.sendtime, 'sendtxt': zone.sendtxt,
                    'photoname': zone.photoname.url,}

        response = HttpResponse(json.dumps(zonedict))
    except Exception as e:
        print(e)
        response = HttpResponse(json.dumps({'code': '0'}))
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response


def getallzone(request):
    zones = Zone.objects.all()
    zoneList = []
    for zone in zones:
        zonedict = {'username': zone.username, 'times': zone.times,
                    'sendtime': zone.sendtime, 'sendtxt': zone.sendtxt,
                    'photoname': zone.photoname.url,}
        zoneList.append(zonedict)

    response = HttpResponse(json.dumps(zoneList))
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = '1000'
    response['Access-Control-Allow-Headers'] = '*'
    return response


def download(request):

    image_data = open(r'd:/django_test2/code.JPG', 'rb').read()
    return HttpResponse(image_data, content_type='image/JPG')