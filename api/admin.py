from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'sent_at')

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('name',)