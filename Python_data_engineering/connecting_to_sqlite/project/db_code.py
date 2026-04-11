import sqlite3
import pandas as pd
conn=sqlite3.connect("STAFF.db")

# Python Scripting: Create and Load the table
"""To create a table in the database, you first need to have the attributes of the required table. Attributes are columns of the table. Along with their names, the knowledge of their data types are also required. The attributes for the required tables in this lab were shared in the Lab Scenario."""

table_name='INSTRUCTOR'
attribute_list=['ID','FNAME','LNAME','CITY','CCODE']

# Reading the CSV file
"""Now, to read the CSV using Pandas, you use the read_csv() function. Since this CSV does not contain headers, you can use the keys of the attribute_dict dictionary as a list to assign headers to the data. For this, add the commands below to db_code.py"""
file_path='INSTRUCTOR.csv'
df=pd.read_csv(file_path,names=attribute_list)

# Loading the data to a table
"""The pandas library provides easy loading of its dataframes directly to the database. For this, you may use the to_sql() method of the dataframe object.

However, while you load the data for creating the table, you need to be careful if a table with the same name already exists in the database. If so, and it isn't required anymore, the tables should be replaced with the one you are loading here. You may also need to append some information to an existing table. For this purpose, to_sql() function uses the argument if_exists. The possible usage of if_exists is tabulated below."""

df.to_sql(table_name,conn,if_exists='replace',index=False)
print('Table is ready')

# Python Scripting: Running basic queries on data
""" Now that the data is uploaded to the table in the database, anyone with access to the database can retrieve this data by executing SQL queries."""
# Viewing all the data in the table.
query_statement=f"SELECT * FROM {table_name}"
query_output=pd.read_sql(query_statement,conn)
print(query_statement)
print(query_output)

# Viewing only FNAME column of data.
query_statement = f"SELECT FNAME FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Viewing the total number of entries in the table.
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Now try appending some data to the table
"""Use the following statements to create the dataframe of the new data."""



data_dict = {'ID' : [100],
            'FNAME' : ['John'],
            'LNAME' : ['Doe'],
            'CITY' : ['Paris'],
            'CCODE' : ['FR']}
data_append = pd.DataFrame(data_dict)
'''Now use the following statement to append the data to the INSTRUCTOR table.'''


data_append.to_sql(table_name, conn, if_exists = 'append', index =False)
print('Data appended successfully')


# Viewing the total number of entries in the table after updating
query_statement = f"SELECT COUNT(*) FROM {table_name}"
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)

# Before proceeding with the final execution, you need to add the command to close the connection to the database after all the queries are executed.

# Add the following line at the end of db_code.py to close the connection to the database.

conn.close()
