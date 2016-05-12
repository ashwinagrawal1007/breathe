from .models import Sensor, Subscription
import random
import requests
import json

def get_subscribable_sensors(user):
    subscribed_sensors_subscription = Subscription.objects.filter(subscriber=user).exclude(sensor__owner=user).select_related('sensor')
    subscribed_sensors = [sub.sensor for sub in subscribed_sensors_subscription]
    public_sensors = Sensor.objects.filter(public_flag=True).exclude(owner=user)
    return [sensor for sensor in public_sensors if sensor not in subscribed_sensors]
     
     
def generate_data():
    gas_dict = {}
    gas_dict['carbon monoxide'] = random.randint(35,150)
    gas_dict['nitrogen dioxide'] = random.randint(1,10)
    gas_dict['sulphur dioxide'] = random.randint(0,5)
    gas_dict['hydrogen sulfide'] = random.uniform(0.00011, 0.00033)
    return gas_dict
    
def get_chart_data_dates(sensor_id, from_date, to_date):
    sensor_search = "https://search-sensor-cloud-3kouvsbrr2mcoorths4t4enioa.us-west-2.es.amazonaws.com/sensor_data/sensor/_search"
    res = requests.post(sensor_search, data=json.dumps({
    "from" : 0, "size" : 1000,
    "query": {
        "filtered": {
            "query": {
                "match": { "sensor_id": "{}".format(sensor_id) }
                },
        "filter": {
            "range": { "timestamp": { "gte": "{}".format(from_date), "lte": "{}".format(to_date)}}
            }
        }
      }
    }))
    return process_data(res.json())
    


def get_chart_data(sensor_id):
    sensor_search = "https://search-sensor-cloud-3kouvsbrr2mcoorths4t4enioa.us-west-2.es.amazonaws.com/sensor_data/sensor/_search"
    res = requests.post(sensor_search, data=json.dumps({
    "from" : 0, "size" : 1000,
    "query": {
        "filtered": {
            "query": {
                "match": { "sensor_id": "{}".format(sensor_id) }
                },
        "filter": {
            "range": { "timestamp": { "gte": "now-15m" }}
            }
        }
      }
    }))
    return process_data(res.json())

def process_data(data):
    data =  data.get('hits', {'hits': {}}).get('hits', {})
    return [x.get('_source') for x in data]