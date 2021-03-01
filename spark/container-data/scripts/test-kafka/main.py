from pyspark.sql import SparkSession

appName = "Kafka Examples"
master = "spark://iotoi-spark-master:7077"

spark = SparkSession.builder.master(master).appName(appName).getOrCreate()

kafka_servers = "192.168.0.9:9092"

# df = spark \
#     .read \
#     .format("kafka") \
#     .option("kafka.bootstrap.servers", kafka_servers) \
#     .option("subscribe", "kontext-kafka") \
#     .load()

# df = df.withColumn('key_str', df['key'].cast('string').alias('key_str')).drop(
#     'key').withColumn('value_str', df['value'].cast('string').alias('key_str')).drop('value')
# df.show(5)

df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", kafka_servers)
    .option("subscribe", "jsontest1")
    .option("startingOffsets", "earliest")
    .load()
)

df.show(5)

df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)").writeStream.format(
    "kafka"
).option("kafka.bootstrap.servers", kafka_servers).option("topic", "jsontest2").start()

df.show(5)

spark.streams.awaitAnyTermination()
