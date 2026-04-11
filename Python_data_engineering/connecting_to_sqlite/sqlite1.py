# SQLite3 is an in-process Python library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. It is a popular choice as an embedded database for local/client storage in application software.

# connecting sqlite
# we can connect to SQLIte3 using the connect() function by passing the required database name as an argument.
import sqlite3
sql_connection=sqlite3.connect('my.db')
# This makes the variable sql_connection an object of the SQL code engine. You can then use this to run the required queries on the databas
# creating a database table using SQLite3 and Pandas?
df.to_sql(table_name,sql_connection,if_exists='replace',index=False)
# Here, we use the to_sql() function to convert the pandas dataframe to an SQL table.
# The table_name and sql_connection arguments specify the name of the required table and the database to which you should load the dataframe.
# The if_exists parameter can take any one of three possible values:
# 'fail': This denies the creation of a table if one with the same name exists in the database already.
# 'replace': This overwrites the existing table with the same name.
# 'append': This adds information to the existing table with the same name
# keep the index parameter set to True only if the index of the data being sent holds some informational value. Otherwise, keep it as False.

""" query a database table using SQLite3 and Pandas?"""
# by using pandas function .read_sql() to query database table
# The function returns a Pandas dataframe with the output to the query. Use the function with the following syntax:
df=pd.read_sql(query_statement,connection)

"""SELECT * FROM table_name
SELECT COUNT(*) FROM table_name
SELECT Column_name FROM table_name
SELECT * FROM table_name WHERE <condition>"""