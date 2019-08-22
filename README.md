
## STEPS FOR THE ETL
1. Perform some data quality check.
1. Read csv or read data from the source API.
2. Load only files we need from the directory.
3. perform data quality check
4. Find duplicate rows
5. Find if dataset has a primary key
6. Check for null values
7. Set up mysql engine
8. Generate SQL to create schema in mysql
9. load csv using panda
10. Perform data cleaning tasks on each file
11. Load dataframe in mysql
12. Clean memory after each load

### Conclusion from data Quality Check

1. DataFrame columns have space in them, we’ll have to remove them before writing sql
2. Data has to be converted in mysql data type
3. Dataframe has no primary key column
4. We will have to create a PK in mySql with our schema query
5. We will need to have assign BIGINT for INT columns, since there max exceeds INT criteria
6. No Duplicate records


## FAKE INSURANCE COMPANY
### Installation 
pip install -r requirements.txt
After the required packages are installed you can simply run the scripts from the phases below.

