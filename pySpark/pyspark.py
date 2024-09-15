
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("First pyspark code") \
    .getOrCreate()

data = [
    ("Alice", 25, "New York"),
    ("Bob", 30, "London"),
    ("Charlie", 22, "Paris"),
    ("David", 35, "Tokyo")
]

columns = ["name", "age", "city"]
df = spark.createDataFrame(data, columns)
df.show()
spark.stop()
