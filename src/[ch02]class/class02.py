class Car:
    """
    Car class
    Author: Minwook Je
    Date:2020.06.08
    """

    # Class (field = Variable)
    car_count = 0

    def __init__(self, company, details):
        self._company = company  # instance variable을 사용할 경우에는 _변수명 is convention
        self._details = details
        # car_count += 1 라고 사용하면 error
        Car.car_count += 1  # Class field

    def __del__(self):
        Car.car_count -= 1

    def __str__(self):
        return 'str: {} : {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} : {}'.format(self._company, self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company, self._details.get('price')))


# Self : instance 변수
car1 = Car("Ferrai", {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car("BMW", {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car("Audi", {'color': 'Silver', 'horsepower': 300, 'price': 3000})
car_list = [car1, car2, car3]

# ID
print(*map(id, car_list))

# dir : override 된 magic method와 method 정보 리스트 형태로 보여줌
# 추가로 Class field (variable) 보여준다.
print(dir(car1))
print(dir(car2))

# __dict__ : dict 형태로 filed 정보 보여줌 ( Class Field는 보여주지 않는다 )
print(car1.__dict__)
print(car2.__dict__)

# Docstring : """ """ 확인
print(Car.__doc__)

# method 실행
for car in car_list: car.detail_info()
# Error : self need
try:
    Car.detail_info()
except:
    print("TypeError: detail_info() missing 1 required positional argument: 'self'")
# Fix Error
Car.detail_info(car1)

# Class
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__))
print(car1.__class__ is car2.__class__)  # id() compare
print(car1.__class__ == car2.__class__)  # value compare

# Class Field access
print(car1.car_count is Car.car_count)
print(car1.car_count == Car.car_count)

# variable scope search
# 인스턴스 namespace에 없으면 상위 scope 검색(__dict__ -> dir)
# 즉, Class Field와 동일한 이름으로 인스턴스 Field를 생성 가능 ( instance scope 검색 후 없을 경우 -> class scope 검색)

