from kafka import KafkaProducer

def message_sender(topic, msg):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
    print(f"Topic: {topic} Message: {msg}")  
    producer.send(topic, value=msg.encode())
    producer.flush()
    return True

