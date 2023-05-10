import json
import random
import time
from lib.producer import *


while True:
    location = random.randint(1, 100)
    unit_id = "TDC" + str(random.randint(0, 999999)).zfill(6)
    state = random.choice(["up", "down", "off-line", "low-voltage"])
    volts = 24 if random.random() < 0.9 else 12 if random.random() < 0.05 else 6 if random.random() < 0.03 else 0

    message = {
        "msg_type": "event",
        "location": location,
        "unit_id": unit_id,
        "state": state,
        "volts": volts
    }

    message_str = json.dumps(message)
    print(message_str)
    message_sender('message_stream', message_str)

    time.sleep(30)