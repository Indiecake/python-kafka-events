from kafka import KafkaConsumer, KafkaProducer
import json
from concurrent.futures import ThreadPoolExecutor
TOPIC_NAME = "NOTIFICATION"
KAFKA_SERVER = "localhost:9092"
EMAIL_TOPIC = "EMAIL"
consumer = KafkaConsumer(
    TOPIC_NAME,
    # to deserialize kafka.producer.object into dict
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)

producer = KafkaProducer(
	bootstrap_servers = KAFKA_SERVER,
	api_version = (0, 11, 15)
)
def sendNotification(data):
    if(data["email"]):
        user_data = json.dumps(data["user"])
        producer.send(EMAIL_TOPIC, str.encode(user_data))
        producer.flush()
    else:
        print("There is not notification channel stablish")
    
for notification in consumer:
	notification_data = notification.value
	sendNotification(notification_data)
