Practice Problems
Try the following practice problems to test your understanding of the lab. Please note that the solutions for the following are not shared, and the learners are encouraged to use the discussion forums in case they need help.

In the same database STAFF, create another table called Departments. The attributes of the table are as shown below.

Header	Description
DEPT_ID	Department ID
DEP_NAME	Department Name
MANAGER_ID	Manager ID
LOC_ID	Location ID


# 2
Populate the Departments table with the data available in the CSV file which can be downloaded from the link below using wget.

# 3
Append the Departments table with the following information.

Attribute	Value
DEPT_ID	9
DEP_NAME	Quality Assurance
MANAGER_ID	30010
LOC_ID	L0010

# 4
Run the following queries on the Departments Table: a. View all entries b. View only the department names c. Count the total entries


Congratulations! You have completed this lesson. At this point in the course, you know:

ETL is the process of extracting large amounts of data from multiple sources and formats and transforming it into one specific format before loading it into a database or target file. 

Web scraping is a process that can be used to extract information automatically from a website using the two Python modules “Requests” and “BeautifulSoup”.

Use the xml library to parse XML, and the pandas library to parse CSV and JSON data. 

Load a Pandas data frame to an SQL database object using the to_sql()method.

Use the Pandas read_sql() method to query a database table. This function returns a Pandas data frame with the output to the query.

Processed data can be stored as a table in a database and retrieved from it using queries, with the Pandas and SQLite libraries.