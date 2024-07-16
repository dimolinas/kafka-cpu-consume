# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from kafka import KafkaProducer
import time
import psutil

topic_name = "test-topic"
kafka_server = 'localhost:9092'

producer = KafkaProducer(bootstrap_servers=kafka_server)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    for i in range(100000):
        time.sleep(0.2)
        cpu_percentage = int(psutil.cpu_percent())
        print("CPU: ", cpu_percentage)
        cpu_percentage_bytes = cpu_percentage.to_bytes(2, 'big')
        producer.send(topic_name, cpu_percentage_bytes)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

