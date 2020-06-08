class Car:
    """
    Title : Car class
    Author : Minwook Je
    Date : 2020.06.09
    Description : Class, Static, Instance Method
    Lecture_Description : 차량 가격 상승률 per year
    """

    price_per_raise = 1.2

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {} : {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} : {}'.format(self._company, self._details)

    # Instance Method
    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info : {} {}".format(self._company, self._details.get('price')))

    # Instance Method : getter
    # !important: .get()을 사용하는게 error로 인한 stop 방지에 더 좋다.
    # .get()은 default None제공 never raises a KeyError
    # []은 default 제공하지 않기 때문에 raise KeyError
    def get_price(self):
        return "Before Car Price -> company : {}, price: {}".format(self._company, self._details.get('price'))

    # Instance Method : getter after inc
    def get_price_after(self):
        return "Before Car Price -> company : {}, price: {}".format(self._company,
                                                                    self._details.get('price') * Car.price_per_raise)

    # Class Method
    # TODO: @classmethod vs _method() ?
    @classmethod
    def raise_price(cls, per):
        try:
            if per <= 1:
                raise Exception("Please Enter 1 or More")
        except Exception as e:
            print("예외가 발생했습니다 : ", e)
            return

        cls.price_per_raise = per
        print("cal succeeded! price increased {}%".format(cls.price_per_raise))

    # static Method: 유연하게 사용할때 활용 (self, cls와 같은 인자를 받지 않는다)
    # 아직 사용할 필요성에 대해 논쟁의 여지가 많다.
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'BMW':
            return "Ok! This car is {}".format(inst._company)
        return "Sorry, This car is not BMW"

car1 = Car("Ferrai", {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car("BMW", {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car("Audi", {'color': 'Silver', 'horsepower': 300, 'price': 3000})
car_list = [car1, car2, car3]

# Call getter
print(car1.get_price())
print(car1.get_price_after())

# Class Method raise Exception
car1.raise_price((0.8))
car1.raise_price((1.2))

# Staic method : 이런식으로 사용가능한게 유연하다는 뜻이다.
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
print(Car.is_bmw(car3))
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(car3.is_bmw(car3))