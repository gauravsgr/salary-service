#!/usr/bin/env python
# Data available at https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs/H-1B_FY14_Q4.xlsx

import pandas as pd
pd.set_option('display.max_columns', 500)  # or 1000

# Updating 2014 
df2014 = pd.read_csv('/home/jovyan/work/2014.txt', sep='\t', encoding='latin-1')
df2014 = df2014[['STATUS', 'LCA_CASE_SUBMIT', 'VISA_CLASS', 'LCA_CASE_JOB_TITLE', 'LCA_CASE_SOC_CODE', 'LCA_CASE_SOC_NAME', 'LCA_CASE_EMPLOYMENT_START_DATE','LCA_CASE_EMPLOYER_NAME', 'LCA_CASE_EMPLOYER_CITY', 'LCA_CASE_EMPLOYER_STATE', 'LCA_CASE_WAGE_RATE_FROM']]
df2014.head()
# Updating column names
df2014.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df2014.head()


# Updating 2015 
df2015 = pd.read_csv('/home/jovyan/work/2015.txt', sep='\t', encoding='latin-1')
df2015.head()
df2015 = df2015[['CASE_STATUS', 'CASE_SUBMITTED', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'EMPLOYMENT_START_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'PREVAILING_WAGE']]
# Updating column names
df2015.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df2015.head()


# Updating 2016 
df2016 = pd.read_csv('/home/jovyan/work/2016.txt', sep='\t', encoding='latin-1')
df2016.head()
df2016 = df2016[['CASE_STATUS', 'CASE_SUBMITTED', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'EMPLOYMENT_START_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM']]
# Updating column names
df2016.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df2016.head()


# Updating 2017 
df2017 = pd.read_csv('/home/jovyan/work/2017.txt', sep='\t', encoding='latin-1')
df2017.head()
df2017 = df2017[['CASE_STATUS', 'CASE_SUBMITTED', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'EMPLOYMENT_START_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM']]
# Updating column names
df2017.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df2017.head()


# Updating 2018 
df2018 = pd.read_csv('/home/jovyan/work/2018.txt', sep='\t', encoding='latin-1')
df2018.head()
df2018 = df2018[['CASE_STATUS', 'CASE_SUBMITTED', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'EMPLOYMENT_START_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM']]
# Updating column names
df2018.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df2018.head()


# Updating 2019 
df2019 = pd.read_csv('/home/jovyan/work/2019.txt', sep='\t', encoding='latin-1')
df2019.head()
df2019 = df2019[['CASE_STATUS', 'CASE_SUBMITTED', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_TITLE', 'PERIOD_OF_EMPLOYMENT_START_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM_1']]
# Updating column names
df2019.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df2019.head()

df = pd.concat([df2014, df2015, df2016, df2017, df2018, df2019]) # Pass in a list
df.to_csv('AggFile_2014_2019.txt', sep='\t', index=False)

df2019 = pd.read_csv('/home/jovyan/AggFile_2014_2019.txt', sep='\t', encoding='latin-1')
df2019.head()




# Updating 2020 Q1
df1 = pd.read_csv('/home/jovyan/2020_Q1.txt', sep='\t', encoding='latin-1')
df1.head()
df1 = df1[['CASE_STATUS', 'RECEIVED_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_TITLE', 'BEGIN_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM']]
# Updating column names
df1.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df1.head()


# Updating 2020 Q2
df2 = pd.read_csv('/home/jovyan/2020_Q2.txt', sep='\t', encoding='latin-1')
df2.head()
df2 = df2[['CASE_STATUS', 'RECEIVED_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_TITLE', 'BEGIN_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM']]
# Updating column names
df2.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df2.head()


# Updating 2020 Q3
df3 = pd.read_csv('/home/jovyan/2020_Q3.txt', sep='\t', encoding='latin-1')
df3.head()
df3 = df3[['CASE_STATUS', 'RECEIVED_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_TITLE', 'BEGIN_DATE','EMPLOYER_NAME', 'EMPLOYER_CITY', 'EMPLOYER_STATE', 'WAGE_RATE_OF_PAY_FROM']]
# Updating column names
df3.columns = ['STATUS', 'SUBMIT_DATE', 'VISA_CLASS', 'JOB_TITLE', 'SOC_CODE', 'SOC_NAME', 'START_DATE','EMPLOYER_NAME', 'CITY', 'STATE', 'BASE']
df3.head()

# Aggegating to create a final file
df = pd.concat([df1, df2, df3, df2019]) # Pass in a list
df.to_csv('AggFile_2014_2020Q3.txt', sep='\t', index=False)

# docker run -p 8888:8888 jupyter/scipy-notebook
# docker run -it -v mongodata:/data/db -p 27017:27017 --name mongodb -d mongo --bind_ip_all
# docker exec -it mongodb bash
# docker inspect mongodb | grep IPAddress
Get the ip address and replace that in the connection string and it will work
Refer https://realpython.com/introduction-to-mongodb-and-python/#pymongo
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://172.17.0.2:27017')
#client = MongoClient('mongodb://mongodb:27017/')
db = client['pymongo_test']
#Import data to mongodb
https://stackoverflow.com/questions/49895447/i-want-to-execute-mongoimport-on-a-docker-container





Run mongo docker container 
copy the 
mongoimport --db test --collection visa --drop --file /tmp/visa.json --jsonArray



FROM mongo
COPY init.json /init.json
CMD mongoimport --host mongodb --db exampleDb --collection contacts --type json --file /init.json --jsonArray



FROM mongo:4.4.2

COPY . /app
WORKDIR /app

RUN apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean
RUN apt-get install -y unzip
RUN unzip visadump_214_2020.zip

#CREATE A DUMP OF MONGO DATABASE AND COPY TO HOST
mongodump --db test --gzip
docker cp <containerID>:/app/dump/ .

# Get the number of documents in the visa collection in the test database
show dbs
use test
db.visa.count()

# To do
Write the command to take gz dump in archive format

# To get the jupyter/scipy-notebook browser link after docker-compose up has been run
https://cloudblogs.microsoft.com/industry-blog/en-gb/cross-industry/2019/06/07/how-to-use-containers-in-data-science-with-docker-and-azure-part-3/

# To connect to mongodb and using it
!pip install pymongo
import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://db:27017/')
print(client.list_database_names()) # listing databases
mydb = client['test'] # using database
collection = mydb["visa"] # using collection in the database
print(collection.find_one()) # printing the first document of the collection


# To install nano in docker container bash
apt-get update
apt-get install nano
