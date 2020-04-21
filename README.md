# SF-Crime-Statistics

### Questions:
1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

Kafka emits at the rate of 1/second and with the current sparkSession allowing maxOffsetsPerTrigger=200, 
changing property parameters will not make a noticeable difference of performace due to the size of the dataset.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?

Properties:
spark.sql.shuffle.partitions
spark.streaming.kafka.maxRatePerPartition
spark.default.parallelism

To determine if we have reached the optimal group of the above property values we will need to reach the largest possible processedRowsPerSecond.