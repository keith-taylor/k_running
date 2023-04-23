import requests
import urllib3
import json # for debugging purposes (print pretty json)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

activites_url = "https://www.strava.com/api/v3/athlete/activities"

def get_strava_activites(user_access_token, f_activities_per_page, f_num_pages):
    my_header = {'Authorization': 'Bearer ' + user_access_token,'read_permission': "read_all"}
    my_params = {'per_page': f_activities_per_page, 'page': f_num_pages}
    activities_dataset = requests.get(activites_url, headers=my_header, params=my_params).json()
    return(activities_dataset)
