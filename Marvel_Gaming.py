
class MarvelHero:
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power
    def Vurus(self):
        return self.power
    def HealthCare(self,power):
        self.health -= power
        return self.health

class DeadPool(MarvelHero):
    def __init__(self,name,health,power):
        MarvelHero.__init__(self,name,health,power)
        self.dayanıklılık = 0 
    def Vurus(self):
        for item in range(0,100):
            self.dayanıklılık += 1
            if (self.dayanıklılık % 5 ==0):
                return self.power*3
            else:
                return self.power
    def HealthCare(self,power):
        self.health -= power
        return self.health
class Hulk(MarvelHero):
    def __init__(self,name,health,power):
        MarvelHero.__init__(self,name,health,power)
        self.vurussayisi = 0
    def Vurus(self):
        for item in range(0,200):
            self.vurussayisi +=1
            if (self.vurussayisi % 3 == 0):
                return self.power *2
            else:
                return self.power
    def HealthCare(self,power):
        self.health -= power
        return self.health   

P1 = Hulk("CaptanAmerica",1100,50)
P2 = DeadPool("Deadpool",1750,100)

list = [Hulk,DeadPool]

print(f"Player1 icin {P2.name} secildi, Player2 icin {P1.name} secildi.")

while (P2.health > 0 and P1.health > 0):
    P1.HealthCare(P2.Vurus())
    print(f"{P1.name}, {P2.name}'e vurdu ==> {P1.name}:{P1.health} ve {P2.name}:{P2.health} ")
    P2.HealthCare(P1.Vurus())
    print(f"{P2.name}, {P1.name}'e vurdu ==> {P2.name}:{P2.health} ve {P1.name}:{P1.health} ")
else:
    print("Game over.")

    
