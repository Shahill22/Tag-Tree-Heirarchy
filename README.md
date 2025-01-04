# Tag Tree Hierarchy - Vue Js & Python

A full stack Vue and python web application using Postgres for Nested Tags Tree.

## Note: API Code under master branch (Switch to master branch to view code) 
## Note: Database Credentials and url added directly to code without using .env file for easier testing.

## Requirements

- Python (https://nodejs.org/)
- Vue/cli
- npm (Node Package Manager)
- Django
- djangorestframework
- pip
- psycopg2(postgresql database driver)

## Getting Started

1. Clone the repository:

   ```bash
   git clone -b master https://github.com/Shahill22/Tag-Tree-Heirarchy.git
   

2. Install dependencies (Frontend):

   ```bash
   cd frontend/
   npm install

3. Install dependencies (Backend):

   ```bash
   cd backend/backend
   pip install django
   pip install psycopg2
   pip install djangorestframework

3. Database Setup:
   - The application uses Postgresql as the default database. Create a database using PG Admin or other UI databse viewers. Run the query to create a table given in the db folder. 
   - To insert temporary data, use the insert data query from the db folder.
   - If you want to use a different database (e.g., MySQL, PostgreSQL), update the dialect accordingly. You may need to install the corresponding database driver/package.

4. Starting the server (Backend):
    - Change the username, password and port of database in backend/settings.py. 
        DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': 'tag-view',       # Your database name
                    'USER': 'name', # Your database username
                    'PASSWORD': 'password', # Your database password
                    'HOST': 'localhost',
                    'PORT': '5432',
                }
            }
        
    ```bash
    python3 manage.py makemigrations tag_tree_manager
    python3 manage.py migrate
    python3 manage.py runserver

4. Starting the server (Frontend):

## Note: Backend Server should be running first, and DB should have initial temporary data
        
    ```bash
    cd frontend
    npm install
    npm run serve

   The server will start, and you should see the message "Server is running on port 8081" in the console.

## Screenshots
1. UI
![image](https://github.com/user-attachments/assets/5c0ba4e8-5bcf-4996-923d-c422e408c821)

2. API Calls
![image](https://github.com/user-attachments/assets/c4ed2cd2-82e0-4fc2-a7f0-d1a19be8e613)

3. Database
![image](https://github.com/user-attachments/assets/e2383137-03b2-48a2-9c6d-5ac506779143)



