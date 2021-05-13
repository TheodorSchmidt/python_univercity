class Transport:
    capacity = 0
    def __init__(self, speed, fuel, year):
        print('')
        print('Создан транспорт', end = '')
        self.speed = speed
        self.fuel = fuel
        self.year = year
        Transport.capacity += 1
    def __del__(self):
        Transport.capacity -= 1
    def charact(self):
        print('')
        return "Двигается со скоростью %s км в час, использует %s, выпущен в %s году."  \
               % (self.speed, self.fuel, self.year)
    def get_speed(self):
        return self.speed
    def get_fuel(self):
        return self.fuel
    def get_year(self):
        return self.year
    @staticmethod
    def howMany():
        print("Всего %s транспортных средств" % (Transport.capacity))
class Car(Transport):
    def __init__(self, speed, fuel, year, model, number):
        Transport.__init__(self, speed, fuel, year)
        self.model = model
        self.number = number
        print(' - автомобиль. Номер %s' % (self.number))
    def charact(self):
        return "Автомобиль марки %s с номером %s. " % (self.model, self.number) \
               + Transport.charact(self)
    def drift(self):
        print('')
        print("Машина %s задрифтила, подвеска сломалась и скорость снизилась на 20 км в час" % (self.number))
        self.speed -= 20
    def get_model(self):
        return self.model
    def get_number(self):
        return self.number
class Train(Transport):
    def __init__(self, speed, fuel, year, number, carriage, passenger):
        Transport.__init__(self, speed, fuel, year)
        self.number = number
        self.carriage = carriage
        self.passenger = passenger
        print(' - поезд. Номер %s' % (self.number))
    def charact(self):
        print('')
        return "Поезд №%s, c %s вагонами и %s пассажирами в каждом. " % (self.number, self.carriage, self.passenger) \
                + Transport.charact(self)
    def get_of_the_rails(self):
        print('')
        print('Поезд №%s сошел с рельс и потерял один вагон' % (self.number))
        self.carriage -= 1
    def get_number(self):
        return self.number
    def get_carriage(self):
        return self.carriage
    def get_passenger(self):
        return self.passenger

transp = Transport(100, 'бензин', 1999)
print(transp.charact())
Transport.howMany()
car = Car(150, 'бензин', 2004, 'Ford', 's102hf')
print(car.charact())
car.drift()
print(car.charact())
Transport.howMany()
train = Train(120, 'сургуч', 2008, 10, 12, 40)
print(train.charact())
train.get_of_the_rails()
print(train.charact())
Transport.howMany()