from dataclasses import dataclass


def lentomet(ft: int, inch: float) -> float:
    return ft*0.3048 + inch*25.4/1000

@dataclass
class Plane:
    # Dimensions
    length = lentomet(242,4)    # Meters
    mtow   = 351534             # KG
