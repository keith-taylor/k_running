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

keith_taylor = {
    'user_name': 'keith-taylor',
    'vanity_url': 'https://www.strava.com/athletes/keith-taylor',
    'client_id': "106016",
    'client_secret': 'dd43cbabc090ed167750e44caaf17ab309aa7da5',
    'refresh_token': 'ab22c653921ac96d02b9b5a22386e9300cadbb0a',
}

keith_test = {
    'user_name': 'keith-taylor',
    'vanity_url': 'https://www.strava.com/athletes/keith_api',
    'client_id': "106247",
    'client_secret': '570c7611ecb7f63666458b789d743bed06683a07',
    'refresh_token': 'b4181e935807b17bb8690f42a264fbcdceb87549', 
}

user = keith_taylor

user_info = {
    'client_id': user['client_id'],
    'client_secret': user['client_secret'],
    'refresh_token': user['refresh_token'],
}

access_token = get_strava_access_token(user_info, auth_url)

activities_dataset = get_strava_activites(access_token, activities_per_page, num_pages,
                                          activities_url) 
print(activities_dataset)

print_last_ten_activities(activities_dataset)

activities_dataset_dic = activities_dataset[0]
pretty_activities_dataset = json.dumps(activities_dataset_dic, indent = 4)
print(pretty_activities_dataset)