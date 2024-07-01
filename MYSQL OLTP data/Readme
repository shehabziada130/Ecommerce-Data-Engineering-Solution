# Sales Data Analysis with MySQL

This repository contains scripts and instructions to create, analyze, and export a sales data table using MySQL.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Creating the Sales Data Table](#creating-the-sales-data-table)
3. [Importing Data](#importing-data)
4. [Performing Analysis](#performing-analysis)
5. [Creating Indexes](#creating-indexes)
6. [Listing Indexes](#listing-indexes)
7. [Exporting Data](#exporting-data)
8. [Scripts](#scripts)

## Prerequisites

Ensure you have MySQL installed and running on your system. You can download MySQL from [the official website](https://dev.mysql.com/downloads/mysql/).

## Creating the Sales Data Table

First, we create a table named `sales_data` with the following structure:

```sql
CREATE TABLE sales_data (
    product_id INT,
    customer_id INT,
    price FLOAT,
    quantity INT,
    timestamp TIMESTAMP
);

## Importing Data

To import data from a CSV file (`oltpdata.csv`) into the `sales_data` table in your MySQL database, use the following MySQL command:

```sql
LOAD DATA INFILE '/path/to/oltpdata.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

## Creating Indexes

To improve query performance, create indexes on specific columns in the `sales_data` table. For example, to index the `product_id` column, execute the following SQL command:

```sql
CREATE INDEX idx_product_id ON sales_data(product_id);

## Listing Indexes

To list all indexes on the `sales_data` table, execute the following SQL query:

```sql
SELECT table_schema, table_name, index_name, index_type
FROM information_schema.statistics
WHERE table_name='sales_data';

## Exporting Data

To export the `sales_data` table to a SQL file named `sales_data.sql` using `mysqldump`, execute the following command:

```bash
mysqldump -u root -p sales > sales_data.sql

# SoftCart Ecommerce Platform - MySQL Commands and Instructions

## Table of Contents

- [Automation Script](#automation-script)

---

## Automation Script

To automate exporting the `sales_data` table to a SQL file named `sales_data.sql`, create a bash script (`export_data.sh`) with the following content:

```bash
#!/bin/bash

# Export sales_data table to sales_data.sql file
mysqldump -u root -p sales > sales_data.sql

Make the script executable by running:
chmod +x export_data.sh


To execute the script and perform the export, run:
./export_data.sh
