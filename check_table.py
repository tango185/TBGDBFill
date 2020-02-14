from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def check_table(query):
    """ Connect to MySQL Database """

    try:
        db_config = read_db_config()
        print("Connecting to MySQL database...")
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print("Connection established.")
        else:
            print("Connection failed.")

        cursor = conn.cursor()
        cursor.execute(query)

        if len(cursor.fetchall()) > 0:
            return True
        else:
            return False

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")
