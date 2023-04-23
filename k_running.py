import requests
import json
from strava_tokens import get_strava_access_token
from strava_data_calls import get_strava_activites 
from data_processes import print_last_ten_activities
import pprint

activities_url = "https://www.strava.com/api/v3/athlete/activities"
auth_url = "https://www.strava.com/oauth/token"
athletes_url = "https://www.strava.com/api/v3/athlete/athlete"

activities_per_page = 9
num_pages = 1

user_info = {
    'client_id': "106016",
    'client_secret': 'dd43cbabc090ed167750e44caaf17ab309aa7da5',
    'refresh_token': 'ab22c653921ac96d02b9b5a22386e9300cadbb0a',
}

access_token = get_strava_access_token(user_info, auth_url)

activities_dataset = get_strava_activites(access_token, activities_per_page, num_pages,
                                          activities_url) 

print_last_ten_activities(activities_dataset)

#activities_dataset_dic = activities_dataset[0]
#pretty_activities_dataset = json.dumps(activities_dataset_dic, indent = 4)
#print(pretty_activities_dataset)