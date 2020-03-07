from django.shortcuts import render

from django.http import JsonResponse

def profile_user(request):
    if (request.method == 'GET'):
        return JsonResponse({'users': 'user1'})

def contacts(request):
    if (request.method == 'GET'):
        return JsonResponse({'users': 'list'})
