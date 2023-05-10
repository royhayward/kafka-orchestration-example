from kafka import KafkaConsumer
import json
from time import sleep
from logic.workflow import *

topic = 'message_stream'

consumer = KafkaConsumer(
    'message_stream',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
print(f"Orchestration Reading: {topic} ")
loop_count = 0
for msg in consumer:
    msg_json = msg.value
    print(f"{loop_count}")
    msg_type = msg_json['msg_type']
    msg_str = json.dumps(msg_json)
    logic_function(msg_type, msg_str)
    loop_count += 1
# print(f"Processed {loop_count} messages.")