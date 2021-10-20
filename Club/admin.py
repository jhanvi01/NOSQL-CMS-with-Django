from Club.models import Event
from django.contrib import admin
from .models import Event, JoinedEv
# Register your models here.

admin.site.register(Event)
admin.site.register(JoinedEv)

