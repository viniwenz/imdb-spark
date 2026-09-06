from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("imdb_spark") \
    .getOrCreate()

df_titles = spark.read.csv(
    "title_basics.tsv", header=True, inferSchema=True, sep="\t", nullValue="\\N"
)

df_ratings = spark.read.csv(
    "title_ratings.tsv", header=True, inferSchema=True, sep="\t", nullValue="\\N"
)

df = df_titles.join(df_ratings, on="tconst", how="inner")

df.printSchema()
df.show(5)