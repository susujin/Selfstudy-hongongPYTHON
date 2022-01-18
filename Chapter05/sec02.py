#반복문으로 팩토리얼 구하기
def factorial(n):
    output=1
    for i in range(1,n+1):
        output*=i
    return output

print("1!: ",factorial(1))
print("2!: ",factorial(2))
print("3!: ",factorial(3))
print("4!: ",factorial(4))
print("5!: ",factorial(5))
print()

#재귀함수로 팩토리얼 구하기
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print("1!: ",factorial(1))
print("2!: ",factorial(2))
print("3!: ",factorial(3))
print("4!: ",factorial(4))
print("5!: ",factorial(5))
print()

#재귀함수로 피보나치수열
def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print("fibonacci(1): ",fibonacci(1))
print("fibonacci(2): ",fibonacci(2))
print("fibonacci(3): ",fibonacci(3))
print("fibonacci(4): ",fibonacci(4))
print("fibonacci(5): ",fibonacci(5))
print()

counter=0
def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter
    counter+=1

    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fibonacci(10)
print("---------")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))

#마무리 연습문제 01
