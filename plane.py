from dataclasses import dataclass
import pandas as pd


def lentomet(ft: int, inch: float) -> float:
    return ft*0.3048 + inch*25.4/1000

class Compartment:
    def __init__(self, name: str, config: pd.DataFrame) -> None:
        self.name = name
        self.conf = config
        pass

    def fillComp(self, weight: int):
        if self.conf["MAX"].sum() < weight:
            print("ERRORSKI")
            return

        



@dataclass
class Plane:
    # Dimensions
    length = lentomet(242,4)    # Meters

    # Configuration for B77W
    fwdCompConf = pd.read_csv("config/FwdCargoComp.csv")
    fwdComp = Compartment("Forward Compartment", fwdCompConf)
    fwdComp.fillComp(43651)

# print(Plane.fwdCompConf)