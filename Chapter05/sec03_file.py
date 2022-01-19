#파일처리
file=open("basic.txt","w")
file.write("Hello Python!")
file.close()

#with키워드
#파일 close 자동으로 됨
with open("basic2.txt","w") as file:
    file.write("Hello Python!2")

#read()읽기
with open("basic.txt","r") as file:
    contents=file.read()
print(contents)
print()

#랜덤으로 100명의 키와 몸무게 만들기
import random
hanguls=list("가나다라마바사아자차카타파하")
with open("info.txt","w") as file:
    for i in range(100):
        name=random.choice(hanguls)+random.choice(hanguls)
        weight=random.randrange(40,100)
        height=random.randrange(140,200)
        file.write("{}, {}, {}\n".format(name,weight,height))

#반복문으로 한 줄씩 읽기
with open("info.txt","r") as file:
    for line in file:
        (name,weight,height)=line.strip().split(", ")

        if(not name) or (not weight) or (not height):
            continue
        bmi=int(weight)/((int(height)/100)**2)
        result=""
        if 25<=bmi:
            result="과체중"
        elif 18.5<=bmi:
            result="정상체중"
        else:
            result="저체중"
        
        print('\n'.join(["이름: {}","몸무게: {}","키: {}","bmi: {}","결과: "]).format(name,weight,height,bmi,result))
        print()