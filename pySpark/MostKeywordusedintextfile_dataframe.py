from pyspark.sql import SparkSession
from pyspark.sql.functions import split, explode, col, trim,lower

# Initialize SparkSession
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read the text file into a DataFrame (each line is a row in the DataFrame)
df = spark.read.text("interview_question_glue.txt")

# Load stopwords from another text file and collect them into a list
stopwords_df = spark.read.text("path_to_stopwords_file.txt")
stopwords = [row['value'].strip().lower() for row in stopwords_df.collect()]  # Remove spaces and convert to lowercase

# Perform word count, excluding empty spaces/words and stopwords
word_counts = (df.withColumn("words", explode(split(col("value"), "\\s+")))   
               .withColumn("words", lower(trim(col("words"))))                       
               .filter(col("words") != "")                                  
               .filter(~col("words").isin(stopwords))                         
               .groupBy("words")                                              
               .count()                                                       
               .orderBy(col("count").desc()))                                  


word_counts.show(truncate=False)


spark.stop()
