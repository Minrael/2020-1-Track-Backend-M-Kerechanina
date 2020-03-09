from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseNotAllowed
from django.views.decorators.http import require_GET, require_POST
from chats.models import Chat, Member, Message
from chats.forms import ChatForm, MessageForm
from datetime import datetime


def index_page(request):
    return render(request, 'index_page.html')

@require_GET
def chat_list(request):
    chats = Chat.objects.filter(is_group_chat = False).values(
        'id', 'topic'
    )
    return JsonResponse({'data': list(chats)})

@require_GET
def chat_page(request, chat_id):
    if (request.method == 'GET'):
        return JsonResponse({'chat': {
            'id': chat_id,
            'topic': 'name',
            'messages': ['Hi!', "What' up?"]
        }})
    else:
        return HttpResponseNotAllowed(['GET'])

def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id = chat_id)
    return JsonResponse({
        'data':{'id': chat_id, 'topic': chat.topic}
    })

@require_GET
def user_chat_list(request, user_id):
        chat_list = {}
        member = Member.objects.filter(user_id=user_id)
        for m in member:
            chat = Chat.objects.filter(id = m['chat_id'] )
            chat_list.append(chat)
        return JsonResponse(chat_list)

def create_pers_chat(request):
    form = ChatForm(request.POST)
    if form.is_valid():
        chat = Chat()
        chat.is_group_chat = False
        chat.topic = form.topic
        chat.last_messege = ''
        chat.save()
    return JsonResponse({'new chat': chat.topic})


def search_user(request):
    pass

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.added_at = datetime.now()
            message.save()
            return JsonResponse({'msg':'message saved'})
        return JsonResponse({'errors':form.errors}, status=400)
    else:
        form = MessageForm()
    return render(request, 'send_message.html',{'form': form})


@require_GET
def chat_message_list(request):
    messages = Message.objects.filter(chat_id = 1).values('content')
    return JsonResponse({'messages':list(messages)})

def read_message(request):
    pass
