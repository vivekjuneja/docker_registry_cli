# docker_registry_cli

Docker Registry CLI - Currently ONLY Supports the Search capability via Catalog API in the new version of Docker Registry v2. 

To use, run the latest Docker Registry Distribution from https://github.com/docker/distribution. The CLI uses the Catalog API available through /v2/_catalog in the new development version of Docker Registry.

**Usage:-**

`python browser.py <REGISTRY_ENDPOINT> <keyword> <options>`

REGISTRY_ENDPOINT : `<IP_ADDRESS_DOCKER_REGISTRY>:<PORT>` eg: 192.168.59.103:5000

keyword :

+ *search* - allows searching for Docker Images. Supports partial search. No RegEx Support yet. 

eg:-

`python browser.py 192.168.59.103:5000 search busybox`

`python browser.py 192.168.59.103:5000 search busy`

`python browser.py 192.168.59.103:5000 search bu`

`python browser.py 192.168.59.103:5000 search jenkins`


+ *list* - lists all the Docker images available in the Image Registry with their respective tags 

eg:- 

`python browser.py 192.168.59.103:5000 list all`


To use the Dockerfile, refer to the following examples :-

1. `docker build -t <imagename> .`

2. `docker run -p 5000:5000 -d <imagename>  192.168.59.103:5000 search busybox`

Examples:- 

`$ docker build -t docker_reg_search .`

`$ docker run docker_reg_search 192.168.59.103:5002 list all`

`-----------`

`Name: busybox`

`Tags: v1	v2	latest`

`-----------`

`Name: busy`

`Tags: v2`

`-----------`

`Name: jenkins`

`Tags: latest`


`$ docker run docker_reg_search 192.168.59.103:5002 search bus`

`-----------`

`Name: busybox`

`Tags: v1	v2	latest`

`-----------`

`Name: busy`

`Tags: v2`


New Support for SSL and Authenticated Docker Registry

Non-Auth and Non-SSL

`python browser.py 192.168.59.103:5000 search busy`

Auth and Non-SSL

`python browser.py exampleuser:exampleuser@192.168.59.103:443 search busybox auth

Auth and SSL

`python browser.py exampleuser:exampleuser@192.168.59.103:443 search mobile busybox ssl`

