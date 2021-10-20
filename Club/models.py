from django.db import models
import uuid
from datetime import date

# Create your models here.
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name= models.CharField(max_length=100)
    desc=models.TextField(max_length=200)
    date=models.DateField(default= date.today())


class JoinedEv(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    s_id=models.IntegerField()
    e_id=models.UUIDField()
    ename=models.CharField(max_length=100)
    edate=models.DateField(default=None)