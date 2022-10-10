# Dockerize Python Flask Web Application

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

# Dockerfile
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