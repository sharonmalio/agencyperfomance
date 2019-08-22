
Before uploading the data in mysql I would want to perform some data quality check.

Read csv or read data from the source API.
Load only files we need from the directory.
perform data quality check
find duplicate rows
find if dataset has a primary key
check for null values

# Conclusion from data Quality Check
# DataFrame columns have space in them, we’ll have to remove them before writing sql
# Data has to be converted in mysql data type
# Dataframe has no primary key column
# We will have to create a PK in mySql with our schema query
# We will need to have assign BIGINT for INT columns, since there max exceeds INT criteria
# No Duplicate records

set up mysql engine
fuction to generate SQL to create schema in mysql
load csv using panda
perform data cleaning tasks on each file
load dataframe in mysql

clean memory after each load
google Drive 
github jupyter Notebook




FAKE INSURANCE COMPANY

Requirements
- Python
    - mimesis (elizabeth is no longer available)
    - faker
    - matplotlib
    - sqlite3
    - numpy
    - pandas
    - sklearn
    - pydotplus
    - openpyxl
Installation
pip install -r requirements.txt
After the required packages are installed you can simply run the scripts from the phases below.

Phases
Create Database
Create the database with meaningful random data.

python createDatabase.py
Cleaning the data
Cleaning invalid data/rows that does not meet a defined criteria. Fills in data using samples or a mean/median.

python cleaning.py
EDA
Exploratory Data Analysis - understand the data and data types as well as some statistics and graphing to see the distribution, correlation, anomalies and outliers of the data.

python eda.py
PPDM
Privacy Preserving Data Mining - suppress, generalize, anatomization, perturbation, categorize, k-anonymity is done in order to preserve privacy so that sensitive attributes cannot identify a person without having the entire dataset. This makes the data safer in an instance the data is leaked, it makes it harder to impersonate someone.

python ppdm.py
Machine learning
Machine leaning was used to detect fraudulent insurance claims. This uses a simple decision tree classifier and was trained with 70/30 train/test ratio. The accuracy of the prediction was ~99% with 73117 training elements and 18280 testing elements. The tree can be seen in insurance.pdf.

python machine_learning.py"# agencyperfomance" 
