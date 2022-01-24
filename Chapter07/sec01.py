#math 모듈
import math
print(math.sin(1))
print(math.floor(2.5))
print()

#from, as구문
from math import sin,cos,tan
print(sin(1))
print(cos(1))
print(tan(1))
print()

import math as m
print(m.sin(1))
print()

#random 모듈
import random
print("random(): ",random.random()) #0.0부터 1.0 사이 float값 
print("uniform(10,20): ",random.uniform(10,20)) #범위 사이 float값
print("randrange(10): ",random.randrange(10)) #0부터 입력값 사이 값을 리턴
print("choice([1,2,3,4,5]): ",random.choice([1,2,3,4,5])) #리스트 안 요소를 랜덤으로 선택
print("shuffle([1,2,3,4,5]): ",random.shuffle([1,2,3,4,5])) #리스트 안 요소를 램덤하게 섞음
print("sample([1,2,3,4,5],k=2): ",random.sample([1,2,3,4,5],k=2)) #리스트 요소중 k개 선택
print()

#sys 모듈
import sys
print(sys.argv)
print("getwindowsversion(): ",sys.getwindowsversion())
print("copyright: ",sys.copyright)
print("version: ",sys.version)
#sys.exit()
print()

#os 모듈
import os
print("현재 운영체제 : ",os.name)
print("현재 폴더 : ",os.getcwd())
print("현재 폴더 내부의 요소 : ",os.listdir())

os.mkdir("hello") #폴더 만들고 
os.rmdir("hello") #제거

with open("original.txt","w") as file: #파일만들고 이름 변경하기
    file.write("hello")
os.rename("original.txt","new.txt")

os.remove("new.txt")

os.system("dir")
print()

#datetime 모듈
import datetime

now=datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")
print()

#time 모듈
import time
print("지금부터 5초동안 정지")
time.sleep(5)
print("프로그램 종료")
print()

#urllib 모듈
from urllib import request
target=request.urlopen("https://google.com")
output=target.read()
print(output)
print()