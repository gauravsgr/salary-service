FROM mongo:4.4.2

# Copying the data to the container
COPY . /app
WORKDIR /app

# Getting unzip utility installed in the container
RUN apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean
RUN apt-get install -y unzip

# Unzipping the data file
RUN unzip AggFile_2014_2020Q3.zip

# Adding logpath and other things in CMD as previous CMD of mongodb docker image is removed because of 'FROM' 
# Creating a new database 'test' and collection 'visa' with the seed data 'AggFile_2014_2020Q3.txt' with headerline to tell it has headers
# Starting the mongodb
CMD mongod --fork --logpath /var/log/mongodb.log; \
    mongoimport --db test --collection visa --type tsv --file AggFile_2014_2020Q3.txt --headerline; \
    mongod --shutdown; \
    docker-entrypoint.sh mongod
