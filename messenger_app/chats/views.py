from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404, HttpResponseNotAllowed
from django.views.decorators.http import require_GET, require_POST
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from chats.models import Chat, Member, Message
from chats.forms import ChatForm, MessageForm
from user.forms import UserForm
from user.models import User
from django.utils import timezone


def item_name(name_for_cache):
  def get_my_item(function):
    def wrapper( *args, **kwargs):
      rv = cache.get(name_for_cache)
      if rv is None:
        rv = function(*args, **kwargs)
        cache.set(name_for_cache, rv, timeout=5*60)
      print(rv)
      #import ipdb
      #ipdb.set_trace(s)
      return rv
    return wrapper
  return get_my_item


def index_page(request):
    return render(request, 'index_page.html')

@require_GET
def chat_list(request):
    chats = Chat.objects.filter(is_group_chat = False).values(
        'id', 'topic'
    )
    return JsonResponse({'data': list(chats)})

'''
def chat_page(request, chat_id):
    if (request.method == 'GET'):
        return JsonResponse({'chat': {
            'id': chat_id,
            'topic': 'name',
            'messages': ['Hi!', "What' up?"]
        }})
    else:
        return HttpResponseNotAllowed(['GET'])
'''

@require_GET
def chat_page(request, chat_id):
    chat = Chat.objects.filter(id = chat_id).values(
        'id', 'topic'
    ).first()
    return JsonResponse({
        'data':{'chat': chat}
    })


@require_GET
def user_chat_list(request, user_id):
        chat_list = {}
        member = Member.objects.filter(user_id=user_id)
        for m in member:
            chat = Chat.objects.filter(id = m.chat_id).first()
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

@require_GET
def search_user(request):
    user = User.objects.all().values('username').first()
    return JsonResponse({'user': user})


def send_message_with_html(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.added_at = timezone.now()
            message.user = User.objects.filter(id = 1).first()
            message.chat = Chat.objects.filter(id = 1).first()
            message.save()
            #message = Message.objects.create(
            #    content = form.content,
            #    user = form.user,
            #    chat = form.chat,
            #   added_at = timezone.now())
            return JsonResponse({'msg':'message saved'})
        return JsonResponse({'errors':form.errors}, status=400)
    else:
        form = MessageForm()
    return render(request, 'send_message_with_html.html',{'form': form})


@require_POST
def send_message(request):
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.added_at = timezone.now()
            message.user = User.objects.filter(id = request.POST['user']).first()
            message.chat = Chat.objects.filter(id = request.POST['chat']).first()
            message.save()
            return JsonResponse({'msg':'message saved'})
        return JsonResponse({'errors': form.errors}, status=400)

@require_GET
#@item_name('messages')
#@cache_page(60*15)
def chat_message_list(request):
    #print(request.GET)
    messages = Message.objects.all().values('content')
    return JsonResponse({'messages':list(messages)})

def read_message(request):
    pass
