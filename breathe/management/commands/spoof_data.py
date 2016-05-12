from django.core.management.base import BaseCommand, CommandError
from breathe.models import Sensor
from breathe.utils import generate_data
import datetime
import requests
import json

class Command(BaseCommand):
    help = 'Generated Data'

    def handle(self, *args, **options):
        aws_uri = "https://search-sensor-cloud-3kouvsbrr2mcoorths4t4enioa.us-west-2.es.amazonaws.com/sensor_data/sensor/"
        from breathe.models import Sensor
        all_sensors = Sensor.objects.all()
        for sensor in all_sensors:
            if sensor.on_status:
                json_data = json.dumps({"sensor_id" : sensor.id , 'timestamp' : datetime.datetime.utcnow().isoformat(), 'data' : generate_data()})
                response_obj2 = requests.post(aws_uri, data=json_data)
                print json_data
                print response_obj2.text
