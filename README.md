# docker_registry_cli
Docker Registry CLI - Supports Search function via Catalog API in the new version of Docker Registry v2. 

To use, run the latest Docker Registry Distribution from https://github.com/docker/distribution

**Usage:-**


`python browser.py <REGISTRY_ENDPOINT> <keyword> <options>`

`<REGISTRY_ENDPOINT> : <IP_ADDRESS_DOCKER_REGISTRY>:<PORT>` eg: 192.168.59.103:5000

<keyword> :

+ *search* - allows searching for Docker Images. Supports partial search. No RegEx Support yet. 

eg:-

`python browser.py 192.168.59.103:5000 search busybox`

`python browser.py 192.168.59.103:5000 search busy`

`python browser.py 192.168.59.103:5000 search bu`

`python browser.py 192.168.59.103:5000 search jenkins`


+ *list* - lists all the Docker images available in the Image Registry with their respective tags 

eg:- 

`python browser.py 192.168.59.103:5000 list all`



