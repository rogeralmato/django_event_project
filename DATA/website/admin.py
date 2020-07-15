from django.contrib import admin
from .models import Event, EventState, Profile, EventSubscription

admin.site.register(Event)
admin.site.register(EventState)
admin.site.register(Profile)
admin.site.register(EventSubscription)