# Chapter02-01

# 1. 리스트 구조
# index를 미리 알고있어야 한다.
# 관리 불
car_company_list = ['Ferrari', 'BMW', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 3000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()
# 2. Nested Dict 구조편
# 코드 반복 지속, 중첩 Collision(키, 덮어씌워짐)
# 성능면에서 나쁘지 않다.
car_dicts = [
    {'car_company': 'Ferrai', 'car_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'BMW', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 3000}}
]

del car_dicts[1]
print(car_dicts)

print()
print()

# 3. class구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car:
    def __init__(self,company,details):
        self._company = company
        self._details = details

    # magic method

    # 사용자 레벨에서 사용
    def __str__(self):
        return 'str: {} : {}'.format(self._company,self._details)

    # deploy 레벨에서 사용 (str 없을 경우 사용)
    def __repr__(self):
        return 'repr: {} : {}'.format(self._company, self._details)


car1 = Car("Ferrai",{'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car("BMW", {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car("Audi",{'color': 'Silver', 'horsepower': 300, 'price': 3000})

print(car1) # str, repr

print(car1.__dict__) # dict 형태로 field 정보 확인

print(dir(car1)) # namespace 확인

car_list = [car1,car2,car3]
print(car_list) # list 안에 있는 class print는 repr로 표현, repr이 없다면 object 단위로 표현된다.


# 명시적으로 repr 사용법
for car in car_list:
    print(repr(car))

