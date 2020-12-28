# Database setup steps

## Get the data from DOL 
The visa data can be downloaded from the [US DOL site](https://www.dol.gov/agencies/eta/foreign-labor/performance#dis) in the OFLC Programs and Disclosures section. This data is in excel files (.xlsx). We downloaded the data from 2014 - 2020 for this project. 

## Process the Excel files
We want a select few columns of interest from these excel files and not all fields. Doing that in Excel file will take a long time due to number of records each file has. We will process this in python using the pandas library. Pandas can process excel files, however that is again very slow to load up. Pandas loads text files (non-binary) files very fast. So we will open each of the excel files using MS excel and save them as tab separated file (<year>.txt) using the option provided in 'save as' in excel. It's frustating part - I know!

## Process the tsv files 
Each year's tab separated file has slightly different field names and therefore we would need to select the right columns, rename them to make them consistent across all files and then union them to get one consolidated tsv. This analysis was done using python. The code for it is in the [VisaAnalysis.py file](https://github.com/gauravsgr/salary_service/blob/main/db/VisaAnalysis.py). 
Note: The 'AggFile_2014_2020Q3.txt' file is read again into a pandas dataframe df and converted to json with record orientation as shown in the below code.

```sh
df.to_json('visa.json', orient ='records')
```
This visa.json is compressed using a zip utility and saved as visadump_2014_2020.zip file. 

## Getting the database dump for mongodb
For the first time, a mongodb docker container is run and the visa.json is copied into that running container's tmp directory. Then the visa.json file is imported into a database and a collection is formed. The following command is used from bash.  
```sh
mongoimport --db test --collection visa --drop --file /tmp/visa.json --jsonArray
```
The above command takes some time. Once the collection is created we can then take a dump of the collection. The following command is run to take a dump of the collection we created. This dump can then be used to create monogodb containers with our collection in them automatically. 
```sh
mongodump --db test --gzip
```
The above creates a dump of the database 'test' which contains our collection named 'visa' in the dump directory of the mongodb docker instance. We then exit the mongodb container bash and using the host bash copy the dump.gz file (the dump of our collection) from the mongodb container to the host. 
```sh
docker cp <containerID>:/app/dump/ .
```
## Note:
- There is a way to create the mongodb database directly from a tab separated value file. This is to be explored. [Reference example](https://stackoverflow.com/questions/31514688/how-to-use-mongoimport-for-specific-fileds-from-tsv-file). The following code should be able to work.
```sh
mongoimport --db test --collection persons  --type tsv --file persons.tsv --headerline
```
- The file size of dump.gz is more than 100 Mbs and hence github wouldn't store it and we would need to use git lfs. This will easily eat up your git lfs bandwidth for free accounts (1 Gbs) per month. It would be worth exploring the idea of loading tsv directly in mongodb. 
- Also you can't push from github to dockerhub as the dump.gz is a git lfs (large file storage) and dockerhub doesn't import lfs and will only have pointers. So, another reason to try out tsv uploads. 



