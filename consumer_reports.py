from kafka import KafkaConsumer
import json

topic = 'report_data'

# Topic: report_data Message: {"msg_type": "detection", "location": 66, "event_type": "fire", "severity": "red"}

# Report Data Variabled
report_data_detections_total = 0
report_data_detections_vehical = 0
report_data_detections_person = 0
report_data_detections_fire = 0
report_data_detections_animal = 0
report_data_event_total = 0
report_data_event_up = 0
report_data_event_down = 0
report_data_event_offline = 0
report_data_event_low = 0

def render_report():
    print("----------------------\n")
    print(f"Security Detections: {report_data_detections_total}")
    print(f"Vehicals: {report_data_detections_vehical}")
    print(f"People: {report_data_detections_person}")
    print(f"Animals: {report_data_detections_animal}")
    print(f"Fires: {report_data_detections_fire}")
    
    print(f"Unit Events: {report_data_event_total}")
    print(f"Units Up: {report_data_event_up}")
    print(f"Units Down: {report_data_event_down}")
    print(f"Units Off-Line: {report_data_event_offline}")
    print(f"Units Low-Voltage: {report_data_event_low}")

    print("----------------------\n")


consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(f"Report Component Reading: {topic} ")
for msg in consumer:
    msg_json = msg.value

    # Add data to report_data
    if(msg_json['msg_type'] == 'detection'):
        report_data_detections_total = report_data_detections_total +1
        if(msg_json['event_type'] == 'vehicle'):
            report_data_detections_vehical +=1
        elif(msg_json['event_type'] == "person"):
            report_data_detections_person += 1
        elif(msg_json['event_type'] == 'animal' ):
            report_data_detections_animal += 1 
        else:
            report_data_detections_fire += 1 
    elif(msg_json['msg_type'] == 'event'):
        report_data_event_total = report_data_event_total +1 
        if(msg_json['state'] == 'up'):
           report_data_event_up += 1
        elif(msg_json['state'] == 'down'):
            report_data_event_down += 1
        elif(msg_json['state'] == 'off-line'):
            report_data_event_offline += 1
        else:
            report_data_event_low += 1

    


    render_report()

    

