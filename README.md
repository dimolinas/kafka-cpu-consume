Here's the rich text formatted into markdown suitable for a README file:

---

### Running Zookeeper and Kafka Servers

1. **Start Zookeeper:**

   Run your `zookeeper-server-start.sh` file and pass `zookeeper.properties` as an argument:

   ```bash
   ./zookeeper-server-start.sh ../config/zookeeper.properties
   ```

   Your Zookeeper server has started. Now proceed to start Kafka.

2. **Start Kafka:**

   To start Kafka server, run `kafka-server-start.sh` with `server.properties` as the argument:

   ```bash
   ./kafka-server-start.sh ../config/server.properties
   ```

   Kafka server is now up and running.

3. **Create a Kafka Topic:**

   Now that both Zookeeper and Kafka servers are running, create a new topic using:

   ```bash
   ./kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 4
   ```

   - `--create`: Indicates creation of a new topic.
   - `--topic test-topic`: Specifies the topic name.
   - `--bootstrap-server localhost:9092`: Specifies Kafka server's address.
   - `--replication-factor 1`: Number of replication factors.
   - `--partitions 4`: Number of partitions for the topic.

### Creating Producers and Consumers

**Create a Producer:**

To produce/send data to `test-topic`, use:

```bash
./kafka-console-producer.sh --broker-list localhost:9092 --topic test-topic
```

- `--broker-list localhost:9092`: Specifies Kafka broker's address.
- `--topic test-topic`: Specifies the topic name.

**Create a Consumer:**

Open a new terminal and change directory to Kafka's bin:

```bash
cd usercode/kafka/bin
```

Then create a consumer that reads messages from `test-topic`:

```bash
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-topic --from-beginning
```

- `--bootstrap-server localhost:9092`: Specifies Kafka server's address.
- `--topic test-topic`: Specifies the topic name.
- `--from-beginning`: Starts consuming from the beginning of the topic.

---

This README provides instructions for setting up Zookeeper and Kafka servers, creating Kafka topics, and managing producers and consumers via command line tools. Adjust paths and configurations based on your environment setup.
