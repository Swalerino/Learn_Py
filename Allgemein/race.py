import random
import math

class track:
    def __init__ (self, liste):
        self.trackList = liste


class trackPiece:
    def __init__ (self, difficulty, length, typ):
        self.typ = typ
        self.difficulty = difficulty           # Difficulty steht für den schwirigkeitsgrad eines Segements. Der wert soll später mit dem Fahrerskill und der Aero verrechnet werden um eine Geschwindikeit zu bestimmen
        self.length = length

class straight(trackPiece):
    def __init__ (self, lenght):
        difficulty = 1
        super().__init__(difficulty, lenght, typ = 'Gerade')


class curve(trackPiece):
    def __init__ (self, radius, angle):
        self.radius = radius

        length = math.pi * radius * angle/180


        difficulty = 100/radius
        if difficulty < 1:
            difficulty = 1

        super().__init__(difficulty, length, typ = 'Kurve')




class car:
    def __init__ (self, ps, weight):
        #self.brand
        self.driver = 'Schumi'
        self.ps = ps
        self.weight = weight


    def carInfo(self):
        print("Das Auto wird von " + self.driver +
            " gefahren und hat " + str(self.ps) +
            " PS, " + str(self.weight) +
            " kg.")
        return True


def randBudgetCar(maxPoints, seed) -> car:
    if seed is not None:
        random.seed(seed)

    # 1) Punkte zufällig auf n Kategorien verteilen (Summe = max_points)
    power_points = random.randint(0, maxPoints)
    rest = maxPoints - power_points
    light_points = rest
    

    # 2) Werte berechnen
    ps = 400 + power_points * 5
    weight = 1700 - light_points * 5

    return car(ps, weight)


car1 = randBudgetCar(100, 1)
car1.carInfo()

car2 = randBudgetCar(100, 2)
car2.carInfo()

car3 = randBudgetCar(100, 3)
car3.carInfo()

car4 = randBudgetCar(100, 5)
car4.carInfo()



