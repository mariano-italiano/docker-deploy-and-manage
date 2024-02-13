# Lab

## Create two isolated networks that will have names dev and prod. Dev network will have subnet 192.168.10.0/24 and prod network will have 172.16.10.0/24. Both networks will have default gateway on .1 IP address and both need to have define an IP pool with 6 addresses available. Make sure the containers created in each can communicate with each other but they cannot communicate between networks, so prod containers cannot access dev and vice versa. In each network create two test containers and provide evidence that connection inside each network is allowed and connection outside is blocked.

There are requested isolated networks so you need to use custom bridge network. To create those two networks use following commands:

```sh
docker network create --subnet 192.168.10.0/24 --gateway 192.168.10.1 --ip-range 192.168.10.0/29 dev
docker network create --subnet 172.16.10.0/24 --gateway 172.16.10.1 --ip-range 172.16.10.0/29 prod
```

To create two test containers you can use `busybox` or `netshoot` image. In my case I create two busybox containers in each network:

```sh
docker run -d -it --name dev_c1 --network dev busybox
docker run -d -it --name dev_c2 --network dev busybox

docker run -d -it --name prod_c1 --network prod busybox
docker run -d -it --name prod_c2 --network prod busybox
```

To test connectivity you need to login to at least one container per network and validate the connectivity:

```sh
# Login
docker exec -it dev_c1 sh

# Connection test that should work
ping dev_c2

# Connection test that should not work
ping prod_c1
```

Same excercise you can perform to login to `prod_c1` or `prod_c2` container and execute same connection tests as above.

```sh
# Login
docker exec -it prod_c1 sh

# Connection test that should work
ping prod_c2

# Connection test that should not work
ping dev_c1
```

