from dataclasses import dataclass
import pandas as pd
import data


def lentomet(ft: int, inch: float) -> float:
    return ft*0.3048 + inch*25.4/1000

class Compartment:
    def __init__(self, config: pd.DataFrame) -> None:
        self.conf =     config
        self.weight:    float
        self.ba:        float
        pass

    def loadComp(self, weight: float) -> None:
        if self.conf["MAX"].sum() < weight:
            print("Weight to fill exceeds maximum compartment weight")
            return None

        counter = weight
        for row in self.conf[::-1].itertuples():
            if counter >= row[4]:
                self.conf.loc[row[0], 'WEIGHT'] = row[4]
                counter -= row[4]

            else:
                self.conf.loc[row[0], 'WEIGHT'] = counter
                counter = 0

        return None

    def calCompBA(self):
        moment = 0
        for row in self.conf.itertuples():
            moment += (row[2] * row[3])
        self.ba = moment / self.conf["WEIGHT"].sum()

        return None

    def calCompWeight(self):
        self.weight = self.conf["WEIGHT"].sum()

        return None
    
    def printComp(self) -> None:
        print(self.conf)
        return None

    def printBA(self) -> None:
        print(self.ba)
        return None


@dataclass
class Plane:
    # Dimensions
    # length = lentomet(242,4)
    OEW = 168682            # KG (NOT FROM KLM AS NO DOCUMENT EXISTS WITH OEW VALUES)
    BALANCE_ARM = 1180.0    # ESTIMATE
    MOMENT = OEW*BALANCE_ARM

    # Configuration for B77W
    # Forward Cargo Compartment
    config  = pd.read_csv(r"config/LD-3_FwdCargoComp.csv")
    fwdComp = Compartment(config)

    # Aft Cargo Compartment
    config  = pd.read_csv(r"config/LD-3_AftCargoComp.csv")
    aftComp = Compartment(config)

