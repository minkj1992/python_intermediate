class Car:
    """
    Car class
    Author: Minwook Je
    Date:2020.06.08
    """

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {} : {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} : {}'.format(self._company, self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company,self._details.get('price')))


car1 = Car("Ferrai", {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car("BMW", {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car("Audi", {'color': 'Silver', 'horsepower': 300, 'price': 3000})

car_list = [car1, car2, car3]

# Self : instance 변수

# ID
print(*map(id, car_list))

# dir : override 된 magic method와 method 정보 리스트 형태로 보여줌
print(dir(car1))
print(dir(car2))

# __dict__ : dict 형태로 filed 정보 보여줌
print(car1.__dict__)
print(car2.__dict__)

# Docstring : """ """ 확인
print(Car.__doc__)

# method 실행
for car in car_list: car.detail_info()

# Class
print(car1.__class__, car2.__class__)
print(id(car1.__class__),id(car2.__class__))
print(car1.__class__ is car2.__class__) # id() compare
print(car1.__class__ == car2.__class__) # value compare



