from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Prefetch
from .models import Message

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')  # Replace with your desired redirect
    else:
        return redirect('profile')  # Replace with your profile page or error page

@login_required
def user_conversation_view(request):
    base_messages = Message.objects.filter(
        sender=request.user, parent_message__isnull=True
    ).select_related('sender', 'receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
    )
    return render(request, 'messaging/conversation.html', {'messages': base_messages})

def get_message_thread(message):
    thread = []

    def collect_replies(msg):
        replies = msg.replies.select_related('sender').all()
        for reply in replies:
            thread.append(reply)
            collect_replies(reply)

    collect_replies(message)
    return thread


def unread_messages_view(request):
    if not request.user.is_authenticated:
        return render(request, 'messaging/unauthorized.html')

    unread_msgs = Message.unread.unread_for_user(request.user)
    return render(request, 'messaging/unread_messages.html', {'unread_messages': unread_msgs})
# Create your views here.
