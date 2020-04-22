# SF-Crime-Statistics

## Project Overview:
In this project, we will use a real-world dataset, extracted from Kaggle, on San Francisco crime incidents, and we will provide statistical analyses of the data using Apache Spark Structured Streaming. We will create a Kafka server to produce data, and ingest data through Spark Structured Streaming.

## Environment Prerequisites:

1. Spark 2.4.3
2. Scala 2.11.x
3. Java 1.8.x
4. Kafka build with Scala 2.11.x
5. Python 3.6.x or 3.7.x

## How to run the project:

1. Run `./start.sh` to install project requirements. If you use **pip** rather than conda, then use `pip install -r requirements.txt`

2. Start **zookeeper server**: `/usr/bin/zookeeper-server-start config/zookeeper.properties`

3. Open a new terminal and start **kafka server**: `/usr/bin/kafka-server-start.sh config/server.properties`

4. Open a new terminal and run `python kafka_server.py`

5. Open a new terminal and start **kafka-consumer-console**: `/usr/bin/kafka-consumer-console --bootstrap-server localhost:9091 --topic service.calls --from-beginning`

6. Run **spark job**: `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py`

## Questions:
1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Kafka emits at the rate of 1/second and with the current sparkSession allowing maxOffsetsPerTrigger=200, 
changing property parameters will not make a noticeable difference of performace due to the size of the dataset.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Properties:
spark.sql.shuffle.partitions
spark.streaming.kafka.maxRatePerPartition
spark.default.parallelism

To determine if we have reached the optimal group of the above property values we will need to reach the largest possible processedRowsPerSecond.
