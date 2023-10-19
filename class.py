

# a = 123
# print(a)
# print(type(a))

# a = 10
# b = 4

# print(a/b)
# print(a//b)

# print("""Hello world!
#       abc
#         def
#             ddd cc""")


# print(len('Python is strong'))


# a = "python is strong, you need python"

# print(a[0:7])
# print(a[-1])
# print(a[-6])
# print(a[:16])
# print(a[18:])
# print(a[:])

# print(a[10:-17])
# print(a[18:-7])


# print("I have %d pens" % 3)
# print("I have %d apples and %d bananas" % (4, 6))


# b=3
# print(f'I have {b} apples')
# print("I have {0} apples and {1} bananas".format(5, 4))

# print(a.count("o"))
# print(a.find("is"))


# print(a.split())
# odd = [1, 3, 5, 7, 9]
# print(type(odd))

# l = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(l[3][:2])

# print([1,2,3]*3)

# l.extend([5, 6])
# l.append([5, 6])
# print(l)


# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = icecream.keys()
# print(ice)
# print(type(ice))

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")


# 상장주식수 = "5,969,782,550"
# print(상장주식수.replace(",", ""))




# money = 3000

# if money >= 3000:
#     print("taxi")
# else:
#     print("walk")


# pocket = ['paper', 'cellphone', 'money', 'card']

# if 'money' not in pocket:
#     print("walk")
# else:
#     print("walk")


# # 백준 오븐 시계(2525)
# a, b = map(int, input().split())
# c = int(input())
# print(((a*60+b+c)//60)%24, (a*60+b+c)%60)


# # 백준 알람 시계(2884)
# h, m = map(int, input().split())
# sum = h*60+m-45
# print(sum//60%24, sum%60)


# score = [90, 25, 67, 45, 80]
# for i in score: 
#     if i >= 80: 
#         print("%d번 학생은 합격입니다." % (score.index(i) + 1))
#     else: 
#         print("%d번 학생은 불합격입니다." % (score.index(i) + 1))


# score = [90, 25, 67, 45, 80]
# for i in score: 
#     if i <= 50: 
#         print("%d번 학생 보충학습입니다" % (score.index(i) + 1))
#     else: 
#         continue


# temp = [i for i in range(11) if (i%2)!=0 ]
# print(temp)
# print(sum(temp))


# coke = 10

# while 1:
#     pay = int(input())

#     if coke <= 0:
#         print("콜라가 다 떨어졌습니다.\n")
#         print("%d원을 돌려드립니다." %pay)
#     elif coke > 0 & pay == 300:
#         print("콜라를 드립니다.")
#     elif coke > 0 & pay > 300:
#         print("콜라를 드립니다.\n")
#         print("잔돈은 %d원입니다" %pay-300)
#     elif pay < 300:
#         print("금액이 부족합니다.\n")
#         print("%d원을 돌려드립니다." %pay)


# member = int(input())
# people = []

# for _ in range(member):
#     age, name = input().split()
#     age = int(age)
#     people.append((age, name))

# people = sorted(people, key=lambda x: x[0])

# for p in people:
#     print(p[0], p[1])


# class Calculator:
#     def __init__(self):
#         self.result = 0
  
#     def add(self, num):
#         self.result += num
#         return self.result
    
#     def sub(self, num):
#         self.result -= num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(1))
# print(cal1.add(2))
# print(cal2.add(3))
# print(cal2.add(4))


# class Calculator:
#     # def setdata(self, num1, num2):
#     #     self.num1 = num1
#     #     self.num2 = num2

#     def __init__(self) -> None:
#         pass

#     def add(self):
#         result = self.num1 + self.num2
#         return result

#     def sub(self):
#         result = self.num1 - self.num2
#         return result
    
        
#     def mul(self):
#         result = self.num1 * self.num2
#         return result
    
        
#     def div(self):
#         result = self.num1 / self.num2
#         return result
    
# a = Calculator()
# a.setdata(3, 2)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())


# import mod1
# print(mod1.add(1, 2))

# import game.sound.echo
# game.sound.echo.echo_test()

# from game.sound import echo
# echo.echo_test()

# from game.sound.echo import echo_test
# echo_test()

# from game.sound import *
# echo.echo_test()


# try:
#     print(1+'b')
# except TypeError:
#     print("Error")

# l = [10, 20, 30]
# try:
#     index, x = map(int, input("input index and num: ").split())
#     print(l[index] / x)
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)



