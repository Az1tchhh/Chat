from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('name',)

class UserField(serializers.Field):
    def to_internal_value(self, data):
        return User.objects.get(username=data)

    def to_representation(self, value):
        return value.username

class DateModel(serializers.Field):
    # Fields and definitions here
    def to_internal_value(self, data):
        return Message.objects.get(sent_at=data)

    def to_representation(self, value):
        return value.strftime("%b %d, %Y %H:%M:%S")

class MessageSerializerForHuman(serializers.ModelSerializer):
    user = UserField()
    sent_at = DateModel()
    class Meta:
        model = Message
        fields = ('chat', 'user', 'text', 'sent_at')
        read_only_fields = ('id', 'sent_at')

class MessageSerializer(serializers.ModelSerializer):
    user = UserField()

    class Meta:
        model = Message
        fields = ('chat', 'user', 'text', 'sent_at')
        read_only_fields = ('id', 'sent_at')


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
