import os 
import requests 

base_url = 'http://127.0.0.1:8000/api/places/'


# key = os.environ.get('MOVIE_API_KEY_LOCAL')  # Set an environment variable
key = '7f236c67431949c24aa40cbcde7d0159291c83e6'


auth_header = {'Authorization': 'Token ' + key}


# Get all 
response = requests.get(base_url, headers=auth_header)
places = response.json()
print('Get all', places)


place = {'name': 'Toronto', 'priority': 1}
response = requests.post(base_url, data=place, headers=auth_header)
toronto = response.json()
toronto_id = toronto['id']
print('Added place', response.status_code, toronto)  # expect 200, place JSON including ID assigned by server 


# place = {'name': 'Auckland, NZ', 'priority': 3}
# response = requests.post(base_url, data=place, headers=auth_header)
# auckland = response.json()
# print('Added place', auckland)

# # Patch - update Auckland 
# auckland_id = auckland['id']
# response = requests.patch(f'{base_url}{auckland_id}/', data={'priority': 4}, headers=auth_header)
# print('After update', response.json())

# # Get Auckland - get one 
# response = requests.patch(f'{base_url}{auckland_id}/', headers=auth_header)
# place = response.json()
# print('Get one', place)

# # Get all 
# response = requests.get(base_url, headers=auth_header)
# places = response.json()
# print('Get all', places)

# # Delete Auckland 
# response = requests.delete(f'{base_url}{auckland_id}/', headers=auth_header)
# print(response.status_code)  # 204, request processed, no content to send in response 

# # Delete Toronto 
# response = requests.delete(f'{base_url}{toronto_id}/', headers=auth_header)
# print(response.status_code)  # 204, request processed, no content to send in response 