from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Chat(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sent_at']

    def __str__(self):
        return f'{self.user.username} - {self.sent_at}'

