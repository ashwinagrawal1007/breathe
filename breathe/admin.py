
from django.contrib import admin


from .models import Sensor, Subscription

admin.site.register(Sensor)
admin.site.register(Subscription)