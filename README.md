Orchestrated Microservices
==========================

This project creates several easy to read microservices in Python. It also uses a Kafka message broker as the common message bus. To implement this resource, check out this repository. https://github.com/wurstmeister/kafka-docker

Before running the examples, change the docker-compose-expose.yml "KAFKA_CREATE_TOPICS" key to look like this:
      KAFKA_CREATE_TOPICS: "message_stream:1:1,sec_command:1:1,unit_command:1:1,notification_command:1:1,report_data:1:1,third_party:1:1"

Then launch docker compose.

To run these example python scripts you will need to have python installed. 

Example 1
=========

This example case has three microservices and the Orchestrator. The microservices workflow has these steps:
1. Security Detection is produced.
2. Command is sent to the Security Service
3. Command is sent to the Notification Service.

Example 2
=========
This example modifies Example 1 in progress. 
The workflow is modified to add a Reporting Service.
Steps:
1. Launch the reporting service. 
2. Modify the Orchestrator workflow logic and uncomment out the reporting service line from the security workflow.
3. Stop the Orchestrator
4. Start the Orchestrator

Note: The original three services didn't have to change to accomidate the new service. Stoping and Starting the Orchestrator didn't impact the operations of these services as well. The only impact was a slight delay in the messages produced during this product monifications.

Example 3
=========
This example modifies the previous examples.
A new workflow for Unit Events is added.
This will require a new service to produce the Unit Event messages.
This will require a new workflow in the Orchestrator logic. 
This will require some new features in the Reporting Service.
No other services are impacted or need to be aware of this change.
Step:
1. Launch the Unit Event producer
2. Modify the Reporting Service and uncomment out the Unit Event section.
3. Modify the Orchestrator workflow logic.
4. Stop the Orchestrator
5. Start the orchestrator

Note, The messages from the Unit Event producer were processed as soon as the Orchestrator started looking for them. 
The security workflow and services were not impacted outside of the restart of the orchestrator. 

Also note, we could segment the orchestration into two Orchestrator services to remove the impact of the restart is needed. This is a recomended best practice if systems become more complex or have workflows with independent SLAs.

