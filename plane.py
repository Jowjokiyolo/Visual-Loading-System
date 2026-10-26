from dataclasses import dataclass

import pandas as pd


def lentomet(ft: int, inch: float) -> float:
    return ft * 0.3048 + inch * 25.4 / 1000


def lbstokg(weight: float) -> float:
    return weight * 0.45359237


class Compartment:
    def __init__(self, config: pd.DataFrame) -> None:
        self.conf = config
        self.weight: float
        self.ba: float

    def __str__(self) -> str:
        return f"Compartment Weight:\t{self.weight}\nWith Balance Arm:\t{self.ba}"

    def printComp(self) -> None:
        print(self.conf)

    def printBA(self) -> None:
        print(self.ba)

    def calWeight(self) -> None:
        self.weight = self.conf["WEIGHT"].sum()

    def calBA(self) -> None:
        moment = 0
        for row in self.conf.itertuples():
            moment += row[2] * row[3]
        self.ba = moment / self.conf["WEIGHT"].sum()

    def update_weight_ba(self):
        self.calWeight()
        self.calBA()


class Cargo(Compartment):
    def load(self, weight: float, update_weight=True) -> None:
        if self.conf["MAX"].sum() < weight:
            print("Weight to fill exceeds maximum compartment weight")
            return

        counter = weight
        for row in self.conf[::-1].itertuples():  # Fills from rear
            if counter >= row[4]:
                self.conf.loc[row[0], "WEIGHT"] = row[4]
                counter -= row[4]

            else:
                self.conf.loc[row[0], "WEIGHT"] = counter
                counter = 0

        if update_weight:
            self.update_weight_ba()

        return


class Cabin(Compartment):
    def load(self, pax: int, update_weight=True) -> None:
        if pax > self.conf.__len__():
            print("ERRORSKI")
            return

        paxmass = 84  # KG
        for row in self.conf.itertuples():
            if pax > 0:
                self.conf.loc[row[0], "WEIGHT"] = paxmass
                pax -= 1
            else:
                self.conf.loc[row[0], "WEIGHT"] = 0

        if update_weight:
            self.update_weight_ba()


@dataclass
class Plane:
    # Dimensions
    # length = lentomet(242,4)
    OEW = 168682  # KG (NOT FROM KLM AS NO DOCUMENT EXISTS WITH OEW VALUES)
    BALANCE_ARM = 1180.0  # ESTIMATE INCHES FROM DATUM
    MOMENT = OEW * BALANCE_ARM

    # Configuration for B77W
    # Forward Cargo Compartment
    confFwd = pd.read_csv(r"config/LD-3_FwdCargoComp_KG.csv")
    fwdCarg = Cargo(confFwd)

    # Aft Cargo Compartment
    confAft = pd.read_csv(r"config/LD-3_AftCargoComp_KG.csv")
    aftCarg = Cargo(confAft)

    # Cabin Compartments
    # Business Class
    config01 = pd.read_csv(r"config/01_CabinBusiness.csv")
    business = Cabin(config01)

    # Premium Economy and Economy
    config02 = pd.read_csv(r"config/02_CabinPremPlusEcon.csv")
    premEcon = Cabin(config02)

    # Economy Overwing
    config03 = pd.read_csv(r"config/03_CabinOverwing.csv")
    wingEcon = Cabin(config03)

    # Economy Rear
    config04 = pd.read_csv(r"config/04_CabinAft.csv")
    rearEcon = Cabin(config04)

