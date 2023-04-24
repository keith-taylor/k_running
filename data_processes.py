import inflect 
p = inflect.engine()

def print_last_ten_activities(f_dataset):
    num_activities_in_words = p.number_to_words(min(10, len(f_dataset)))
    if len(f_dataset) == 1:
        print(f"Your only activity so far is: ")
    else:
        print(f"Your last {num_activities_in_words} activities were: ")
   
        
    for i in range (0, min(10, len(f_dataset))):
        activity_name = f_dataset[i]["name"].strip()
        activity_distance = round((f_dataset[i]["distance"]/1000), 1)
        activity_pace = round((f_dataset[i]["moving_time"] / 60 / activity_distance), 2)
        sport_type = (f_dataset[i]["sport_type"]).lower()
        print(f'{i+1}\t \'{activity_name}\': a {activity_distance} km {sport_type} with an average {activity_pace} min/km pace.')
    