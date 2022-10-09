# init a base image (Alpine is small Linux distro)
FROM python:3.7.9-alpine

# Need to get the time when image was built 
ARG CREATION_DATE

ENV DATE=$CREATION_DATE

# Need to get the dynamic parameter provided when image was built 
ARG DYNAMIC_NUMBER

ENV NUMBER=$DYNAMIC_NUMBER

# update pip to minimize dependency errors 
RUN pip install --upgrade pip

# define the present working directory
WORKDIR /flask-app

# copy the contents into the working dir
ADD . /flask-app

# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

# define the command to start the container
CMD ["python","app.py"]