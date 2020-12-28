# Salary service

## General Info
Salary service provides RESTful APIs to get salary and other job information of people on work visas such as H1B as filed by their (potential) employers in the US for [Labor Condition Application (LCA)](https://en.wikipedia.org/wiki/Labor_Condition_Application). This primary goal of the this project was to provide the job seekers who are negotiating their offers with potential employers, information on what their potential employer usually pay, however, this api can be used for other use cases as getting statistics on salary information by location, title, employer, time, etc. The visa data has been aggregated from 2014 - 2020 (Q3) and stored in a database, against which the RESTful apis of this service run. The information aggregated and provided through the apis and the database are for informational purpose only. 

## Running service on your local
Fork the repo and clone the repo on your local machine with docker and docker-compose installed. Then run the following command from the salary-service directory. 
```sh
sudo docker-compose up -d 
```
Once the containers are up and running. 

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

## Request for Features
Open issues if you want to request features or fork and add in features. 

## Future State
A web app (frontend) for this service to make it easy for the non-developers to access this information. Possibly host the webapp somewhere too. 
