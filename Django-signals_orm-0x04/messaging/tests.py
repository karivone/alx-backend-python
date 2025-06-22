from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class NotificationSignalTestCase(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='alice', password='testpass')
        self.receiver = User.objects.create_user(username='bob', password='testpass')

    def test_notification_created_on_message(self):
        Message.objects.create(sender=self.sender, receiver=self.receiver, content='Hello Bob!')
        notification = Notification.objects.filter(user=self.receiver).first()
        self.assertIsNotNone(notification)
        self.assertEqual(notification.message.content, 'Hello Bob!')

# Create your tests here.
