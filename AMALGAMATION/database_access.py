import mysql.connector
def establish_connection():

    host='127.0.0.1'
    user='aakash'
    password='1234'
    database ='flight_project'

    conn=mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    if conn.is_connected():
        print(f'Connection Established.........')
    else:
        print(f'Connection rejected')
    return conn




