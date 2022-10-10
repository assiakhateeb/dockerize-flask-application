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

<!-- ![](https://www.docker.com/wp-content/uploads/2021/03/pythonwhale-1048x1024.png ) -->
<img src="https://www.docker.com/wp-content/uploads/2021/03/pythonwhale-1048x1024.png" width="500" height="420" />



---
<!--- BEGIN_TF_DOCS --->
## Requirements

| Name | Version |
|------|---------|
| Flask | 2.0.3 |
| Flask-WTF | any version|
| Werkzeug | any version |
| python | 3.7.9-alpine |

