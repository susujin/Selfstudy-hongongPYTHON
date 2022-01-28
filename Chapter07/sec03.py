#모듈 만들기
from flask import request
import sec03_test_module as test

radius=test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))
print()

#모듈이름 출력하는 모듈 만들기
import sec03_module_main

print("메인의__name__출력")
print(__name__)
print()

#모듈 활용하기
import sec03_module_ex as test2
radius=test2.number_input()
print(test2.get_circumference(radius))
print(test2.get_circle_area(radius))
print()

#엔트리 포인트를 확인하는 모듈
import sec03_module_ex as test3
radius=test3.number_input()
print(test3.get_circumference(radius))
print(test3.get_circle_area(radius))
print()

#이미지 읽어 들이고 저장
from urllib import request

target=request.urlopen("https://www.hanbit.co.kr/images/common/logo_hanbit.png")
output=target.read()
print(output)

file=open("output.png","wb")
file.write(output)
file.close()