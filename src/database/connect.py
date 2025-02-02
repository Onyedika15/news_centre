# This is a function that is written to connect to the mysql database

import mysql.connector
from mysql.connector import Error
 
 
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database="news_data"
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
 
    return connection