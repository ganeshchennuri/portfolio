from django.db import models
from django.conf import settings
from django.db.models.deletion import SET_NULL

class SearchQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True,null=True,on_delete=SET_NULL)
    query = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
