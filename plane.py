from dataclasses import dataclass

import pandas as pd


def lentomet(ft: int, inch: float) -> float:
    return ft * 0.3048 + inch * 25.4 / 1000


def lbstokg(weight: float) -> float:
    return weight * 0.45359237


def calmac(ba: float) -> float:
    return ((ba - 1174.5) * 100.0) / 278.5


class Compartment:
    def __init__(self, config: pd.DataFrame) -> None:
        self.conf = config
        self.weight: float
        self.ba: float

    def __str__(self) -> str:
        return (
            f"Compartment Weight:\t{self.weight}\nWith Balance Arm:\t{self.ba}"
        )

    def printComp(self) -> None:
        print(self.conf)

    def printBA(self) -> None:
        print(self.ba)

    def calWeight(self) -> None:
        self.weight = self.conf["WEIGHT"].sum()

    def calBA(self) -> None:
        if self.weight == 0:
            self.ba = self.conf["BA"].mean()
            return

        moment = 0
        for row in self.conf.itertuples():
            moment += row[2] * row[3]
        self.ba = moment / self.conf["WEIGHT"].sum()

    def update_weight_ba(self):
        self.calWeight()
        self.calBA()


class Cargo(Compartment):
    def load(self, weight: float, update_weight=True) -> None:
        if weight > self.conf["MAX"].sum():
            raise ValueError(
                f"Weight of {weight} kg exceeds maximum compartment weight ({self.conf['MAX'].sum()} kg)"
            )

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


class Cabin(Compartment):
    def load(self, pax: int, update_weight=True) -> None:
        if pax > len(self.conf):
            raise ValueError(
                f"Passenger count of {pax} exceeds maximum passengers for compartment ({self.conf.__len__()})"
            )

        paxmass = 84  # KG
        for row in self.conf.itertuples():
            if pax > 0:
                self.conf.loc[row[0], "WEIGHT"] = paxmass
                pax -= 1
            else:
                self.conf.loc[row[0], "WEIGHT"] = 0

        if update_weight:
            self.update_weight_ba()


class Fuel(Compartment):
    def load(self, weight: float, update_weight=True) -> None:
        count = weight
        if weight > self.conf["MAX"].sum():
            raise ValueError(
                f"Weight of {weight} kg exceeds max tank capacity ({self.conf['MAX'].sum()} kg)"
            )

        elif weight >= 2 * self.conf.loc[0, "MAX"]:
            count -= 2 * self.conf.loc[0, "MAX"]
            self.conf.loc[0, "WEIGHT"] = self.conf.loc[0, "MAX"]
            self.conf.loc[1, "WEIGHT"] = self.conf.loc[1, "MAX"]
            self.conf.loc[2, "WEIGHT"] = count

        elif weight < 2 * self.conf.loc[0, "MAX"]:
            count /= 2
            self.conf.loc[0, "WEIGHT"] = count
            self.conf.loc[1, "WEIGHT"] = count
            self.conf.loc[2, "WEIGHT"] = 0

        if update_weight:
            self.update_weight_ba()


@dataclass
class Plane:
    # Dimensions
    # length = lentomet(242,4)
    _OEW = 168682  # KG (NOT FROM KLM AS NO DOCUMENT EXISTS WITH OEW VALUES)
    _BALANCE_ARM = 1180.0  # ESTIMATE INCHES FROM DATUM
    _MOMENT = _OEW * _BALANCE_ARM

    mac: float
    weight: float

    def calBalance(compartments: tuple[Compartment, ...]) -> None:
        weight = Plane._OEW
        moment = Plane._MOMENT
        for comp in compartments:
            weight += comp.weight
            moment += comp.ba * comp.weight

        ba = moment / weight
        Plane.mac = calmac(ba)
        Plane.weight = weight

    # Configuration for B77W
    # Forward Cargo Compartment
    _confFwd = pd.read_csv(r"config/LD-3_FwdCargoComp_KG.csv")
    fwdCarg = Cargo(_confFwd)

    # Aft Cargo Compartment
    _confAft = pd.read_csv(r"config/LD-3_AftCargoComp_KG.csv")
    aftCarg = Cargo(_confAft)
    # Cabin Compartments
    # Business Class
    _config01 = pd.read_csv(r"config/01_CabinBusiness.csv")
    business = Cabin(_config01)

    # Premium Economy and Economy
    _config02 = pd.read_csv(r"config/02_CabinPremPlusEcon.csv")
    econPrem = Cabin(_config02)

    # Economy Overwing
    _config03 = pd.read_csv(r"config/03_CabinOverwing.csv")
    econWing = Cabin(_config03)

    # Economy Rear
    _config04 = pd.read_csv(r"config/04_CabinAft.csv")
    econRear = Cabin(_config04)

    # Fuel
    _confFuel = pd.read_csv(r"config/FuelTanks.csv")
    fuelTank = Fuel(_confFuel)

    COMPARTMENTS = (
        fwdCarg,
        aftCarg,
        business,
        econPrem,
        econWing,
        econRear,
        fuelTank,
    )
