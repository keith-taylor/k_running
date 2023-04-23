import requests
from strava_tokens import get_strava_access_token
from strava_data_calls import get_strava_activites 

activities_url = "https://www.strava.com/api/v3/athlete/activities"
auth_url = "https://www.strava.com/oauth/token"
athletes_url = "https://www.strava.com/api/v3/athlete/athlete"

activities_per_page = 200
num_pages = 1

user_info = {
    'client_id': "106016",
    'client_secret': 'dd43cbabc090ed167750e44caaf17ab309aa7da5',
    'refresh_token': 'ab22c653921ac96d02b9b5a22386e9300cadbb0a',
}

access_token = get_strava_access_token(user_info, auth_url)

activities_dataset = get_strava_activites(access_token, activities_per_page, num_pages,
                                          activities_url) 

print("Your last ten runs are: ")

for i in range (0,10):
    run_name = activities_dataset[i]["name"].strip()
    run_length = round((activities_dataset[i]["distance"]/1000), 1)
    run_pace = round((activities_dataset[i]["moving_time"] / 60 / run_length), 2)
    print(f'{i+1}\t {run_name}: {run_length} km at an average {run_pace} min/km pace.')

