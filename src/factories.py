from databricks.connect import DatabricksSession
from pyspark.sql import SparkSession
from databricks.sdk.core import Config
from dotenv import dotenv_values

env_vars = dotenv_values(".env.local")


def create_databricks_client() -> SparkSession:
    config = Config(
        host=env_vars.get("DATABRICKS_HOST"),
        token=env_vars.get("DATABRICKS_TOKEN"),
        cluster_id=env_vars.get("DATABRICKS_CLUSTER_ID"),
    )
    return DatabricksSession.builder.sdkConfig(config).getOrCreate()
