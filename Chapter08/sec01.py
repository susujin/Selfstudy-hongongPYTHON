#객체
from re import S


students=[
    {"name":"홍길동","korean":87,"math":98,"english":88,"science":95},
    {"name":"유관순","korean":92,"math":98,"english":98,"science":90},
    {"name":"이순신","korean":76,"math":96,"english":94,"science":94},
    {"name":"정봉준","korean":98,"math":92,"english":99,"science":93},
    {"name":"윤동주","korean":95,"math":98,"english":93,"science":98},
    {"name":"김홍도","korean":74,"math":88,"english":82,"science":95},
]

print("이름","총점","평균",sep='\t')
for student in students:
    score_sum=student["korean"]+student["math"]+student["english"]+student["science"]
    score_avg=score_sum/4
    print(student["name"],score_sum,score_avg,sep='\t')
print()

#객체를 만드는 함수
def create_student(name,korean,math,english,science):
    return{
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

students=[
    create_student("김가네",98,43,54,87),
    create_student("박가네",93,77,80,95),
    create_student("이가네",78,98,84,62),
    create_student("윤가네",88,83,33,79),
    create_student("정가네",73,55,77,67),
    create_student("구가네",94,80,99,87),
]

print("이름","총점","평균",sep='\t')
for student in students:
    score_sum=student["korean"]+student["math"]+student["english"]+student["science"]
    score_avg=score_sum/4
    print(student["name"],score_sum,score_avg,sep='\t')
print()

#객체를 만드는 함수2
def create_student_2(name,korean,math,english,science):
    return{
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

def student_get_sum(student):
    return student["korean"]+student["math"]+student["english"]+student["science"]

def student_get_average(student):
    return student_get_sum(student)/4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"],student_get_sum(student),student_get_average(student))

students=[
    create_student("토끼",98,43,54,87),
    create_student("여우",93,77,80,95),
    create_student("호랑이",78,98,84,62),
    create_student("사자",88,83,33,79),
    create_student("곰",73,55,77,67),
    create_student("사슴",94,80,99,87),
]
print()

#클래스
class Student:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

students=[
    Student("땅콩",98,43,54,87),
    Student("아몬드",93,77,80,95),
    Student("피스타치오",78,98,84,62),
    Student("해바라기씨",88,83,33,79),
    Student("호두",73,55,77,67),
    Student("브라질너트",94,80,99,87),
]

print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)
print()

#메소드
#클래스 내부에 메소드 선언
class Student2:
    def __init__(self,name,korean,math,english,science):
        self.name=name
        self.korean=korean
        self.math=math
        self.english=english
        self.science=science

    def get_sum(self):
        return self.korean+self.math+self.english+self.science
    
    def get_average(self):
        return self.get_sum()/4
    
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())

students=[
    Student2("복숭아",98,43,54,87),
    Student2("딸기",93,77,80,95),
    Student2("포도",78,98,84,62),
    Student2("귤",88,83,33,79),
    Student2("바나나",73,55,77,67),
    Student2("사과",94,80,99,87),
]

print("이름","총점","평균",sep='\t')
for student in students:
    print(student.to_string())
print()