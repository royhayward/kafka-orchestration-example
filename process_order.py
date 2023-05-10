from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads
from time import sleep
import json

# this application will consume orders from the 'new_order' stream
consumer = KafkaConsumer(
    'new_order',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)
#this application will produce messages for activate_unit and relocation
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

#listen for and restpond to events in the new_order stream
for event in consumer:
    event_data = event.value

    # Do whatever you want
    print(event_data)
    json_data = json.loads(event_data)
    if(json_data["unit"]):
        print("Unit:" + json_data["unit"])
        activate_unit(json_data["unit"])
        # sleep(2)

#produce events to relocate a unit
def activate_unit(id):
    print("ID: "+id)
    data = {'id': id}
    producer.send('relocate', value=data)
    sleep(0.5)
    producer.send('activate_unit', value=data)
    sleep(0.5)


