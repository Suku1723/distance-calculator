import requests
from creds import key

class LocationEntry:
# Vijay doing work
    def __init__(self, currLocation, destination) -> None:
        self.currLocation = currLocation
        self.destination = destination

    def get_distance(self):  
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?destinations={self.destination}&origins={self.currLocation}&units=imperial&key={key}"
        r = requests.get(url)
        data = r.json()
        
        if data['status'] == 'OK':
            element = data['rows'][0]['elements'][0]
            distance_text = element['distance']['text']
            
            distance_miles = float(distance_text.split()[0])
            
            return distance_miles
        else:
            return None