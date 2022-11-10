from abc import ABC


class Plant(ABC):
    def SetName(self, name):
        self.name = name

    def SetName(self, latinName):
        self.latinName = latinName

    def SetName(self, genus):
        self.genus = genus

    def __str__(self) -> str:
        return f"Name: {self.name}, Latin Name: {self.latinName}"


class HousePlant(Plant):
    def SetPlacement(self, pot):
        self.pot = pot
