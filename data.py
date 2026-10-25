def calmac(ba: float) -> float:
    return ((ba-1174.5) * 100.0) / 278.5

def calba(mac: float) -> float:
    return ((mac*278.5) / 100) + 1174.5

def calmom(weight:float, ba: float) -> float:
    return weight * ba