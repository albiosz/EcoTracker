import os

import openrouteservice
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
API_KEY = os.getenv("OPEN_ROUTE_SERVICE_API_KEY")

client = openrouteservice.Client(key=API_KEY)


def get_route_distance(start, end):
    """
    Calculates the distance (in meters) between two coordinates.

    :param start: Tuple (longitude, latitude) for the starting point
    :param end: Tuple (longitude, latitude) for the destination point
    :return: Distance in kilometers
    """
    try:
        route = client.directions(
            coordinates=[start, end],
            profile='driving-car',  # Alternatives: 'cycling-regular', 'foot-walking', etc.
            format='geojson'
        )
        distance_meters = route['features'][0]['properties']['segments'][0]['distance']
        return distance_meters / 1000  # Convert meters to kilometers
    except Exception as e:
        print("Error:", e)
        return None


# Example: Berlin to Munich
start_coords = (13.4050, 52.5200)  # Berlin
end_coords = (11.5820, 48.1351)  # Munich

distance = get_route_distance(start_coords, end_coords)
if distance:
    print(f"The distance is approximately {distance:.2f} km")
