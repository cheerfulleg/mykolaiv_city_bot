# FastAPI + Mongo and Aiogram project

## Installation and usage

- Create env files from templates both ```cp backend/example.env backend/.env ``` and ```cp bot/example.env bot/.env``` (only once)
- Edit env variables **DB_NAME** in ```backend/.env``` and **API_TOKEN** in ```bot/.env```
- Run docker stack ```docker-compose up -d```

## To give user admin rights

- Enter docker shell ```docker exec -it mongo bash```
- Enter mongo shell ```mongo```
- Enter database ```user your_database_name```
- Update user with admin rights ```db.users.update({"first_name": "Your_Name"}, { $set: {"is_admin": true}})```
