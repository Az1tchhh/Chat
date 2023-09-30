from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('chats/', views.chats, name="all-chats"),
    path('messages/', views.messages, name="all-messages"),
    path('chat/<int:chat_id>/messages/', views.messages_by_chat, name="messages-by-chat"),
    path('registration/', views.UserCreateView.as_view(), name="registration")
]