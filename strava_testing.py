
import requests
import urllib3
import json 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "106016",
    'client_secret': 'dd43cbabc090ed167750e44caaf17ab309aa7da5',
    'refresh_token': 'ab22c653921ac96d02b9b5a22386e9300cadbb0a',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Access Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
#print(res.json())
access_token = res.json()['access_token']
res_json = res.json()
print(json.dumps(res, indent = 4))
#print(f"Access Token: {access_token}\n")
#print(f"Access Token: {access_token}\n")

header = {'Authorization': 'Bearer ' + access_token,'read_permission': "read_all"}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

print("Your last ten runs are: ")

for i in range (0,10):
    run_name = my_dataset[i]["name"].strip()
    run_length = round((my_dataset[i]["distance"]/1000), 1)
    run_pace = round((my_dataset[i]["moving_time"] / 60 / run_length), 2)
    print(f'{i+1}\t {run_name}: {run_length} km at an average {run_pace} min/km pace.')

