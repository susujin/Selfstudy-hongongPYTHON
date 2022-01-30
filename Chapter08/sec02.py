#isinstance()
class Student:
    def study(self):
        print("공부를 합시다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

classroom=[Student(),Student(),Teacher(),Student(),Student()]

for person in classroom:
    if isinstance(person,Student):
        person.study()
    elif isinstance(person,Teacher):
        person.teach()
print()

#__str__
class Student2:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
    
    def get_sum(self):
        return self.korean+self.english+self.math+self.science
    def get_avg(self):
        return self.get_sum()/4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_avg())
    
students2=[
    Student2("김순이",98,65,77,87),
    Student2("고현정",38,95,74,76),
    Student2("양동이",83,88,89,100),
    Student2("박우니",98,65,40,99),
    Student2("이하윤",98,100,77,54),
    Student2("정예진",95,62,73,87),
]

print("이름","총점","평균",sep='\t')
for s in students2:
    print(str(s))
print()

#크기 비교 함수
class Student3:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
    
    def get_sum(self):
        return self.korean+self.english+self.math+self.science
    def get_avg(self):
        return self.get_sum()/4
    
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_avg())
    
    def __eq__(self, value):
        return self.get_sum()==value.get_sum()
    def __ne__(self, value):
        return self.get_sum()!=value.get_sum()
    def __gt__(self, value):
        return self.get_sum()>value.get_sum()
    def __ge__(self, value):
        return self.get_sum()>=value.get_sum()
    def __lt__(self, value):
        return self.get_sum()<value.get_sum()
    def __le__(self, value):
        return self.get_sum()<=value.get_sum()

students3=[
    Student3("김순이",98,65,77,87),
    Student3("고현정",38,95,74,76),
    Student3("양동이",83,88,89,100),
    Student3("박우니",98,65,40,99),
    Student3("이하윤",98,100,77,54),
    Student3("정예진",95,62,73,87),
]

st_a=Student3("고현정",38,95,74,76)
st_b=Student3("정예진",95,62,73,87)

print("st_a==st_b : ",st_a==st_b)
print("st_a!=st_b : ",st_a!=st_b)
print("st_a>st_b : ",st_a>st_b)
print("st_a>=st_b : ",st_a>=st_b)
print("st_a<st_b : ",st_a<st_b)
print("st_a<=st_b : ",st_a<=st_b)
print()

#클래스변수
class Student4:
    count=0

    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

        Student4.count+=1
        print("{}번째 학생이 생성되었습니다.".format(Student4.count))

students4=[
    Student4("정수정",98,65,77,87),
    Student4("하수연",38,95,74,76),
    Student4("김지현",83,88,89,100),
    Student4("연세인",98,65,40,99),
    Student4("강지민",98,100,77,54),
    Student4("원서운",95,62,73,87),
]
print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student4.count))
print()

#클래스 함수
class Student5:
    count=0
    students=[]

    @classmethod
    def print(cls):
        print("---------학생목록---------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("-------------------------")

    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science
        Student5.count+=1
        Student5.students.append(self)

    def get_sum(self):
        return self.korean+self.english+self.math+self.science
    def get_avg(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_avg())

Student5("고현정",38,95,74,76)
Student5("양동이",83,88,89,100)
Student5("박우니",98,65,40,99)
Student5("김지현",83,88,89,100)
Student5("연세인",98,65,40,99)
Student5("강지민",98,100,77,54)
Student5("원서운",95,62,73,87)
Student5("김순이",98,65,77,87)
Student5("정수정",98,65,77,87)
Student5("하수연",38,95,74,76)
Student5("이하윤",98,100,77,54)
Student5("정예진",95,62,73,87)

Student5.print()
print()