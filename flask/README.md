
# How to install locally geovote application ?

* $git clone https://github.com/geovote/geovote-main.git
* $./geovote install			
* $./geovote build-frontend	
* $./geovote start-backend
* Test the website with a browser on "localhost" 

# How to Deploy ?

## Prerequist :

* $./geovote build-frontend		=> update front-end if necessary
* If necessary push on master of flask directory

## Process :

* $git tag					=> to see last version
* $git tag x.y.z 				=> increment version number (x.y.z)
* $./geovote -e staging deploy-backend
* Connect to the staging application to verify it works : https://geovote-backend-staging.scalingo.io/
* $./geovote -e production deploy-backend
* Connect to the production application to verify it works : https://geovote-backend.scalingo.io/
