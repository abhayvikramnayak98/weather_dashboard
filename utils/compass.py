DIRECTIONS = [
    "N",
    "NNE",
    "NE",
    "ENE",
    "E",
    "ESE",
    "SE",
    "SSE",
    "S",
    "SSW",
    "SW",
    "WSW",
    "W",
    "WNW",
    "NW",
    "NNW",
]


def degrees_to_compass(degrees: float) -> str:

    index = int(
        (degrees + 11.25) / 22.5
    ) % 16

    return DIRECTIONS[index]