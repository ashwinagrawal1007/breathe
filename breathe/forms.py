from django.forms import ModelForm, Form
from django import forms
from .models import Sensor, Subscription


class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        fields = ['zipcode', 'public_flag']
        
class SubscribeSensorForm(Form):
    
    def __init__(self, *args, **kwargs):
        sensor_list = kwargs.pop('sensor_list')
        super(SubscribeSensorForm, self).__init__(*args, **kwargs)
        self.fields['sensor_id'] = forms.ChoiceField(choices=sensor_list, widget=forms.RadioSelect)
    