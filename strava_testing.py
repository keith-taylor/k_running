import stravalib
from stravalib import Client

my_strv_client_id = str(106016)
client = Client()

url = client.authorization_url(client_id=my_strv_client_id,
                                     redirect_uri='https://www.thinkmachines.dev')



str_activities = client.get_activities()
for acty in str_activities:
    print(acty)