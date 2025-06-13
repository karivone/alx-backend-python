
from django.urls import path
from .views import delete_user
from .views import unread_messages_view

urlpatterns = [
    path('unread/', unread_messages_view, name='unread_messages'),
]
urlpatterns = [
    path('delete-account/', delete_user, name='delete_user'),
]
