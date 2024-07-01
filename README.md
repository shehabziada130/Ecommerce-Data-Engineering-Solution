# Ecommerce Data Engineering Solution

## Overview

This document introduces you to the data platform architecture of an ecommerce company leveraging a hybrid architecture with databases both on-premises and on the cloud.

## Tools and Technologies

- **OLTP Database**: MySQL
- **NoSQL Database**: MongoDB
- **Production Data Warehouse**: DB2 on Cloud
- **Staging Data Warehouse**: PostgreSQL
- **Big Data Platform**: Hadoop
- **Big Data Analytics Platform**: Spark
- **Business Intelligence Dashboard**: IBM Cognos Analytics
- **Data Pipelines**: Apache Airflow

## Architecture

The ecommerce company's online presence is primarily through its website, accessed by customers using various devices such as laptops, mobiles, and tablets.

### Databases

- **MongoDB**: Stores all the catalog data of the products.
- **MySQL**: Stores all the transactional data like inventory and sales.
- These databases drive the ecommerce company's webserver.

### Data Warehouses

- **Staging Data Warehouse**: Data is periodically extracted from MySQL and MongoDB and put into the staging data warehouse running on PostgreSQL.
- **Production Data Warehouse**: The production data warehouse is hosted on the cloud instance of IBM DB2 server. BI teams connect to this for operational dashboard creation.

### Big Data Platform

- **Hadoop**: Used as the big data platform where all data is collected for analytics purposes.
- **Spark**: Used to analyze the data on the Hadoop cluster.

### Business Intelligence

- **IBM Cognos Analytics**: Used to create dashboards connected to the IBM DB2 data warehouse.

### Data Pipelines

- **Apache Airflow**: ETL pipelines are used to move data between OLTP, NoSQL, and the data warehouse, running on Apache Airflow.

## Process

1. **Data Collection**: Product catalog data is stored in MongoDB, and transactional data is stored in MySQL.
2. **Staging**: Data from MongoDB and MySQL is periodically extracted to the PostgreSQL staging data warehouse.
3. **Production Data Warehouse**: Staging data is further processed and stored in the IBM DB2 production data warehouse.
4. **Big Data Analytics**: Data is collected in the Hadoop cluster for analytics, and Spark is used for analysis.
5. **Business Intelligence**: BI teams create operational dashboards using IBM Cognos Analytics connected to the IBM DB2 data warehouse.
6. **Data Pipelines**: Apache Airflow is used to manage the ETL processes moving data between the databases and data warehouses.

---

This README provides a high-level overview of the data platform architecture and the tools and technologies used by the ecommerce company.
