from django.shortcuts import get_object_or_404, render, get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from .utils import get_subscribable_sensors, get_chart_data, get_chart_data_dates
import json
import datetime
from pprint import pprint
from .forms import SensorForm, SubscribeSensorForm
from .models import Sensor, Subscription

@login_required
def console(request):
    ctx = {}
    ctx['sensors'] = Sensor.objects.filter(owner=request.user)
    ctx['subscribed_sensors'] = Subscription.objects.filter(subscriber=request.user).exclude(sensor__owner=request.user).select_related('sensor')
    return render(request, 'console.html', ctx)
    
@login_required    
def add_sensor(request):
    if request.method == "POST":
        form = SensorForm(request.POST)
        if form.is_valid():
            sensor_obj = form.save(commit=False)
            sensor_obj.creation_date = datetime.datetime.utcnow().isoformat()
            sensor_obj.owner = request.user
            sensor_obj.save()
            messages.success(request, "Sensor added successfully")
            return redirect('console')
    else:
        form = SensorForm()
    return render(request, "add_sensor.html", {'form': form})
    
@login_required    
def delete_sensor(request, sensor_id=None):
    Sensor.objects.get(id=sensor_id).delete()
    messages.success(request, "Sensor deleted successfully")
    return redirect('console')

@login_required
def toggle_sensor(request, sensor_id=None):
    sensor = Sensor.objects.get(id=sensor_id)
    sensor.on_status = not sensor.on_status
    sensor.save()
    status = "off"
    if sensor.on_status:
        status = "on"
    give_message = "sensor successfully turned " + status
    messages.success(request, give_message)
    return redirect('console')

@login_required    
def subscribe_sensor(request):
    if request.method == "POST":
        form = SubscribeSensorForm(request.POST, sensor_list=[(sensor.pk,sensor) for sensor in get_subscribable_sensors(request.user)])
        if form.is_valid():
            new_sub = Subscription(subscriber=request.user, sensor_id=int(form.cleaned_data['sensor_id']))
            new_sub.save()
        messages.success(request, "Sensor subscribed successfully")
        return redirect('console')
    else:
        form = SubscribeSensorForm(sensor_list=[(sensor.pk,sensor) for sensor in get_subscribable_sensors(request.user)]) 
    return render(request, "subscribe_sensor.html", {'form': form})
    
@login_required
def unsubscribe_sensor(request, sensor_id=None):
    Subscription.objects.filter(subscriber=request.user).filter(sensor=sensor_id).delete()
    messages.success(request, "Sensor unsubscribed successfully")
    return redirect('console')

@login_required
def chart(request, sensor_id=None):
    if request.method == "POST":
        from_date = request.POST['from']
        to_date = request.POST['to']
        data = json.dumps(get_chart_data_dates(sensor_id, from_date, to_date), indent=2)
        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="sensor-data.json"'
        return response
        
        
    
    
    ctx={}
    ctx['sensor_id'] = sensor_id 
    return render(request, 'chart.html', ctx)
    
def chart_json(request):
    sensor_id = request.GET.get('sensor_id')
    data = get_chart_data(sensor_id)
    for entry in data:
        entry["timestamp"] = entry["timestamp"][11:19]
    return HttpResponse(json.dumps(data))
        
