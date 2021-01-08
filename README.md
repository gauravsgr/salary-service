# Salary service

## General Info
Salary service provides RESTful APIs to get salary and other job information of people on work visas such as H1B as filed by their (potential) employers in the US for [Labor Condition Application (LCA)](https://en.wikipedia.org/wiki/Labor_Condition_Application). This primary goal of the this project was to provide the job seekers who are negotiating their offers with potential employers, information on what their potential employer usually pay, however, this api can be used for other use cases as getting statistics on salary information by location, title, employer, time, etc. The visa data has been aggregated from 2014 - 2020 (Q3) and 3+ million records stored in a database, against which the RESTful apis of this service run. Refer this [presentation](https://github.com/gauravsgr/salary-service/blob/master/demo.pdf) to get a general sense of the data availabe through the apis.

**Note:** The information aggregated and provided through the apis and the database are for informational purpose only and is provided as-is from the LCA publically shared files after cleaning them up.   

## Running service on your local
Fork the repo and clone the repo on your local machine with docker and docker-compose installed. Then run the following command from the salary-service directory. 
```sh
sudo docker-compose up -d --build
```
Once the containers are up and running, you can start making the API calls. 

## APIs
The input parameters to all the APIs do partial match and will return everything that partially or completely matches the string. The response is returned in JSON format.
Note: The URI in the following examples is for representational purposes only. The IP address of the host running the service should be replaced when making the calls. 

* GET /employers
  + Parameters: employer DESC: Name of the employer (doesn't have to be an exact value; api supports partial match)
  + Returns: Distinct list of employers which match the employer string provided in the input paramter
  + curl -X GET "http://192.168.1.25:5000/employers?employer=JO-ANN"

* GET /titles
  + Parameters: employer DESC: Title of the job (doesn't have to be an exact value; api supports partial match) 
  + Returns: Distinct list of titles which match the title string provided in the input paramter
  + curl -X GET "http://192.168.1.25:5000/titles?title=analyst"

* GET /salaries
  + Parameters: employer and title (refer DESC above; doesn't have to be an exact value; api supports partial match) 
  + Returns: JSONified dataset of salary, location, title and time for the documents (records) that match the input parameters
  + curl -X GET "http://192.168.1.25:5000/salaries?employer=microsoft&title=director"

## High level service architecture
The service is completely docker-ized. It utilized two containers for the REST api (frontend) and the database (backend). The RESTful apis are powered by a container running Flask. Flask is connects to mongodb backend running in another container. Mongodb gets seeded with the salary data upon the container start. More details on the data aggregation and mongodb data seeding can be found in the **[doc here](https://github.com/gauravsgr/salary-service/blob/master/db/database_setup.md)**. There is also a docker container running a juypter. This container has an **[embedded notebook](https://github.com/gauravsgr/salary-service/blob/master/jptr/Salary_Service_API_Calls.ipynb)** that has sample API requests made in python and transfored to pandas dataframe. The mongodb with the seeded data can be pulled from dockerhub with the following. 
```sh
docker pull gauravsgr/salary-service-db
```

## Debugging
- If you want to look into a particular container and see any warning or error messages. Docker logs is the best resource. 
```sh
docker logs salary-service_db_1
```
- If you want to connect with the mongodb container directly with your language of choice, you would need the container IP address. You can get it with the following code.
```sh
docker inspect mongodb | grep IPAddress
```

- Some general mongodb commands you can run from mongo shell (after you get into the bash of the docker container running mongodb)
```sh
# Show all databases in the mongodb
show dbs

# Use the 'test' database
use test

# Get count of the documents in a collection (visa collection here)
db.visa.count()
```

- To copy files from the docker container to the host (files can be copied from host to a live container in a similar way)
```sh
docker cp <containerID>:/app/dump/ .
```

## Future State
A web app (frontend) for this service to make it easy for the non-developers to access this information. Possibly host the webapp somewhere too. 

