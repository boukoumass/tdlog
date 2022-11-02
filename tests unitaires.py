#les armes:
class weapon:
    def __init__(self, ammunitions, range):
        self.ammunitions = ammunitions
        self.range = range
    def fire_at(self, x:float, y:float, z:float):
        print(f"fire at {x,y,z}")
    def getrange(self):
        print(self.range)
Lance_missiles_antisurface=weapon(40,30)
Lance-missiles antiair=weapon(50,40)
Lance-torpilles=weapon(15,20)
Lance_missiles_antisurface.fire_at(2,5,6)
class Vessel:
    def __init__(self, coordinates, weapon, maxhits):
        self.coordinates = coordinates
        self.weapon = weapon
        self.maxhits = maxhits
    def getcoordinates(self):
        return self.coordinates
    def go_to(self,x,y,z):
        return (x,y,z)
    def fire_at(self,x,y,z):
        return (x,y,z)