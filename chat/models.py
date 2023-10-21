from django.db import models



class Message(models.Model):
    content = models.TextField()
    response = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'chat'