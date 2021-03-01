#    Spark
from pyspark import SparkContext

#    Spark Streaming
from pyspark.streaming import StreamingContext

#    Kafka
from pyspark.streaming.kafka import KafkaUtils

#    json parsing
import json


sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")

ssc = StreamingContext(sc, 60)

kafkaStream = KafkaUtils.createStream(
    ssc, "192.168.0.9:9092", "spark-streaming", {"jsontest1": 1}
)

parsed = kafkaStream.map(lambda v: json.loads(v[1]))

print(parsed)


ssc.start()
ssc.awaitTermination()