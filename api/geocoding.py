import requests

from config.settings import GEOCODING_URL
from models.location import Location


def search_locations(query: str) -> list[Location]:

    response = requests.get(
        GEOCODING_URL,
        params={
            "name": query,
            "count": 8,
            "language": "en",
            "format": "json",
        },
        timeout=8,
    )

    response.raise_for_status()

    data = response.json()

    results = []

    for item in data.get("results", []):

        location = Location(
            name=item.get("name", ""),
            latitude=item["latitude"],
            longitude=item["longitude"],
            country=item.get("country", ""),
            admin1=item.get("admin1", ""),
            timezone=item.get("timezone", "auto"),
        )

        results.append(location)

    return results