#les armes classe mère qui représente une arme de manière générale:
class Weapon:
    def __init__(self, ammunitions: int, range: int):
        self.ammunitions = ammunitions
        self.range = range
    def fire_at(self, x:float, y:float, z:float):
        print(f"fire at {x,y,z}")
    def getrange(self):
        print(self.range)
Lance_missiles_anti_surface=Weapon(40,30)
Lance_missiles_anti_air=Weapon(50,40)
Lance_torpilles=Weapon(15,20)
Lance_missiles_anti_surface.fire_at(2,5,6)
# Les vaisseaux :classe mère qui représente un vaisseau de manière générale :
class Vessel:
    def __init__(self, coordinates: tuple, maxhits: int ,weapon: Weapon, ):
        self.coordinates = coordinates
        self.weapon = Weapon
        self.maxhits = maxhits
    def go_to(self,x:float, y:float, z:float):
        print(f" aller à {x,y,z}")
    def getcoordinates(self):
        print(self.coordinates)
    def fire_at(self,x:float, y:float, z:float):
        print(f"fire at {x,y,z}")
Cruiser=Vessel((2,3,4),6,Lance_missiles_anti_air)
Submarine=Vessel((2,3,4),2,Lance_torpilles)
Fregate=Vessel((2,3,4),5,Lance_missiles_anti_surface)
Destroyer=Vessel((2,3,4),4,Lance_torpilles)
Aircraft=Vessel((2,3,4),1,Lance_missiles_anti_surface)