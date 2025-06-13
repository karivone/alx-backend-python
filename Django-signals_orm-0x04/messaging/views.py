from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.db.models import Prefetch

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')  # Replace with your desired redirect
    else:
        return redirect('profile')  # Replace with your profile page or error page

def conversation_thread(user1, user2):
    base_messages = Message.objects.filter(
        sender=user1, receiver=user2, parent_message__isnull=True
    ).select_related('sender', 'receiver').prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
    )

    return base_messages
def get_message_thread(message):
    thread = []

    def collect_replies(msg):
        replies = msg.replies.select_related('sender').all()
        for reply in replies:
            thread.append(reply)
            collect_replies(reply)

    collect_replies(message)
    return thread

# Create your views here.
