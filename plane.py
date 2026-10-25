from dataclasses import dataclass
import pandas as pd


def lentomet(ft: int, inch: float) -> float:
    return ft*0.3048 + inch*25.4/1000

class Compartment:
    def __init__(self, config: pd.DataFrame) -> None:
        self.conf = config
        self.ba: float
        pass

    def fillComp(self, weight: int) -> None:
        if self.conf["MAX"].sum() < weight:
            print("ERRORSKI")
            return

        counter = weight
        for row in self.conf[::-1].itertuples():
            if counter >= row[4]:
                self.conf.loc[row[0], 'WEIGHT'] = row[4]
                counter -= row[4]

            else:
                self.conf.loc[row[0], 'WEIGHT'] = counter
                counter = 0

            print(self.conf)
            
        return None



@dataclass
class Plane:
    # Dimensions
    length = lentomet(242,4)    # Meters

    # Configuration for B77W
    fwdCompConf = pd.read_csv("config/FwdCargoComp.csv")
    fwdComp = Compartment(fwdCompConf)
    fwdComp.fillComp(5200)

# print(Plane.fwdCompConf.__len__())