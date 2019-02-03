
# How to install locally geovote application ?

* clone the repo
  ```bash
    git clone https://github.com/geovote/geovote-main.git
  ```

* install
  ```bash
    ./gv install			
  ```
* build with docker
  ```bash
    ./gv build-frontend
  ```
  
* start containers
  ```bash
    ./gv start-backend
  ```

* Test the website with a browser on "localhost" 

# How to Deploy ?

## Prerequist :

* update front-end if necessary
  ```bash
    ./gv build-frontend
  ```
* If necessary push on master of flask directory

## Process :

* see last version
  ```bash
    git tag
  ```
* increment version number (x.y.z)
  ```bash
    git tag x.y.z
   ```
* deploy to staging first for reciping
  ```bash
    ./gv -e staging deploy-backend
  ```
* connect to the staging application to verify it works : https://geovote-backend-staging.scalingo.io/

* deploy to production
  ```bash
    ./gv -e production deploy-backend
  ```
  
* connect to the production application to verify it works : https://geovote-backend.scalingo.io/
