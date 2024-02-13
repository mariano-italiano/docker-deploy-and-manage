# Lab

## Let's assume you are a DevOps engineer working on a project that requires running multiple Docker containers on a remote server. You have already built the Docker images and pushed them to a container registry. Your task is to create the container called red1 that is using redis image in version 7.0 alpine and configure it to start automatically when the server reboots. Set environment variable app equal to development, inside the container.

To create a container execute the command:

```sh
docker run -d --restart=always --env app=development --name red1 redis:7.0-alpine
```

where:
- `-d` flag run the container in detached mode
- `--restart=always` flag set the restart policy to the container
- `--env app=development` flag set the environment variable inside the container
- `--name red1` flag will set requested name for the container
- `redis:7.0-alpine` defines the image name that was requested

To validate the configuration of the container once it's running use following commands:

```sh
docker inspect --format '{{.Config.Env}}' red1
docker inspect red1 | grep -i env -A 6
```
