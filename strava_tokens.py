
import requests
import urllib3
import json # for debugging purposes (print pretty json)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


auth_url = "https://www.strava.com/oauth/token"

athletes_url = "https://www.strava.com/api/v3/athlete/athlete"

def get_strava_access_token(user_info):
    client_id = user_info['client_id']
    client_secret = user_info['client_secret']
    refresh_token = user_info['refresh_token']
    
    call_payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': "refresh_token",
        'f': 'json' 
    }
    
    print("Requesting Access Token...\n")
    response = requests.post(auth_url, data=call_payload, verify=False)
    #res_json = response.json()
    #print(json.dumps(res_json, indent = 4))
    access_token = response.json()['access_token']
    return access_token
    

    
    