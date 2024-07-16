# kafka-cpu-consume
Kafka Quick Start Guide

This guide provides step-by-step instructions to quickly set up and run Apache Kafka on your local machine for development and testing purposes.
1. Start Zookeeper

bash

./zookeeper-server-start.sh ../config/zookeeper.properties

2. Start Kafka Server

bash

./kafka-server-start.sh ../config/server.properties

3. Create a Kafka Topic

bash

./kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 4

4. Produce Messages to the Topic

bash

./kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic

5. Consume Messages from the Topic

bash

./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning

Conclusion

Follow these steps to quickly set up and start using Kafka on your local machine. Adjust configurations and explore further based on your specific use cases and requirements.
