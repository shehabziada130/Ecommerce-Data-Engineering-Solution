# Import libraries required for connecting to mysql


import mysql.connector
# Import libraries required for connecting to DB2 or PostgreSql
import psycopg2
# Connect to MySQL
connection = mysql.connector.connect(user='root', password='Q2BqXRpAgz4XZVN1NJCjsHT2',host='172.21.106.237',database='sales')
curmysql = connection.cursor()

# Connect to DB2 or PostgreSql
dsn_hostname = '127.0.0.1'
dsn_user = 'postgres'
dsn_pwd = 'ODkxMC1zaGVoYWJ6'
dsn_port = '5432'
dsn_database = 'postgres'
      
conn = psycopg2.connect(
    database=dsn_database,
    user=dsn_user,
    password=dsn_pwd,
    host=dsn_hostname,
    port=dsn_port
)
curpg = conn.cursor()

# Find out the last rowid from DB2 data warehouse or PostgreSql data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database or PostgreSql.

def get_last_rowid():
    SQL = 'SELECT MAX(row_id) FROM sales_data'
    curpg.execute(SQL)
    res = curpg.fetchone()
    return int(res[0])
   

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
    SQL = f"SELECT * FROM sales_data WHERE rowid > {rowid}"
    curmysql.execute(SQL)
    res = curmysql.fetchall()
    return res

new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 or PostgreSql data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database or PostgreSql.
def insert_records(records):
    for record in records:
        query = f"INSERT INTO sales_data (row_id, product_id, customer_id, quantity) VALUES {record};"
        curpg.execute(query)
 
insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse
curmysql.close()
# disconnect from DB2 or PostgreSql data warehouse 
curpg.close()
# End of program