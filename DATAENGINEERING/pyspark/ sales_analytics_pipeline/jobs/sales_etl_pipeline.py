"""
End-to-End Sales Analytics Pipeline
Author: Shaziya Sayed
Purpose: Demonstrate ETL + Aggregations + Window Functions
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    sum as spark_sum,
    avg,
    count,
    row_number,
    rank,
    dense_rank,
    lag,
    to_date,
    month,
)
from pyspark.sql.window import Window


def create_spark():
    return (
        SparkSession.builder
        .appName("Sales Analytics Pipeline")
        .getOrCreate()
    )


def load_data(spark):
    df = spark.read.csv(
        "../data/sales_data.csv",
        header=True,
        inferSchema=True
    )
    return df


def clean_data(df):
    df = df.dropDuplicates()
    df = df.withColumn("order_date", to_date(col("order_date")))
    df = df.fillna({"amount": 0})
    return df


# =========================================================
# GROUP BY AGGREGATIONS
# =========================================================
def customer_aggregation(df):
    return (
        df.groupBy("customer_id")
        .agg(
            spark_sum("amount").alias("total_spent"),
            avg("amount").alias("avg_spent"),
            count("*").alias("order_count")
        )
    )


# =========================================================
# ORDER BY EXAMPLES
# =========================================================
def top_customers(df):
    return df.orderBy(col("amount").desc())


# =========================================================
# WINDOW FUNCTIONS
# =========================================================
def window_metrics(df):

    # Window by customer
    customer_window = Window.partitionBy("customer_id").orderBy(col("order_date"))

    # Global window
    global_window = Window.orderBy(col("order_date"))

    df = df.withColumn(
        "running_total",
        spark_sum("amount").over(global_window)
    )

    df = df.withColumn(
        "customer_rank",
        dense_rank().over(
            Window.partitionBy("region").orderBy(col("amount").desc())
        )
    )

    df = df.withColumn(
        "prev_day_sales",
        lag("amount").over(customer_window)
    )

    df = df.withColumn(
        "row_num",
        row_number().over(customer_window)
    )

    return df


# =========================================================
# MAIN PIPELINE
# =========================================================
def main():

    spark = create_spark()

    df = load_data(spark)
    df = clean_data(df)

    print("=== Raw Data ===")
    df.show()

    print("=== Customer Aggregation ===")
    customer_aggregation(df).show()

    print("=== Top Transactions ===")
    top_customers(df).show()

    print("=== Window Metrics ===")
    window_metrics(df).show()

    spark.stop()


if __name__ == "__main__":
    main()