## 코드업(성실한 개미)
# array = []

# for i in range(10):
#     array.append(list(map(int, input().split())))

# x, y = 1, 1

# while True:
#     if (array[x][y] == 0):
#         array[x][y] = 9
#     elif (array[x][y] == 2):
#         array[x][y] = 9
#         break

#     if ((array[x][y+1] == 1 and array[x+1][y] == 1)):
#         break

#     if (array[x][y+1] != 1):
#         y = y + 1
#     elif (array[x+1][y] != 1):
#         x = x + 1

# for i in range(10):
#     for j in range(10):
#         print(array[i][j], end=' ')
#     print()


## 백준 신입 사원(1946)
# import sys
# n = int(sys.stdin.readline())

# for i in range(0, n):
#     nn = int(input())
#     cnt = nn
#     caseList = [] 
#     min = nn + 1

#     for j in range(0, nn):
#         a, b = map(int, sys.stdin.readline().split())
#         caseList.append([a,b])

#     caseList.sort()

#     for j in range(0, nn):
#         if caseList[j][1] < min:
#             min = caseList[j][1]
#         else:
#             cnt -= 1

#     print(cnt)



# 백준 N번째 큰 수(2075)
# import heapq
# import sys

# heap = []
# N = int(sys.stdin.readline())

# for _ in range(N):
#     l = list(map(int, sys.stdin.readline().split()))

#     for i in l:
#         if len(heap) < N : 
#             heapq.heappush(heap, i)
#         elif i > heap[0]:
#             heapq.heappop(heap)
#             heapq.heappush(heap, i)

# print(heapq.heappop(heap))    



# 수행평가 대비
string = "python is strong, you need python"

print(string[10:-17])
print(string[18:-7]) # 출력 값은?

print("%10s" % "hi")
print("%-10s" % "hi")
print("%-10shi" % "teacher")

print("I have %s apples" % 3)

a = 4
b = 6
print("I have %d apples and %d bananas" % (a, b))

print("%0.4f" % 3.42179234) # python은 소수 반올림
print("%10.4f" % 3.42134234)

print("I eat {0} apples".format(3)) # 숫자 바로 대입하기
print("I eat {0} apples".format("five")) # 문자 바로 대입하기

a = 5
print("I eat {0} apples".format(a))

a = 5
b = 4
print("I have {0} apples and {1} bananas".format(a, b))

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

name = "suh"
age = 18
print(f"My name is {name}, my age is {age}")

d = {"name": "suh", "age": 18}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

string = "apple"
print(string.count("p"))

string = "python is very strong"
print(string.find("t"))
print(string.find("is"))
print(string.find("Q"))

string = "python is very strong"
print(string.index("t"))
print(string.index("is"))

print(",".join('abcd'))

string = ",".join(['a', 'b', 'c', 'd'])
print(string)

s1 = "HI"
s2 = "hi"
print(s1.lower())
print(s2.upper())

s1 = "python is very strong"
s2 = s1.replace("python", "my arm")
# s1[4] = "ffgdfg" 문자열은 인덱스로 수정 안 됨
print(s1)
print(s2)

s = "Life is too short"
s1 = s.split()
print(s1)

s = "1:2:3:4:5"
s1 = s.split(":")
print(s1)

odd = [1, 3, 5, 7, 9]
print(odd)
print(type(odd))

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(a,b,c,d,e)

a = [1, 2, 3]
print(a[0])
print(a[1] + a[2])
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[3][2])

a = [1, 2, ['a', 'b', ['Life', 'is']]]
print(a[2][2][0])

a = [1, 2, 3, 4, 5]
print(a[0:2])
b = a[:2]
c = a[2:]
print(b)
print(c)

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])
print(a[3][:2])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

a = [1, 2, 3]
b = a * 3
print(b)

a = [1, 2, 3, 4, 5]
print(len(a))

a = [1, 2, 3]
b = str(a[2]) + "hi"
print(b)

a = [1, 2, 3]
a[2] = 4
print(a)

a = [1, 2, 3, 4, 5]
del a[:3]
print(a)

a = [1, 2, 3]
a.append(4)
print(a)

a.append([5, 6])
print(a)

a = [1, 5, 3, 2, 4]
a.reverse()
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = [1, 2, 3, 4, 5]
i = a.index(3)
print(i)

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a = [1, 2, 3, 4, 5]
print(a.pop()) # 맨 뒤 요소 꺼내고 삭제
print(a.pop())
print(a)

