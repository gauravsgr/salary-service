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



# Cleaning up the dataset of special characters and other string manipulation
import pandas as pd
df = pd.read_csv('/home/jovyan/AggFile_2014_2020Q3.txt', sep='\t', encoding='latin-1')
df.head()

# Cleaning the base salary of '$' and ',' to make it a consistent column
df['BASE'] = df['BASE'].str.replace('$', '')
df['BASE'] = df['BASE'].str.replace(',', '')

# Cleaning the employer name and job title of special characters
df['EMPLOYER_NAME'] = df['EMPLOYER_NAME'].str.replace('[\t\n\r\f]+', '')
df['JOB_TITLE'] = df['JOB_TITLE'].str.replace('[\t\n\r\f]+', '')

# Making the fields upper case
df['JOB_TITLE'] = df['JOB_TITLE'].str.upper() 
df['EMPLOYER_NAME'] = df['EMPLOYER_NAME'].str.upper() 
df['STATUS'] = df['STATUS'].str.upper()

# Dropping the rows with NaNs
df = df.dropna()
df.to_csv('AggFile_2014_2020Q3_clean.txt', sep='\t', index=False)
