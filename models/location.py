from dataclasses import dataclass


@dataclass
class Location:
    name: str
    latitude: float
    longitude: float
    country: str
    admin1: str
    timezone: str

    @property
    def display_name(self):
        parts = [
            self.name,
            self.admin1,
            self.country
        ]

        return ", ".join(
            part for part in parts
            if part
        )