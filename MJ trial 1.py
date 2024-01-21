#Project: OEM (Operation: Eternal Micheal)
#Purpose: this program will use micheal jackson lyrics and build
#a machine learning AL to make new micheal jackson songs
#Creation Date: 1/20/24

# requests and pandas were not included at first
#so i used the following code in terminal to install them
#python -m venv env to activate the environment
#source env/bin/activate
#python -m pip install --upgrade pip upgrade pip and install the following
#pip3 install requests
#pip3 install pandas
import requests
import json
import pandas as pd

#Function to authenticate and make requests from Genius API

client_id = "URiWfR2_bQsTbuKEsNdVZt7EtwyUUQ-w6-c_ROsxdkiMemAcP70x0fWVVTMfxMpS" 
client_secret = "_D92xS1ZEl-VrBo3K-a9-zRN3v3sBXl3j23BKEAdOvyP_riciihoC1ri8CT7baCvNXEnnVGIJJlvB4oEuLzG_A"

def get_genius_token():

    url = "https://api.genius.com/oauth/token" 
    data = {'client_id': client_id, 
            'client_secret': client_secret,
            'grant_type': 'client_credentials'}
    response = requests.post(url, data=data)
    
    access_token = response.json()['access_token']
    return access_token


def get_song_info(song_id, access_token):
  
    endpoint = f"https://api.genius.com/songs/{song_id}"
    headers = {"Authorization": f"Bearer {access_token}"}
       
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    song_info = response.json()["response"]["song"]
    print(song_info)

    return song_info



access_token = get_genius_token()
song_id = "242122" # Example song ID

song_data = get_song_info(song_id, access_token)
print(song_data)


# Print raw full response 
print(response.text)

# Check if JSON decoded 
print(type(response.json()))

# Print keys of base JSON  
print(list(response.json().keys()))

# Try accessing song data from base level
song_info = response.json()['song'] 

# Access step-by-step
json = response.json()
meta = json['meta']  
print(meta)

# Use test client ID  
test_id = "123_fake"
url = f"https://api.genius.com/songs/{test_id}" 

# Output response to file
with open('genius.json', 'w') as f:
    f.write(response.text)