import requests
import datetime as dt
#get data we want from API endpoint
# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# # print(response) <Response [200]>
# response.raise_for_status() # will raise exception if request is unsuccessful

# RESPONSE CODES
# 1XX: Hold on...
# 2XX: Here you go, successful
# 3XX: Go away, don't have permission
# 4XX: You screwed up!!!
# 5XX: Server screwed up!!!


# data = response.json() #the actual data from the request
# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# iss_position= (longitude, latitude) # store as tuple
# print(iss_position)

params = {
    'lat': 56.004940,
    'lng': -4.732860,
    'formatted': 0,
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()
data = response.json()
#we want 'results' > 'sunrise' and 'sunset'
sunset = data['results']['sunset'].split('T')[1].split(':')[0] #hour
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]

now = dt.datetime.now()
hour = now.hour