from flask import Flask
from flask import Response, request
import os
import pymongo
from pymongo import MongoClient
from bson.json_util import loads, dumps # needed for converting mongo bson output to json

client = MongoClient('mongodb://db:27017/')
#print(client.list_database_names()) # listing databases
mydb = client['test'] # using database
mycollection = mydb["visa"] # using collection in the database

app = Flask(__name__)


@app.route('/')
def hello():
    """To check if the flask app is up"""

    return "Hello World!"


@app.route('/check')
def check():
    """A way to check if mongodb is up and running by returning the first document of the visa collection in test db"""

    return dumps(mycollection.find_one())


@app.route('/titles')
def getTitles(title = ''):
    """Get a list of job titles that even partially match the title inputted.
    
        Parameters
        ----------
        title : str
            The job title of interest 
    """

    title = request.args.get('title')
    cur = mycollection.distinct("JOB_TITLE", {"JOB_TITLE" : { "$regex": title, "$options": "si" }})
    list_cur = list(cur) # converting cursor (bson) to list
    json_data = dumps(list_cur)  # converting list to json
    return json_data


@app.route('/employers')
def getEmployers(employer = ''):
    """Get a list of employers that even partially match the employer inputted.
    
        Parameters
        ----------
        employer : str
            The name of the employer of interest 
    """

    employer = request.args.get('employer')
    cur = mycollection.distinct("EMPLOYER_NAME", {"EMPLOYER_NAME" : { "$regex": employer, "$options": "si" }})
    list_cur = list(cur) # converting cursor (bson) to list
    json_data = dumps(list_cur)  # converting list to json
    return json_data


@app.route('/salaries')
def getSalaries(employer = '', title = ''):
    """Get a list of job data (location, title, employer, submittion date and base salary) that partially match the employer and job-title inputted.
    
        Parameters
        ----------
        title : str
            The job title of interest
        employer : str
            The name of the employer of interest  
    """

    title = request.args.get('title')
    employer = request.args.get('employer')
    cur = mycollection.find({"$and":[ {"EMPLOYER_NAME":{ "$regex": employer, "$options": "si" }}, {"JOB_TITLE":{ "$regex": title, "$options": "si" }}]} \
                        , {"_id":0, "SOC_CODE":0, "SOC_NAME":0, "STATUS":0})
    list_cur = list(cur) # converting cursor (bson) to list
    json_data = dumps(list_cur)  # converting list to json
    return json_data



if __name__ == '__main__':
    #app.run()
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))