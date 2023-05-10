from lib.producer import *
import json
import random
import time


while True:
    # Generate random values
    location = random.randint(1, 100)
    event_type = random.choice(["vehicle", "person", "animal", "fire"])
    severity = random.choice(["red", "yellow", "green"])

    # Create message dictionary
    msg = {"msg_type": "detection", "location": location, "event_type": event_type, "severity": severity}
    msg_str = json.dumps(msg)
    print(msg_str)

    # Send message to topic
    message_sender('message_stream', msg_str)

    time.sleep(30)