a = [1, 2, 2, 3, 3, 3]
cnt = a.count(2)
print(cnt)

a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)

t1 = () #빈 튜플
t2 = (1, ) # 요소 하나일 때는 무조건 뒤에 콤마 붙이기
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))
print(type(t1))
# 튜플은 절대 삭제/수정 불가
# 소괄호()로 감싸지 않아도 튜플로 인식

t1 = 1, 2, 3, 4
t2 = t1[1:3]
print(t2)

t1 = 1, 2, 3
t2 = 4, 5, 6
t3 = t1 + t2
print(t3)

t1 = 1, 2, 3
t2 = t1 * 3
print(t2)

t1 = (1, 2, 3, 4)
print(len(t1))

d = {"name": "suh", "age": 18, "phone": "010-1234-5678"}
print(type(d))
print(d)

a = {"a": [1, 2, 3]}
print(a)

a = "name"
d = {a:"suh"}
print(d)

d = {1: "a"}
d[2] = "b"
print(d)
d["name"] = "suh"
print(d)

d = {1: "a",2: "b", "name": "suh"}
del d["name"]
print(d)
del d[1]
print(d)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
keys = a.keys() # dict_keys 개체는 리스트처럼 사용할 수 있지만, append/pop/insert/remove/sort 등 함수 사용 불가 
print(keys)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
l = list(a.keys())
print(l)
print(type(l))

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
values = a.values()
print(values)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
items = a.items()
print(items)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.clear()
print(a)

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
is_in1 = 'name' in a
is_in2 = 'height' in a
print(is_in1)
print(is_in2)

s1= set([1,2,3])
print(type(s1))
print(s1)

s2 = set("Hello")
print(type(s2))
print(s2)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = s1 & s2 
# s3 = s1.intersection(s2)
print(s3)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = s1 | s2
# s3 = s1.union(s2)
print(s3)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s3 = s1 - s2
# s3 = s1.difference(s2)
print(s3)

s1 = set([1, 2, 3])
s1.add(4)
print(s1)

s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

s1 = set([1, 2, 3])
s1.remove(2)
print(s1)

# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어 있으면 거짓이고 비어있지 않은 경우 참
a = [1, 2, 3, 4]
while a:
	print(a.pop())
	
print(bool("python"))
print(bool(""))

a = 10
b = 10
print("a is b =", a is b)
print("a == b =", a == b)
print("id(a) =", id(a))
print("id(b) =", id(b))

print("and")
print(1 and 9) 
print(2 and 9)
print(1 and 0) 
print(0 and 1)
print(0 and 0)

print("&")
print(1 & 9)
print(2 & 9) 
print(1 & 0)
print(0 & 1)
print(0 & 0)

print("or")
print(1 or 9) 
print(2 or 9) 
print(1 or 0)
print(0 or 1)
print(0 or 0)

print("|")
print(1 | 9) 
print(2 | 9) 
print(1 | 0)
print(0 | 1) 
print(0 | 0)

print(not(0)) 
print(not(9))

print(~0)
print(~7)

pocket = ["paper", "cellphone", "money"]
if "money" in pocket:
    print("택시 타라")
else:
    print("걸어 가라")

pocket = ['paper', 'cellphone', 'money']
if "money" in pocket:
    pass
else:
    print("걸어 가라")

score = 100
if score >= 80:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 80 else "failure"

list = ['one', 'two', 'three'] 
for i in list: 
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
	print(first, last)
     
score = [90, 25, 67, 45, 80]
for i in score: 
    if i >= 80: 
        print("%d번 학생은 합격입니다." % (score.index(i) + 1))
    else: 
        print("%d번 학생은 불합격입니다." % (score.index(i) + 1))

score = [90, 25, 67, 45, 80]
for i in score: 
    if i >= 80: 
        print("%d번 학생 축하합니다" % (score.index(i) + 1))
    else: 
        continue

sum = 0
for i in range(1, 11):
    if i % 2 == 1:
        sum += i
print(sum)

for i in range(2, 10):
    for j in range(1, 10):
        print("%d X %d = %d    " %(i, j, i*j), end="")
    print("")

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

list1 = [i for i in  range(1, 11)]
print(list1)
list2 = [i for i in list1 if i % 2 == 1]
print(list2)

count = 1
while count <= 10:
    print("나무를 %d번 찍었습니다." % count)
    count += 1
print("나무가 넘어갔습니다.")

