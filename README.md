# EMS (Entity Management System)

----
## 

> Entity Management System Provides Basic APIs for CRUD Operations for Entities.

----
## Steps for Setup on Local Machine

1. Install [ElasticSearch](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-elasticsearch-on-ubuntu-18-04) on your machine.
2. Install [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
3. Install pip3 for creating environment and libpq-dev for Postgres Binaries for Django Integration with Postgres:
```sudo apt-get install python3-pip python-dev libpq-dev``` 
4. Clone the Repository. 
```
git clone git@github.com:suhridmathur/ems.git 
```
5. Create virutal environment
```
virtualenv -p python3.8 env
```
6. Activate Environment & Install Requirements:
```
source env/bin/activate
```
```
pip install -r requirements.txt
```
7. Run Django Server
```
python manage.py runserver
```

