from time import sleep
from json import dumps
from lib.producer import *
import random

command_list = ['new_order','activate_unit','deactivate_unit','relocate_unit','bill_units']

for j in range(9999):
    command = random.choice (command_list)
    data = {'command':command,'unit': j}
    # if command == 'new_order':
    #     data = {'command':command,'unit': j}

    # if command == 'activate_unit':
    #     data = {'unit': j}


    # if command == 'deactivate_unit':
    #     data = {'unit': j}

    # if command == 'reloacate_unit':
    #     data = {'unit': j}

    # if command == 'bill_units':
    #     data = {'unit': j}

        
    print(command, j)
   message_sender('orchastrator_topic', value=data)
    sleep(0.5)