# Change this to be your API key.
import os

import requests
from dotenv import load_dotenv

load_dotenv()
MY_API_KEY=os.getenv("CLIMATIQ_API_KEY")

# Example from climatiq tutorials: https://www.climatiq.io/docs/guides/how-tos/using-python
def example():
    url = "https://api.climatiq.io/data/v1/search"
    query="grid mix"
    data_version = "^3"

    query_params = {
        # Free text query can be written as the "query" parameter
        "query": query,
        "data_version": data_version,
        # You can also filter on region, year, source and more
        # "AU" is Australia
        "region": "AU"
    }

    # You must always specify your AUTH token in the "Authorization" header like this.
    authorization_headers = {"Authorization": f"Bearer {MY_API_KEY}"}

    # This performs the request and returns the result as JSON
    return requests.get(url, params=query_params, headers=authorization_headers).json()


response = example()
# And here you can do whatever you want with the results
print(response.get("current_page"))
