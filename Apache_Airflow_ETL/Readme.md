# Apache Airflow DAG: process_web_log

This Apache Airflow DAG (`process_web_log`) is designed to extract data from a web server log file, transform the data, and load the transformed data into a tar file. It runs daily to ensure continuous processing of the web log data.

## DAG Overview

The DAG consists of three main tasks executed sequentially:
1. **Extract Data (`extract_data`)**:
   - Bash command: Extracts the first field from the web server log (`accesslog.txt`) and saves it to `extracted_data.txt`.
   
2. **Transform Data (`transform_data`)**:
   - Bash command: Removes lines containing the IP address "198.46.149.143" from `extracted_data.txt` and saves the result to `transformed_data.txt`.

3. **Load Data (`load_data`)**:
   - Bash command: Creates a tar file (`weblog.tar.gz`) containing `transformed_data.txt`.

## DAG Configuration

- **Owner**: airflow
- **Start Date**: Today (`days_ago(0)`)
- **Email**: shehab@gmail.com

## Schedule

The DAG is scheduled to run daily (`schedule_interval='@daily'`) to process new web log data regularly.

## Prerequisites

Ensure the following:
- Apache Airflow is installed and configured.
- The necessary Python packages (`airflow`, `apache-airflow-providers-<provider>`) are installed.
- Web server log file (`accesslog.txt`) is available at `/home/project/airflow/dags/capstone/accesslog.txt`.

## Usage

1. **Deploy DAG**:
   - Place the DAG file (`process_web_log.py`) in the Airflow DAGs directory (`$AIRFLOW_HOME/dags/`).

2. **Run DAG**:
   - Once deployed, Airflow will automatically detect and start scheduling the DAG based on the defined `schedule_interval`.

3. **Monitor Execution**:
   - Access the Airflow UI to monitor DAG runs, task statuses, logs, and any email notifications sent to `shehab@gmail.com`.

## Files

- `process_web_log.py`: Apache Airflow DAG script.
- `README.md`: This file, providing an overview and setup instructions for the `process_web_log` DAG.

## Notes

- Adjust file paths and commands (`bash_command`) in the DAG tasks as per your environment and specific requirements.
- Ensure permissions are set correctly for reading and writing files in the specified directories.
- Monitor Airflow logs and task outputs to troubleshoot any issues during DAG execution.



