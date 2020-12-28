FROM mongo:4.4.2

COPY . /app
WORKDIR /app

# CMD mongod --fork --logpath /var/log/mongodb.log; \
#     mongorestore --gzip --archive=dump.gz; \
#     mongod --shutdown; \
#     docker-entrypoint.sh mongod

RUN apt-get update -y && \
     apt-get upgrade -y && \
     apt-get dist-upgrade -y && \
     apt-get -y autoremove && \
     apt-get clean
RUN apt-get install -y unzip
RUN unzip AggFile_2014_2020Q3.zip

CMD mongod --fork --logpath /var/log/mongodb.log; \
    mongoimport --db test --collection visa --type tsv --file AggFile_2014_2020Q3.txt --headerline; \
    mongod --shutdown; \
    docker-entrypoint.sh mongod