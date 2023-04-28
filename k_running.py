
from user_info import *

#import requests
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

user_info = keith_taylor
#user_info = keith_test

user_payload = {
    'client_id': user_info['client_id'],
    'client_secret': user_info['client_secret'],
    'refresh_token': user_info['refresh_token'],
}

access_token = get_strava_access_token(user_info, auth_url)

activities_dataset = get_strava_activites(access_token, activities_per_page, num_pages,
                                          activities_url) 
#print(activities_dataset)

print_last_ten_activities(activities_dataset)

# activities_dataset_dic = activities_dataset[0]
# pretty_activities_dataset = json.dumps(activities_dataset_dic, indent = 4)
# print(pretty_activities_dataset)