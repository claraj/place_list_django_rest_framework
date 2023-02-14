## Place API 

### How to run locally 

#### Install requirements

`pip install -r requirements.txt`   Or whatever your local pip, virtual environment etc preferences are 

#### Set up database 

`python manage.py migrate`

#### Create superuser 

`python manage.py createsuperuser`

Enter username, password when prompted and remember them

#### Run server 

`python manage.py runserver`

Visit http://127.0.0.1:8000 in your browser, expect to see a 'Hello android students' messsage

Visit http://127.0.0.1:8000/admin to browse app's data. Look for Tokens and create a token for your user. 

#### Stopping server 

Press Control+C to stop the server. 

### Example API calls

GET http://127.0.0.1:8080/api/places/   **Get all places**  
GET http://127.0.0.1:8080/api/places/1/   **Get place with ID 1**  
POST http://127.0.0.1:8080/api/places/   **Create a new place**  
PATCH http://127.0.0.1:8080/api/places/1/   **Edit place 1**   
DELETE http://127.0.0.1:8080/api/places/1/   **Delete place 1**   

The trailing slashes for POST, PATCH are important otherwise the API server will redirect to GET requests. 

POST and PATCH requests should include the relevant data as JSON 

All requests require an authorization header containing your key in this form `Authorization: Token 123456787234567871234567876543`

 


