from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from chat.models import Message, Room
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required(login_url='/accounts/login/')
def chat(request, room_name):
    user = get_object_or_404(User, username=room_name)
    room = Room.objects.filter(users=user.pk).filter(users=request.user.pk)
    chats = []
    if room.exists():
        chats = Message.objects.filter(room=room.first()).order_by('timestamp')
    
    context = {
        'chats': chats,
        'room_name': room_name,
        'users': User.objects.exclude(username=request.user)
    }

    return render(request, 'chat/chat.html', context)