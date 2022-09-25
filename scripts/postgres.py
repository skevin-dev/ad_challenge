import psycopg2
import pandas as pd 


class PostgresDBUtils:
    """The class aims to connect and communicate with the 
    postgres database

    Methods
    -------

    1. create_db: aims to create database
    2. create_table: aims to create a table in database
    3. insert_into_table: aims to insert data into a table created
    4. execute_fetch_db: to fetch data from a table in database

    """