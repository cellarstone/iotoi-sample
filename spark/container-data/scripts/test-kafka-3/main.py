# Imports and running findspark
import findspark

findspark.init("/etc/spark")
import pyspark
from pyspark import RDD
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

# Spark context details
sc = SparkContext(appName="PythonSparkStreamingKafka")
ssc = StreamingContext(sc, 2)
# Creating Kafka direct stream
dks = KafkaUtils.createDirectStream(
    ssc,
    ["jsontest1"],
    {"metadata.broker.list": "192.168.0.9:9092"},
)
counts = dks.pprint()
# Starting Spark context
ssc.start()
ssc.awaitTermination()