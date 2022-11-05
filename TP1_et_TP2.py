#les armes classe mère qui représente une arme de manière générale:
from math import *
class Weapon:
    def __init__(self):
        self.ammunitions = 5
        self.range = 0
        
    def fire_at(self, x:float, y:float, z:float):
        if self.ammunitions==0:
            raise Exception('NoammunitionError')
        else:
            print(f"fire at {x,y,z}")
            self.ammunitions-=1
            print(self.ammunitions)
            
        
        
        
            
class Lance_missiles_antisurface(Weapon):
    def __init__(self):
        # Sans super
        # Employee.__init__(self, name=name, surname=surname)
        super().__init__()
        self.ammunitions=40
        self.range=30
        
    def fire_at(self, x, y, z):
        if self.ammunitions==0:
            raise Exception('NoammunitionError')
        elif z!=0:
            raise Exception('OutOfRangeError')
            self.ammunitions-=1
        
        else:
            super().fire_at(x, y, z)
class Lance_missiles_antiair(Weapon):
    def __init__(self):
        # Sans super
        # Employee.__init__(self, name=name, surname=surname)
        super().__init__()
        self.ammunitions=50
        self.range=40
        self.p=5
    def fire_at(self, x, y, z):
        if self.ammunitions==0:
            raise Exception('NoammunitionError')
        elif z <= 0:
            raise Exception('OutOfRangeError')
            self.ammunitions-=1
        else:
            super().fire_at(x, y, z)
class Lance_torpilles(Weapon):
    def __init__(self):
        # Sans super
        # Employee.__init__(self, name=name, surname=surname)
        super().__init__()
        self.ammunitions=15
        self.range=20
       
        
    def fire_at(self, x, y, z):
        if self.ammunitions==0:
            raise Exception('NoammunitionError')
        elif z>0:
            raise Exception('OutOfRangeError')
            self.ammunitions-=1
        else:
            super().fire_at(x, y, z)
            
laceur1=Lance_torpilles() 
laceur1.fire_at(2,3,-5)  

class Vessel:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.weapon = Lance_torpilles()
        self.maxhits = 0
    def go_to(self,x:float, y:float, z:float):
        self.coordinates=(x,y,z)
        print(f" aller à {x,y,z}")
    def getcoordinates(self):
        print(self.coordinates)
    def fire_at(self,x:float, y:float, z:float):
        self.weapon.fire_at(x, y, z)



class Cruiser(Vessel):
    def __init__(self, coordinates):
        super().__init__(coordinates)
        self.coordinates = coordinates
        self.weapon = Lance_missiles_antiair()
        self.maxhits =  6 
    def go_to(self,x:float, y:float, z:float):
        if z!=0:
            raise Exception('CoordinatesNotValid')
        else:
            super().go_to(x, y, z)
    def fire_at(self, x, y, z):
        if self.maxhits==0:
            raise Exception('DestroyedError')
        r=sqrt((x-self.coordinates[0])**2+(y-self.coordinates[1])**2+(z-self.coordinates[2])**2)
        #print(r)
        if r>self.weapon.range:
            raise Exception('OutOfRangeError')
            self.weapon.ammunitions-=1
        else:
            self.weapon.fire_at(x, y, z)
class Submarine(Vessel):
    def __init__(self, coordinates: tuple):
        super().__init__(coordinates)
        self.coordinates = coordinates
        self.weapon = Lance_torpilles()
        self.maxhits =  2 
    def go_to(self,x:float, y:float, z:float):
        if z!=0 and z!=-1:
            raise Exception('CoordinatesNotValid')
        else:
            super().go_to(x, y, z)
    def fire_at(self, x, y, z):
        if self.maxhits==0:
            raise Exception('DestroyedError')
        r=sqrt((x-self.coordinates[0])**2+(y-self.coordinates[1])**2+(z-self.coordinates[2])**2)
        #print(r)
        if r>self.weapon.range:
            raise Exception('OutOfRangeError')
            self.weapon.ammunitions-=1
        else:
            self.weapon.fire_at(x, y, z)
class Fregate(Vessel):
    def __init__(self, coordinates: tuple):
        super().__init__(coordinates)
        self.coordinates = coordinates
        self.weapon = Lance_missiles_antisurface()
        self.maxhits =  5
    def go_to(self,x:float, y:float, z:float):
        if z!=0:
            raise Exception('CoordinatesNotValid')
        else:
            super().go_to(x, y, z)
    def fire_at(self, x, y, z):
        if self.maxhits==0:
            raise Exception('DestroyedError')
        r=sqrt((x-self.coordinates[0])**2+(y-self.coordinates[1])**2+(z-self.coordinates[2])**2)
        #print(r)
        if r>self.weapon.range:
            raise Exception('OutOfRangeError')
            self.weapon.ammunitions-=1
        else:
            self.weapon.fire_at(x, y, z)
class Destroyer(Vessel):
    def __init__(self, coordinates: tuple):
        super().__init__(coordinates)
        self.coordinates = coordinates
        self.weapon = Lance_torpilles()
        self.maxhits =  4
    def go_to(self,x:float, y:float, z:float):
        if z!=0:
            raise Exception('CoordinatesNotValid')
        else:
            super().go_to(x, y, z)
    def fire_at(self, x, y, z):
        if self.maxhits==0:
            raise Exception('DestroyedError')
        r=sqrt((x-self.coordinates[0])**2+(y-self.coordinates[1])**2+(z-self.coordinates[2])**2)
        #print(r)
        if r>self.weapon.range:
            raise Exception('OutOfRangeError')
            self.weapon.ammunitions-=1
        else:
            self.weapon.fire_at(x, y, z)
class Aircraft(Vessel):
    def __init__(self, coordinates: tuple):
        super().__init__(coordinates)
        self.coordinates = coordinates
        self.weapon = Lance_missiles_antisurface()
        self.maxhits =  1
    def go_to(self,x:float, y:float, z:float):
        if z!=1:
            raise Exception('CoordinatesNotValid')
        else:
            super().go_to(x, y, z)
    def fire_at(self, x, y, z):
        if self.maxhits==0:
            raise Exception('DestroyedError')
        r=sqrt((x-self.coordinates[0])**2+(y-self.coordinates[1])**2+(z-self.coordinates[2])**2)
        #print(r)
        if r>self.weapon.range:
            raise Exception('OutOfRangeError')
            self.weapon.ammunitions-=1
        else:
            self.weapon.fire_at(x, y, z)
        
d=Cruiser((2,3,0))
d.go_to(3, 3, 0) 
d.fire_at(1, 1, 1)    
A=Aircraft((2,3,0))
A.go_to(3, 3, 1) 
A.fire_at(1, 1, 1)
B=Destroyer((2,3,0))
B.go_to(3, 3, 0) 
B.fire_at(1, 1, 1)
c=Fregate((2,3,0))
c.go_to(3, 3, 0) 
c.fire_at(1, 1, 1)
e=Submarine((2,3,0))
e.go_to(3, 3, 0) 
e.fire_at(1, 1, 1)
        
    
        