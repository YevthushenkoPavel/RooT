from django.urls import path
from user_messages.views import messages_view, error, message_processed


urlpatterns = [
    path('view/', messages_view),
    path('error/', error),
    path('view/<message>', message_processed),
]
