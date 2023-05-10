import json

from django.shortcuts import render
from kafka import KafkaConsumer
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from io import BytesIO
import base64

topic = 'report_dashboard'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


# Topic: report_data Message: {"msg_type": "detection", "location": 66, "event_type": "fire", "severity": "red"}
# Report Data Variabled
def init_data_vars():
    report_data_detections_total = report_data_detections_vehical = report_data_detections_person = report_data_detections_fire = report_data_detections_animal = 0
    report_data_event_total = report_data_event_up = report_data_event_down = report_data_event_offline = report_data_event_low = 0
    timestamp = datetime.now() 
    fifteen_minutes_ago = current_time - timedelta(minutes=15)


def init_tables():
    sec_table = [
        [ timestamp, report_data_detections_total, report_data_detections_vehical, report_data_detections_person,  report_data_detections_fire, report_data_detections_animal, ] 
    ]
    unit_table = [
        [ timestamp, report_data_event_total, report_data_event_up, report_data_event_down, report_data_event_offline, report_data_event_low ]
    ]

def update_tables():
    sec_table += [
        [ timestamp, report_data_detections_total, report_data_detections_vehical, report_data_detections_person,  report_data_detections_fire, report_data_detections_animal, ] 
    ]
    unit_table += [
        [ timestamp, report_data_event_total, report_data_event_up, report_data_event_down, report_data_event_offline, report_data_event_low ]
    ]

#set the data up
init_data_vars()
init_tables()

# Iterate over the Kafka messages and update the event totals and timeline
for message in consumer:
    msg_json = msg.value

    # Add data to report_data_vars
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
    update_tables()
    init_data_vars()

    if timestamp < fifteen_minutes_ago:
        update_tables()
    else
        update_tables()
        render_graph()
        init_data_vars()


    
def render_graph():
    # Create a bar chart of the event totals
    fig, ax = plt.subplots()
    ax.bar(event_totals.keys(), event_totals.values())
    ax.set_title('Event Totals')
    ax.set_xlabel('Event Type')
    ax.set_ylabel('Total Events')

    # Encode the chart as a base64 string
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    chart_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # Render the dashboard template with the event totals and chart
    return render(request, 'dashboard.html', {
        'event_totals': event_totals,
        'chart_image': chart_image,
        'event_timeline': event_timeline
    })

#######################


    




# print(f"Report Component Reading: {topic} ")
# for msg in consumer:
#     msg_json = msg.value

#     # Add data to report_data
#     if(msg_json['msg_type'] == 'detection'):
#         report_data_detections_total = report_data_detections_total +1
#         if(msg_json['event_type'] == 'vehicle'):
#             report_data_detections_vehical +=1
#         elif(msg_json['event_type'] == "person"):
#             report_data_detections_person += 1
#         elif(msg_json['event_type'] == 'animal' ):
#             report_data_detections_animal += 1 
#         else:
#             report_data_detections_fire += 1 
#     elif(msg_json['msg_type'] == 'event'):
#         report_data_event_total = report_data_event_total +1 
#         if(msg_json['state'] == 'up'):
#            report_data_event_up += 1
#         elif(msg_json['state'] == 'down'):
#             report_data_event_down += 1
#         elif(msg_json['state'] == 'off-line'):
#             report_data_event_offline += 1
#         else:
#             report_data_event_low += 1

    


#     render_report()

    

