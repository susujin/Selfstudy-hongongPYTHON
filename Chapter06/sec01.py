#조건문 예외처리
input_a=input("정수 입력> ")
if input_a.isdigit(): #숫자로만 구성되어 있다면
    number_input_a=int(input_a)
    print("원의 반지름 : ",number_input_a)
    print("원의 둘레 : ",2*3.14*number_input_a)
    print("원의 넓이 : ",3.14*number_input_a*number_input_a)
else:
    print("정수를 입력하지 않았습니다.")
print()

#try except
try:
    number_input_a=int(input("정수 입력> "))
    print("원의 반지름 : ",number_input_a)
    print("원의 둘레 : ",2*3.14*number_input_a)
    print("원의 넓이 : ",3.14*number_input_a*number_input_a)
except:
    print("잘못되었습니다.")
print()

#try except pass
list_input_a=["52","9","20","스파이","312"]
list_number=[]
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        pass
print("{} 내부에 있는 숫자는 ".format(list_input_a))
print("{}입니다.".format(list_number))
print()

#try except else
try:
    number_input_a=int(input("정수 입력 > "))
except:
    print("정수 아님")
else:
    print("원의 반지름 : ",number_input_a)
    print("원의 둘레 : ",2*3.14*number_input_a)
    print("원의 넓이 : ",3.14*number_input_a*number_input_a)
print()

#finally
try:
    number_input_a=int(input("정수 입력 > "))
    print("원의 반지름 : ",number_input_a)
    print("원의 둘레 : ",2*3.14*number_input_a)
    print("원의 넓이 : ",3.14*number_input_a*number_input_a)
except:
    print("정수 입력하세요!!")
else:
    print("예외가 발생하지 않음.")
finally:
    print("일단 끝")