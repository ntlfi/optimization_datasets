import numpy as np
import pandas as pd
import os


# The maximum and minimum latitude and longitude of New York State
min_lat = 40.5
max_lat = 45.016667
min_lon = -71.85
max_lon = -79.766667


current_dir = os.path.dirname(os.path.realpath(__file__))
df = pd.read_csv(f'{current_dir}/../child_care_regulated/child_care_regulated.csv')
df['lat_lon'] = df[['latitude', 'longitude']].values.tolist()

full_list_of_current_facilities = df['lat_lon'].tolist()

# generate random latitude and longitude within the range of New York State
def random_lat_lon(min_lat, max_lat, min_lon, max_lon, full_list_of_current_facilities):
    ran_lat_lon = np.random.uniform(min_lat, max_lat), np.random.uniform(min_lon, max_lon)
    # if there are at least 3 current facilities which is within 0.1 degree of the random latitude and longitude, generate a new random latitude and longitude
    if len([1 for lat_lon in full_list_of_current_facilities if np.linalg.norm(np.array(ran_lat_lon) - np.array(lat_lon)) < 0.1]) >= 3:
        return ran_lat_lon
    
# generate 100 random latitude and longitude
lst = []
lat_list = []
lon_list = []
report_len = False
while len(lst) < 10000:
    ran_lat_lon = random_lat_lon(min_lat, max_lat, min_lon, max_lon, full_list_of_current_facilities)
    if ran_lat_lon:
        lst.append(ran_lat_lon)
        lat_list.append(ran_lat_lon[0])
        lon_list.append(ran_lat_lon[1])
        report_len = True
    
    if report_len and len(lst) % 10 == 0:
        print(len(lst))
        report_len = False

# save data of random latitude and longitude to a csv file
df = pd.DataFrame(lst, columns=['latitude', 'longitude'])
df.to_csv(f'{current_dir}/potential_loc.csv', index=False)
