import requests
from datetime import datetime

#Pixela API DOCS https://docs.pixe.la/
#Pixela https://pixe.la/

#create own token between 8 - 120 characters
TOKEN = ""
#create own name/username
USERNAME = ""
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    #agree to terms of service
    "agreeTermsOfService": "yes",
    #Agree to not being a minor if applicable
    "notMinor": "yes",
}

#This tests the code to see if the user profile has been created
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "minutes",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#This tests the code to see if the graph has been created
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#TO TEST GRAPH
#https://pixe.la/v1/users/a-know/graphs/test-graph
#REPLACE "a-know" WITH YOUR OWN USER NAME
#REPLACE "test_graph" WITH ID (IN GRAPH CONFIG)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2023, month=12, day=13)
#print(today.strftime("%y%m%d"))

pixel_date = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "169",
}

#This tests the code to see if the habit has been tracked
#response = requests.post(url=pixel_creation_endpoint, json=pixel_date, headers=headers)
#print(response.text)

#Update's Endpoint
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "120"
}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

#Delete's Endpoint
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
