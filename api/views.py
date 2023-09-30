from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


# Create your views here.
@api_view(['GET'])
def messages(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def messages_by_chat(request, chat_id):
    try:
        chat = Chat.objects.get(id=chat_id)
    except:
        return Response({'error': 'Chat not Found'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        messages = chat.messages.all()
        serializer = MessageSerializerForHuman(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(chat=chat)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Error with posting the message"}, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
def chats(request):
    if request.method == 'GET':
        chat = Chat.objects.all()
        serializers = ChatSerializer(chat, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer