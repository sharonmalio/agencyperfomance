import numpy as np
import pandas as pd
## set the connection to the db
import sqlalchemy
import os

from pathlib import Path

mypath = Path().absolute()
import pymysql
from IPython.display import Image

# importing the finalapi CSV file
finalapi_df = pd.read_csv('Data/finalapi.csv')

finalapi_df.head(6)
# replacing the 99999 values with 0
finalapi_df.loc[finalapi_df["RETENTION_RATIO"] == "9999"] = 0
finalapi_df.to_csv("finalapi.csv", index=False)
finalapi_df.head(5)
# data types of data frame

dtype_pd = pd.DataFrame(finalapi_df.dtypes, columns=['data_type']).reset_index()
unique_records = pd.DataFrame(finalapi_df.nunique(), columns=['unique_records']).reset_index()
info_df = pd.merge(dtype_pd, unique_records, on='index')
info_df
# It seams that there’s no primary key in our DataFrame lets check that:
print('Is there a column with unique values in entire dataFrame? : ', len(finalapi_df) in info_df['unique_records'])
# the above check point results to false
# Lets  view some basic statistical details
# summerized information( Summary statistics for all numeric columns )
data_info = finalapi_df.describe()
data_info
grouped_agency = finalapi_df.groupby('AGENCY_ID')
grouped_agency
grouped_month = finalapi_df.groupby('MONTHS')
grouped_month
grouped_year = finalapi_df.groupby('STAT_PROFILE_DATE_YEAR')
grouped_year
grouped_state = finalapi_df.groupby('STATE_ABBR')
grouped_state
grouped_minage = finalapi_df.groupby('MIN_AGE')
# Summary statistics for all numeric columns by minimum and maximum age
grouped_minage.describe()
grouped_minage.mean()
grouped_maxage = finalapi_df.groupby('MAX_AGE')
grouped_maxage.describe()
grouped_maxage.mean()

# unique prod line count?
prod_count = finalapi_df['PROD_LINE'].value_counts()
prod_count
# Are there duplicate Rows?
# No. Total rows repeating 0
print('Total rows repeating is/are', sum(finalapi_df.duplicated()))

# Conclusion from data Quality Check

# DataFrame columns have space in them, we’ll have to remove them before writing sql
# Data has to be converted in mysql data type
# Dataframe has no primary key column
# We will have to create a PK in mySql with our schema query
# We will need to have assign BIGINT for INT columns, since there max exceeds INT criteria
# No Duplicate records

# set up mysql engine

# Steps to take

# Rename column name
# Set up a connection to MySql
# Define Data Mapping as per MySql
# Write a function to return a sql schema according to input dataframe.
# Close connection

# engine = sqlchemy.create_engine('mysql+pymsql://<username>:<password>@<server-name>:<port_number>/<database_name>')
engine = sqlalchemy.create_engine('mysql+pymysql://root:malio1234@localhost:3306/agency_performance')
engine

# database connection
sql_table_name = 'perfomance'
# creating a primary key
initial_sql = "CREATE TABLE IF NOT EXISTS " + str(sql_table_name) + "(key_pk INT AUTO_INCREMENT PRIMARY KEY"


# renaming the columns to remove the white spaces.
def rename_df_cols(df):
    '''Input a dataframe, outputs same dataframe with No Space in column names'''
    col_no_space = dict((i, i.replace(' ', '')) for i in list(df.columns))
    df.rename(columns=col_no_space, index=str, inplace=True)
    return df


def dtype_mapping():
    # '''Returns a dict to refer correct data type for mysql'''
    return {'object': 'TEXT',
            'int64': 'BIGINT',
            'float64': 'FLOAT',
            'datetime64': 'DATETIME',
            'bool': 'TINYINT',
            'category': 'TEXT',
            'timedelta[ns]': 'TEXT'}


# engine = sqlchemy.create_engine('mysql+pymsql://<username>:<password>@<server-name>:<port_number>/<database_name>')

def create_sql(engine, df, sql=initial_sql):
    # '''input engine: engine (connection for mysql), df: dataframe that you would like to create a schema for,
    #     outputs Mysql schema creation'''

    df = rename_df_cols(df)

    col_list_dtype = [(i, str(df[i].dtype)) for i in list(df.columns)]

    map_data = dtype_mapping()

    for i in col_list_dtype:
        key = str(df[i[0]].dtypes)
        sql += ", " + str(i[0]) + ' ' + map_data[key]
    sql = sql + str(')')

    print('\n', sql, '\n')

    try:
        conn = engine.raw_connection()
    except ValueError:
        print('You have connection problem with Mysql, check engine parameters')

    cur = conn.cursor()

    try:
        cur.execute(sql)
    except ValueError:
        print("Ohh Damn it couldn't create schema, check Sql again")

    cur.close()


# creating the sql to be used to create our schema in MySQL
create_sql(engine, df=finalapi_df)
# Image(filename='Schema.JPG')

#  load the data in the schema that we just created

# Define relative path
# Add Data in your path
# Search for the file that need to be uploaded
# For loop to read file and load in mysql
# data cleaning in every loop
# clearing memory after every loop

data = str(mypath) + str('\\Data\\')
list_of_files = os.listdir(data)
dir_data = [str(data) + str(i) for i in list_of_files if "finalapi" in i]


def load_data_mysql(dir_data):
    for i in dir_data:
        i = pd.read_csv(i, low_memory=False)
        rename_df_cols(i)
        i.to_sql(name=sql_table_name, con=engine, index=False, if_exists='append', )
        lst = list(i)
        del lst

load_data_mysql(dir_data=dir_data)
