# ETL Process from MySQL to PostgreSQL Data Warehouse

This contains Python scripts for automating the ETL process from a MySQL database to a PostgreSQL data warehouse. Below is an overview of how the process works and the scripts involved.

## Overview

The ETL process involves extracting sales data from a MySQL database, transforming it, and loading it into a PostgreSQL data warehouse. This process ensures that data is cleaned, standardized, and ready for analytical purposes in the data warehouse.

## Components

### 1. MySQL Data Extraction (`mysqlconnect.py`)

The script `mysqlconnect.py` connects to the MySQL database, creates a table if it doesn't exist, inserts sample data, queries the data, and closes the connection.

### 2. PostgreSQL Data Loading (`Postgresqlonnect.py`)

The script `Postgresqlonnect.py` connects to the PostgreSQL data warehouse, creates a table if it doesn't exist, inserts sample data, queries the data, and closes the connection.

### 3. Automation Script (`automation.py`)

The `automation.py` script automates the ETL process:
- Connects to MySQL and PostgreSQL databases.
- Determines the last processed row ID from the PostgreSQL data warehouse.
- Extracts new records from MySQL that have a higher row ID than the last processed row ID.
- Inserts the new records into the PostgreSQL data warehouse.
- Closes connections after processing.

## Usage

To run the ETL process:
1. Ensure Python 3 and necessary libraries (`psycopg2` for PostgreSQL, `mysql-connector-python` for MySQL) are installed.
2. Update connection details (`user`, `password`, `host`, `database`) in the scripts to match your environment.
3. Execute the scripts in the following order:
   - `mysqlconnect.py` to set up MySQL staging.
   - `Postgresqlonnect.py` to set up PostgreSQL data warehouse.
   - `automation.py` to automate the ETL process.

## Files

- `mysqlconnect.py`: Connects to MySQL, creates a table, inserts data, and queries data.
- `Postgresqlonnect.py`: Connects to PostgreSQL, creates a table, inserts data, and queries data.
- `automation.py`: Automates the ETL process by extracting new data from MySQL and loading it into PostgreSQL.
- `README.md`: This file, providing an overview of the ETL process and instructions for usage.

## Notes

- Ensure proper configuration of database credentials and permissions.
- Customize SQL queries and data manipulation logic as per your specific requirements.
- Monitor logs and outputs to verify successful execution and data integrity in the PostgreSQL data warehouse.

This repository serves as a demonstration of a basic ETL pipeline from MySQL to PostgreSQL using Python and SQL.


