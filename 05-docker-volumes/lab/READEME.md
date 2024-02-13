# Lab

## Create the Postgress container that will use a named volume that will use dedicated physical device for the database data. Volume need to be named `postgres-data` and need to be mounted to the container. Please expose port 5432 externally. Container should be named as `pg-db` and should be isolated from any other containers. Once you run it, please login from external server and validate if DB is configured correctly. Below you will find configuration details:

Postgress configuration:
- Postgress DB user: `app_user`
- Postgress DB password: `P@ssw0rd123!`
- Postgress DB name: `app_db`


To create the volume:

```sh
docker volume create --opt device=/dev/sdb1 --opt type=btrfs postgres-data
```

To meet the isolation requirement dedicated network need to be created:

```sh
docker network create pg_network
```

To create Postgress container with all environment variables use following command:

```sh
docker run -d -it --name pg-db --network pg_network -e POSTGRES_PASSWORD=P@ssw0rd123! -e POSTGRES_USER=app_user -e POSTGRES_DB=app_db -e PGDATA=/var/lib/postgresql/data/pgdata -p 5432:5432 -v postgres-data:/var/lib/postgresql/data postgres
```

Validation:
```sh
# Login 
psql -h <docker-host-ip> -d app_db -U app_user

# Show DBs - app_db should be listed
\l
```
