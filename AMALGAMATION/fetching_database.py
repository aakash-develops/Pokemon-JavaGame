from sys import float_info
from tkinter.font import names

from database_access import establish_connection

conn=establish_connection()

cursor=conn.cursor()
#for AIRPORT TABLE
cursor.execute("SELECT * FROM airports_project")
airport_rows=cursor.fetchall()
airport_columns=[desc[0] for desc in cursor.description]

#for COUNTRY TABLE
cursor.execute("SELECT * FROM country")
country_rows=cursor.fetchall()
country_columns=[desc[0] for desc in cursor.description]

# print (columns)
# print (rows[1])
def store_data():
    flight = {}
    for row in airport_rows:
        row_dict = dict(zip(airport_columns, row))

        row_dict['airport_name']=row_dict.get('name','unknown')

        for c_row in country_rows:
            country_code=c_row[1] # this is the code column in country table
            country_name=c_row[2] #this is the name column in country table
            if row_dict['country']==country_code:
                row_dict['name']=country_name #over writing with country name
                break
        else:
            row_dict['name']="unknown"

        flight[row_dict['ident']]=row_dict

    return flight






# for i in data:
#     print(f'{i } is {data[i].latitude}')
















# print(rows)
# count=0
# for row in rows:
#     if row!=0:
#         count+=1
#
# print(count)


