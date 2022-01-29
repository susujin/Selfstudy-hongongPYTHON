#객체
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
