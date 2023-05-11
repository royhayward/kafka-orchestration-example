import json
from lib.producer import *

# This functions handles the first level of logic and routes information
# sending the information to the desired path
def logic_function(msg_type, msg_str):
    
    if msg_type == "event":
        unit_event_workflow(msg_str)
    elif msg_type == "detection":
        security_event_workflow(msg_str)
    elif msg_type == "report":
        report_event_workflow(msg_str)

   
    return True

# This function handles the workflow what happens with a security event

def security_event_workflow(msg_str):
    message_sender('sec_command', msg_str)
    message_sender('notification_command', msg_str)
    message_sender('report_data', msg_str)

    # message_sender('report_dashboard', msg_str)

# this function handles the logic of what happens with a unit event
def unit_event_workflow(msg_str):
    message_sender('unit_command', msg_str)
    message_sender('report_data', msg_str)

    # message_sender('report_dashboard', msg_str)

# this function handles the logic o what happens with a report event
def report_event_workflow(msg_str):
    message_sender('report_data', msg_str)

    # message_sender('report_dashboard', msg_str)

# this function handles the logic of what happens with a nogification event
def notification_event_workflow(msg_str):
    message_sender('notification_command', msg_str)
    message_sender('report_data', msg_str)
    message_sender('report_dashboard', msg_str)

