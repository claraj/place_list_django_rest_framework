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

Example code using requests, which is entirely lacking in validation, exception handling etc. which you would, of course, add in a real app. 

```
import os 
import requests 

base_url = 'http://127.0.0.1:8000/api/places/'

key = os.environ.get('MOVIE_API_KEY_LOCAL')  # Set an environment variable

# A user's places must have unique names. Place ratings are out of 5

auth_header = {'Authorization': 'Token ' + key }
place = {'name': 'Wonder Woman', 'rating': 4}

response = requests.post(base_url, data=place, headers=auth_header)
wonder_woman = response.json()
wonder_woman_id = wonder_woman['id']
print('Added place', response.status_code, wonder_woman)  # expect 200, place JSON including ID assigned by server 

place = {'name': 'Batman', 'rating': 3}
response = requests.post(base_url, data=place, headers=auth_header)
batman = response.json()
print('Added place', batman)

# Patch - update Batman 
batman_id = batman['id']
response = requests.patch(f'{base_url}{batman_id}/', data={'rating': 4}, headers=auth_header)
print('After update', response.json())

# Get Batman - get one 
response = requests.patch(f'{base_url}{batman_id}/', headers=auth_header)
place = response.json()
print('Get one', place)

# Get all 
response = requests.get(base_url, headers=auth_header)
places = response.json()
print('Get all', places)

# Delete Batman 
response = requests.delete(f'{base_url}{batman_id}/', headers=auth_header)
print(response.status_code)  # 204, request processed, no content to send in response 

# Delete Wonderwoman 
response = requests.delete(f'{base_url}{wonder_woman_id}/', headers=auth_header)
print(response.status_code)  # 204, request processed, no content to send in response 
```

