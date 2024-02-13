# Lab

## Create a Docker image for application that will be written in Python using Flask server. The main aim of the application will be to manage the courses, and it need to run as web frontend interface on port 5000 (Flask default). Take care about all required Python libraries and dependencies by using `requirements.txt` file. Create multiple routes to handle following tasks: create course, delete course, get all courses and initialize empty postgress database. Website should also have some test page and welcome page that will be shown once application is started. Please take care about the look and feel and use styles as well as HTML templates. Create Dockerfile and build the image with tag docker-flask:2.0. Upload it to Docker Hub and remove local image. As final test create a container using Docker Hub image.

The whole application files are available [HERE](flask-app).

To crate the image and tag it properly:

```sh
cd flask-app
docker build -t docker-flask:2.0 .
```

To upload image to Docker Hub:

```sh
# Login to Docker Hub
docker login 

# Upload the image
docker push <reponame>/docker-flask:2.0 
```

To remove local image:

```sh
docker image rm docker-flask:2.0
```

To perform final test and run the container with Docker Hub image:

```sh
docker run -d -it --name falsk-app -p 5000:5000 <reponame>/docker-flask:2.0
```
