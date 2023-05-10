from kafka import KafkaConsumer
import json

topic = 'sec_command'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print(f"Security Component Reading: {topic} ")
for msg in consumer:
    msg_json = msg.value

    print(f"Security Event Received!\n")
    print(f"Event detected at location {msg_json['location']}")
    print(f"A {msg_json['event_type']} has been detected.")
    if(msg_json["severity"] == "green"):
        print("Everything is fine.\nNo further action.")
    elif(msg_json["severity"] == "yellow"):
        print("Suspicious activity.\nPlease investigate further.")
    else:
        print("Serious violation!\nTake action immediately!")
    print("\n----------------------------------------------------\n\n")

