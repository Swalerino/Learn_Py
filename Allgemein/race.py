import random
import math

class Track:
    def __init__ (self, liste):
        self.trackList = liste

    

    def __iter__(self):
        return iter(self.trackList)


class TrackPiece:
    def __init__ (self, difficulty, length, typ):
        self.typ = typ
        self.difficulty = difficulty           # Difficulty steht für den schwirigkeitsgrad eines Segements. Der wert soll später mit dem Fahrerskill und der Aero verrechnet werden um eine Geschwindikeit zu bestimmen
        self.length = length

class Straight(TrackPiece):
    def __init__ (self, lenght):
        difficulty = 1
        super().__init__(difficulty, lenght, typ = 'Gerade')


class Curve(TrackPiece):
    def __init__ (self, radius, angle):
        self.radius = radius

        length = math.pi * radius * angle/180


        difficulty = 600/radius                 # Muss um den Faktor des Winkels erweitert werden. Kurven mit sehr kleinem Winkel ~ Gerade
        if difficulty < 1:
            difficulty = 1

        super().__init__(difficulty, length, typ = 'Kurve')


class Car:
    def __init__ (self, ps, weight):
        #self.brand
        self.driver = 'Schumi'
        self.ps = ps
        self.weight = weight
        self.topSpeed = self.ps**0.5 * 10 + 100


    def carInfo(self):
        print("Das Auto wird von " + self.driver +
            " gefahren und hat " + str(self.ps) +
            " PS, " + str(self.weight) +
            " kg.")
        return True
    
    
    def driveOneLap(self, track):
        lapTime = 0
        speed = self.topSpeed / 3.6      # km/h --> m/s
        for piece in track:
            lapTime += piece.length / (speed / piece.difficulty)


        return lapTime


def randBudgetCar(maxPoints, seed) -> Car:
    if seed is not None:
        random.seed(seed)

    # 1) Punkte zufällig auf n Kategorien verteilen (Summe = max_points)
    power_points = random.randint(0, maxPoints)
    rest = maxPoints - power_points
    light_points = rest
    

    # 2) Werte berechnen
    ps = 400 + power_points * 5
    weight = 1700 - light_points * 5

    return Car(ps, weight)



monza = Track([
    Straight(1400),
    Curve(240, 70),
    Straight(800),
    Curve(50, 100),
    Straight(250),
    Curve(40, 60),
    Straight(1000),
    Curve(200, 45),
    Straight(900),
    Curve(170, 175)])


car1 = randBudgetCar(100, 2)
car1.carInfo()
print(car1.driveOneLap(monza))
print()

car2 = randBudgetCar(100, 1)
car2.carInfo()
print(car2.driveOneLap(monza))
print()

car3 = randBudgetCar(100, 3)
car3.carInfo()
print(car3.driveOneLap(monza))
print()

car4 = randBudgetCar(100, 5)
car4.carInfo()
print(car4.driveOneLap(monza))
print()




