# class Test:
#     def __init__(self,name):
#         self.name=name
#         print("{} - 생성되었습니다.".format(self.name))
#     def __del__(self):
#         print("{} - 파괴되었습니다.".format(self.name))

# #변수에 저장하지 않은경우
# Test("A")
# Test("B")
# Test("C")
# print()

# #변수에 저장한 경우
# a=Test("A")
# b=Test("B")
# c=Test("C")
# print()

import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def get_circumference(self):
#         return 2*math.pi*self.radius
#     def get_area(self):
#         return math.pi*(self.radius**2)

# circle=Circle(10)
# print("원의 둘레 = ",circle.get_circumference())
# print("원의 넓이 = ",circle.get_area())
# print()

# #프라이빗 변수 __변수이름
# class Circle2:
#     def __init__(self,radius):
#         self.__radius=radius
#     def get_circumference(self):
#         return 2*math.pi*self.__radius
#     def get_area(self):
#         return math.pi*(self.__radius**2)

# circle=Circle2(10)
# print("원의 둘레 = ",circle.get_circumference())
# print("원의 넓이 = ",circle.get_area())
# print(circle.__radius)
# print()

#게터/세터
class Circle3:
    def __init__(self,radius):
        self.__radius=radius
    def get_circumference(self):
        return 2*math.pi*self.__radius
    def get_area(self):
        return math.pi*(self.__radius**2)

    def get_radius(self):
        return self.__radius
    def set_radius(self,value):
        self.__radius=value

circle=Circle3(10)
print("원의 둘레와 넓이")
print("원의 둘레 = ",circle.get_circumference())
print("원의 넓이 = ",circle.get_area())
print()
print("__radius접근")
print(circle.get_radius())
print()
circle.set_radius(2)
print("반지름 변경 후 원의 둘레와 넓이")
print("원의 둘레 = ",circle.get_circumference())
print("원의 넓이 = ",circle.get_area())
print()

#상속
class Parent:
    def __init__(self):
        self.value="테스트"
        print("Parent클래스의 __init()__메소드가 호출되었습니다")
    def test(self):
        print("Parent클래스의 test()메소드입니다")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child클래스의 __init()__메소드가 호출되었습니다")

child=Child()
child.test()
print(child.value)