from django.db import models
from datetime import datetime
from django.utils import timezone

# User class for built-in authentication module
from django.contrib.auth.models import User


class Item(models.Model):
    text = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    #mytime = datetime.date.today()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return str(self.text) 