coke = 10
while 1:
    money = 800
    if coke == 0:
        print("콜라가 다 떨어졌습니다.")
        print("%d원을 돌려드립니다." % money)
        break
    elif money == 300:
        print("콜라를 드립니다.")
        coke -= 1
        print("남은 콜라의 개수는 %d개 입니다." % coke)
    elif money > 300:
        print("콜라를 드립니다.")
        print("잔돈은 %d원입니다." % (money - 300))
        coke -= 1
        print("남은 콜라의 개수는 %d개 입니다." % coke)
    elif money < 300:
        print("금액이 부족합니다.")
        print("%d원을 돌려드립니다." % money)
        print("남은 콜라의 개수는 %d개 입니다." % coke)

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)

def cal(choice, *args):
    if choice == "pls":
        result = 0
        for i in args:
            result += i
        return result
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
        return result
    else:
        print("pls 또는 mul")
        return
print(cal("pls", 1, 2, 3, 4, 5))
print(cal("mul", 1, 2, 3, 4))

def person(**kwargs):
    print(kwargs)
person(name="suh")
person(name="suh", age = 1, height = 180)

def say_myself(name, age, man=True): # 초기값 설정하려면 매개 변수 중에 제일 끝에 위치해야 함
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
say_myself("suh", 18)

a = 1 
def vartest(): 
    global a 
    a = a + 1
vartest() 
print(a)

add = lambda a, b: a+b
result = add(3, 4)
print(result)

# f = open("새파일.txt", 'w')
# f.close()

# f = open("새파일.txt", 'w', encoding="utf-8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# line = f.readline()
# print(line)
# f.close()

# f = open("새파일.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# f = open("새파일.txt", "r")
# while True:
#     line = f.readline().strip()
#     if line:
#         print(line)
#     else:
#         break
# f.close()

# f = open("새파일.txt", 'r')
# lines = f.readlines()
# print(lines)
# f.close()

# f = open("새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# f = open("새파일.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
#     print(line)
# f.close()

f = open("새파일.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("새파일.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

with open("새파일.txt", "w") as f:
    f.write("Life is too short, you need python")

class Calculator:
    def setdata(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    def div(self):
        result = self.num1 / self.num2
        return result
a = Calculator()
a.setdata(3, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class Person:
    def __init__(self, age, name): # 인스턴스 생성시 넘길 매개변수  # 객체변수 생성
        self.name = name
        self.age = age
    def say_name(self):
        print(self.name)
    def say_age(self):
        print(self.age)
person1 = Person(17, "suh")
person2 = Person(18, "in")
person1.say_name()
person1.say_age()
person2.say_name()
person2.say_age()

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    def div(self):
        result = self.num1 / self.num2
        return result
class MoreCalculator(Calculator):
    def pow(self):
        result = self.num1 ** self.num2
        return result
a = MoreCalculator(3, 2)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print("")
print(a.pow())

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        result = self.num1 + self.num2
        return result
    def sub(self):
        result = self.num1 - self.num2
        return result
    def mul(self):
        result = self.num1 * self.num2
        return result
    # 기존 div메서드
    def div(self):
        result = self.num1 / self.num2
        return result
class SafeCalculator(Calculator):
    # 메서드 오버라이딩 부분
    def div(self):
        if self.num2 == 0:
            return "Can't divide by Zero"
        else:
            result = self.num1 / self.num2
            return result
a = SafeCalculator(4, 0)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())

class Family:
    lastname = "서"
    
a = Family()
a.lastname = "김"
print(a.lastname)

# # mod1.py
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# if __name__ == "__main__": # 다른 파일에서 불러올 땐 실행 안 됨
#     print(add(1, 2))
#     print(sub(4, 3))

# import mod2
# a = mod2.Math()
# print(a.solv(2))

l = [10, 20, 30]
try:
    index, x = map(int, input("input index and num: ").split())
    print(l[index] / x)
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try: # 실행 코드
    x = int(input("input number: "))
    y = 10 / x
except ZeroDivisionError: # 예외 처리
    print("Can't divide by Zero")
else: # 예외 안 나면 실행
    print(y)
finally: # 항상 실행
    print('코드 실행이 끝났습니다.')

def three_multiple():
    x = int(input("3의 배수를 입력하세요: "))
    if x % 3 != 0:  
        raise Exception("3의 배수가 아닙니다.") # 예외 발생
    print(x)
try:
    three_multiple()
except Exception as e:  
    print("예외가 발생했습니다.", e)