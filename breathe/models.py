# coding: utf-8

from django.contrib.auth.models import User
from django.db import models
    
class Sensor(models.Model):
    owner = models.ForeignKey(User)
    zipcode = models.CharField(max_length=5)
    creation_date = models.DateTimeField(editable=False)
    public_flag = models.BooleanField(default=False)
    on_status = models.BooleanField(default=False)

    
    def __unicode__(self):
        return u'Sensor ' + unicode(self.id) + u' at  zipcode ' + unicode(self.zipcode)
    
class Subscription(models.Model):
    subscriber = models.ForeignKey(User)
    sensor = models.ForeignKey(Sensor)
    
    def __unicode__(self):
        return u'Sensor# ' + unicode(self.sensor.id) + u' - Subscriber# ' +  unicode(self.subscriber.username)
        

