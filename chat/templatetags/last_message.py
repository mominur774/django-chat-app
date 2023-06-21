from django import template
from chat.models import Room, Message

register = template.Library()

@register.filter(name='last_message')
def get_last_message(user, recipient):
    room = Room.objects.filter(users=user).filter(users=recipient)
    msg = Message.objects.filter(room=room.first())
    if msg.exists():
        return msg.last().message
    else:
        return "Last message goes here"