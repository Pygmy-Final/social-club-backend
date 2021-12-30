from django.db import models
# from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Message(models.Model):

    message = models.TextField()
    seen = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="sent_messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="received_messages", on_delete=models.CASCADE)

    class Meta:
        ordering = ("date_created",)