from symbol import return_stmt
import psycopg2
import pandas as pd 


class PostgresDBUtils:
    """The class aims to connect and communicate with the 
    postgres database

    Methods
    -------

    1. create_db: aims to create database
    2. execute_fetch_db: to fetch data from a table in database

    """

    def __init__(self):
        """instantiate our class

        Attributes
        ---------
        conn: database connection
        cursor: cursor object 

        Paramas
        -------

        None

        returns
        -------

        None
        """

        try:
            # establishing connection

            self.conn = psycopg2.connect(
                     database="airflow", user='airflow', password='airflow', 
                     host='localhost', port= '5432'   
                     )

            self.autocommit = True

            #cursor object creation using cursor method 
            self.cursor = self.conn.cursor()

        except Exception as e:
            pass 

    def create_db(self, db_name: str) -> None:
        """Creates a database with the specified database name.

        Parameters
        ----------
        db_name : str
            The name of the database we are creating

        Returns
        -------

        None

        """
        # Preparing query to create a database
        sql = f'''CREATE database ${db_name}'''
        # Creating a database
        self.cursor.execute(sql)

    def db_execute_fetch(self, table_name='', return_df=True) -> pd.DataFrame:
        """Fetches dataframe from a table with the specified name.

        Parameters
        ----------
        table_name : str
            The name of the table we are inserting into
        return_df: bool
            Return dataframe or list

        Returns
        -------

        Result: a dataframe 

        """

        query = f""" select * from {table_name}"""
        
        self.cursor.execute(query)
        # get column names
        field_names = [col[0] for col in self.cursor.description]

        # get column values
        result = self.cursor.fetchall()

        # get row count and show info
        number_of_rows = self.cursor.rowcount
        if table_name:
            print(f"{number_of_rows} records fetched from {table_name} table")

        self.cursor.close()
        self.conn.close()

        if return_df:
            return pd.DataFrame(result, columns=field_names)
        else:
            return result

    def close_connection(self):
        """
        Close the connection with the database.
        """
        self.conn.close()


