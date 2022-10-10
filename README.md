# Dockerize Python Flask Web Application

## Table of Contents

## Description
In this repository, we will create a docker image that includes a simple python flask web application that has the following apis/endpoints:
1. **`/creation`** - provides the time the image was built.
2. **`/dynamic`** - a dynamic parameters / value provided when the image is built.
3. **`/dockerfile`** - provides the dockerfile the image was created with (in the image).
4. **`/`** - returns an index.html.
5. **`/put`** - gets a file and stores it on the image runtime. 
6. **`/get?filename`** - returns a file from the lcoal store (that was uploaded previously). 
7. **`/list`** - list all files that were uploaded previously.

<p align="center">
<img src="https://www.docker.com/wp-content/uploads/2021/03/pythonwhale-1048x1024.png" width="400" height="320" /></p>



---
<!--- BEGIN_TF_DOCS --->


| Requirements |
|------|
| python v3.7.9-alpine |
| Flask | 
| Docker | 



## Getting started
### Step 1: Build the docker image

> Run the following command to create the docker image from src directory<br>
Pass in the **-t** parameter to name your image flask-app. <br>
Also, Pass in the **--build-arg** parameter to set the image creation time and the dynamic variable<br>

```
docker image build --build-arg CREATION_DATE="$(date)" --build-arg DYNAMIC_NUMBER="16" -t flask-app .
```
> Verify that your image shows in your image list: <br>

```
docker image ls
```
### Step 2: Run the docker container 
> The **-p** flag maps a port running inside the container to your host.<br> In this case, we're mapping the Python app running on port 8080 inside the container to port 8080 on your host.<br>
 **-d** flag means that a Docker container runs in the background of your terminal.

```
docker run -d -p 8080:8080 --name flask-api-app flask-app
```
### OR Pull the image from DockerHub 
```
docker pull assiak/flask-app
```
### Then run the installed image with run command
```
docker run -d -p 8080:8080 --name flask-api-app assiak/flask-app
```
https://hub.docker.com/u/assiak 

### Step 3:  Access The application from the host machine
```
Navigate to http://127.0.0.1:8080 in a browser to see the web application.
```
### Tip:
If you want to see logs from your application, you can use the `docker container logs` command.<br> By default, `docker container logs` prints out what is sent to standard out by your application.
```
$ docker container ls

You should see your container id by running this command.
CONTAINER ID   IMAGE              COMMAND           CREATED          STATUS          PORTS                                       NAMES
41b0f0701dfa   assiak/flask-app   "python app.py"   21 minutes ago   Up 21 minutes   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   flask-api-app

$ docker container logs flask-api-app

output should be look like : * ... 
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://172.17.0.2:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 205-345-037
172.17.0.1 - - [10/Oct/2022 14:56:02] "GET /dockerfile HTTP/1.1" 200 -
172.17.0.1 - - [10/Oct/2022 14:56:05] "GET /list HTTP/1.1" 200 -
172.17.0.1 - - [10/Oct/2022 14:56:06] "GET /get HTTP/1.1" 200 -
172.17.0.1 - - [10/Oct/2022 14:56:08] "GET /put HTTP/1.1" 200 -
```
### Step 4: Stop the docker container
```
docker container stop flask-api-app
```
### Step 5:  Remove the stopped container and remove the image
```
$ docker container rm flask-api-app
$ docker image rm flask-app 
or 
$ docker image rm assiak/flask-app 
```
#### OR:
> Use the following command removes any stopped containers, unused volumes and networks, and dangling images.
```
docker system prune
```


Link to DockerHub: https://hub.docker.com/u/assiak 

## DEMO:
Pull the image and run the docker container:

https://github.com/assiakhateeb/dockerize-flask-application/blob/master/demo-run-docker-container.mp4

## Understanding the Dockerfile
Dockerfile consists of a set of instructions to create docker image of the application.
```
1. FROM python:3.7.9-alpine
2. ARG CREATION_DATE
3. ENV DATE=$CREATION_DATE
4. ARG DYNAMIC_NUMBER
5. ENV NUMBER=$DYNAMIC_NUMBER
6. RUN pip install --upgrade pip
7. WORKDIR /flask-app
8. ADD . /flask-app
9. RUN pip install -r requirements.txt
10.CMD ["python","app.py"]
```
**Line by line description:** <br>
<!-- -->
```1. FROM python:3.7.9-alpine ``` <br />
> FROM allows us to initialize the build over a base image. In our case, we are using a python:3.7.9-alpine image. (Alpine is a small Linux Distribution (~ 5MB).) In short, we are using a Linux environment with python 3.6.5 for our app.<br />

```2. ARG CREATION_DATE ``` <br />
> Defines the image creation date variable. we'll set it during build using the --build-arg flag.<br />

```3. ENV DATE=$CREATION_DATE ``` <br />
> Image creation date environment variable which is passed to the container.<br />

```4. ARG DYNAMIC_NUMBER ``` <br />
> Defines a dynamic variable provided when image was built. we'll set it during build using the --build-arg flag.<br />

```5. ENV NUMBER=$DYNAMIC_NUMBER ``` <br />
> Passing the dynamic variable to the container.<br />

```6. RUN pip install --upgrade pip ``` <br />
> Run instruction to update pip to minimize dependency errors.<br />

```7. WORKDIR /flask-app ``` <br />
>  A work directory called flask-app where the "present working directory" will be set.

```8. ADD . /flask-app ``` <br />
> Copy everything in the current directory (our server code and configurations) into the flask-app directory.

```9. RUN pip install -r requirements.txt ``` <br />
> Run pip to install the dependencies of our application.

```10. CMD ["python","app.py"] ``` <br />
> CMD is the command that is executed when we start a container. <br /> Here, we are using CMD to run a Python applcation. 



## Useful Links
 [Get Started with Docker](https://www.docker.com/get-started/) <br>
 [Build time arguments](https://docs.docker.com/engine/reference/builder/#arg) <br>
