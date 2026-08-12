import requests
import time

from config.settings import GEOCODING_URL
from models.location import Location


def search_locations(query: str) -> list[Location]:

    request_started = time.perf_counter()

    print()
    print("========== GEOCODING DEBUG ==========")
    print(
        f"Request started: {request_started:.4f}"
    )

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

    request_finished = time.perf_counter()

    print(
        f"Request finished: "
        f"{request_finished:.4f}"
    )

    print(
        f"HTTP request time: "
        f"{request_finished - request_started:.3f} seconds"
    )

    print(
        "====================================="
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