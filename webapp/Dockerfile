FROM python:3.8
WORKDIR /webapp
ADD . /webapp

# install python packages and execute python app
RUN pip3 install -r requirements.txt

# expose port 5000
EXPOSE 5000
CMD ["python3","app.py"]