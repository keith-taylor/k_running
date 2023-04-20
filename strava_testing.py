
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "106016",
    'client_secret': 'dd43cbabc090ed167750e44caaf17ab309aa7da5',
    'refresh_token': '0069492457c0e43f120495a203b954f6bb69669f',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
#access_token = res.json()['access_token']
access_token = '256b159c464ef2cc0a46f1b2cb1a87b2dc3d4621'
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token, 'read_permission': "read_all"}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

print("Your last ten runs are: ")
for i in range (1,11):
    run_name = my_dataset[i]["name"].strip()
    run_length = round((my_dataset[i]["distance"]/1000), 1)
    print(f'{i}\t {run_name} - {run_length} km.')
