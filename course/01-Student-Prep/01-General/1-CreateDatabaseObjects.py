# Databricks notebook source
# MAGIC %md
# MAGIC # What's in this exercise?
# MAGIC
# MAGIC 1) Create a student-specific database<BR>

# COMMAND ----------

# MAGIC %md ### 0. Select Serverless as compute
# MAGIC
# MAGIC Press the Connect dropdown in the upper left menu, and select Serverless
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1. Create the taxi_db database in Databricks
# MAGIC
# MAGIC Specific for the student

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 1.1. Create schemas (AKA databases)

# COMMAND ----------

from libs.dbname import dbname

# COMMAND ----------

catalog = "acme_transport_taxinyc"
revenue_db = dbname(cat=catalog, db="revenue")
#reveune_db = 'hallvards_kos'
print("New db name: " + revenue_db)
spark.sql(f"USE catalog {catalog}")
spark.sql(f"CREATE DATABASE IF NOT EXISTS {revenue_db}")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### 1.2. Validate

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG acme_transport_taxinyc;
# MAGIC SHOW DATABASES;

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG acme_transport_taxinyc;
# MAGIC use schema dev_hallvard_featgh81218bergen_4c6799ab_revenue;
# MAGIC --show schemas;
# MAGIC select * FROM acme_transpo;
# MAGIC --create table acme_transport_taxinyc.dev_hallvard_featgh81218 

# COMMAND ----------

# MAGIC %sql
# MAGIC --USE CATALOG acme_transport_taxinyc;
# MAGIC --use schema dev_hallvard_featgh81218bergen_4c6799ab_revenue;
# MAGIC --show schemas;
# MAGIC select * FROM acme_transport_taxinyc.dev_hallvard_featgh81218bergen_4c6799ab_revenue.acme_transpo;

# COMMAND ----------



# COMMAND ----------


