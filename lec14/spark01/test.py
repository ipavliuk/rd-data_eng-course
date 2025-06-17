from pyspark.sql import SparkSession

spark = SparkSession.builder.master('local[3]').getOrCreate()

print(spark.version)