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
import heapq
import sys

heap = []
N = int(sys.stdin.readline())

for _ in range(N):
    l = list(map(int, sys.stdin.readline().split()))

    for i in l:
        if len(heap) < N : 
            heapq.heappush(heap, i)
        elif i > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, i)

print(heapq.heappop(heap))    