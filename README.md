# Simple django example


## Local Environment
The local django example will connect postgres in docker.
### Database
#### Start database
1. Download and install docker and docker compose.
2. Go to postgres folder.

Pull image
```commandline

docker-compose pull
```
Start docker in background
```commandline
docker-compose up -d
```
#### Access to postgres:
- localhost:5432
- Username: postgres (as a default)
- Password: postgres (as a default)
#### Access to PgAdmin:
- URL: http://localhost:5050
- Username: pgadmin4@pgadmin.org (as a default)
- Password: admin (as a default)
#### Add a new server in PgAdmin:
- Host name/address postgres
- Port 5432
- Username as POSTGRES_USER, by default: postgres
- Password as POSTGRES_PASSWORD, by default postgres

### Start Django
1. Go to folder sample_web.
2. Create the '.env' file
```text
DEBUG=True|False
DATABASE_URL=postgres://username:password@host:port/dbname
SECRET_KEY=[Your secret key]
```
3. Start the web.
```commandline
python manage.py runserver
```

### Run Test
1. Go to folder sample_web.
```commandline
python manage.py test .
```

### Migrate database
#### New database
```commandline
python manage.py makemigrations

python manage.py migrate
```

### Create admin
```commandline
python manage.py createsuperuser
```

#### Existing database
There are two method:
1. Manual way
   1. Manual create the migrations python.
   2. If not able to do that, then manually write sql script.
   3. Every updated need re-run the unit test.
2. Handle by django
   1. Execute below script
```commandline
python manage.py makemigrations

python manage.py migrate
```

## Deploy AWS
Install AWS Beanstalk CLI in local
```commandline
pip install awsebcli
```
Check CLI version
```commandline
eb --version
```
Init beanstalk config
```commandline
eb init
```
Create AWS resource
```commandline
eb create
```
Update Environment Variable in AWS Beanstalsk

Deploy to AWS
```commandline
eb deploy
```
Collect static resource
```commandline
python manage.py collectstatic
```