from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseNotAllowed


def index_page(request):
    return render(request, 'index_page.html')

def chat_list(request):
    if (request.method == 'GET'):
        return JsonResponse({'test': 'App'})
    else:
        return HttpResponseNotAllowed(['GET'])

def chat_page(request, chat_id):
    if (request.method == 'GET'):
        return JsonResponse({'chat': {
            'id': chat_id,
            'topic': 'name',
            'messages': ['Hi!', "What' up?"]
        }})
    else:
        return HttpResponseNotAllowed(['GET'])

