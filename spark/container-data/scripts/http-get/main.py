"""
Copy the data from the test file into a new one.
"""

# Import what we need from PySpark
from pyspark import SparkContext, SparkConf
import requests

# Create a basic configuration
conf = SparkConf().setAppName("myTestCopyApp")

# Create a SparkContext using the configuration
sc = SparkContext(conf=conf)

URL = "https://randomuser.me/api/"
r = requests.get(url=URL)
data = r.json()

print(data)