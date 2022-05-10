import random

# ===================== Q1.  배수 구하기 =========================
# input 으로 입력값 A와 B를 받아옵니다.
# for 과 while 을 활용해 1이상 B 이하에서 A의 배수를 출력하세요,
# * 한 코드에서 두 문법을 모두 사용하는 것이 아닌 for 로 만든 코드, while 로 만든 코드 두 개를 만듭니다
# * 항상 B > A 입니다.

# 예시)
# 입력값 10 , 200
# for 에서 출력값 10,20,30,40... 200
# while 에서 출력값 10,20,30,40.... 200

A = 2
B = 50
# A=int(input())
# B = int(input())
for a in range(2,3):
    for b in range(1,26):
        print(a*b ,end=" ")
print()

c = 1
while c < 26:
    print(c * 2 ,end=" ")
    c = c+1
print()


# ===================== Q2. 난수 =====================
# 길이 7의 리스트을 지정하고 안에 랜덤한 숫자를 넣습니다.
# 리스트 안에 있는 값들을 모두 출력합니다.
# 다음 줄에서 리스트에 있는 값들의 합을 출력합니다.
# 그 다음 줄에서 리스트의 최소값, 최대값을 출력합니다
# 마지막으로 리스트에 값의 평균을 출력합니다.
# 리스트 안의 값x 는 0 < x < 100을 만족합니다 .

# 예시
# 입력 없음
# 출력
# 21 23 74 56 23 85 25
# 307
# 21 85
# 43.8
l = [12,34,56,78,9,10,13]
for i in range(7):
    l[i] = random.randint(1,99)
print(l[0], l[1], l[2], l[3], l[4], l[5], l[6])
print(l[0] + l[1] + l[2] + l[3] + l[4] + l[5] + l[6])
l.sort()
print("최댓값 = ", l[6])
print("최솟값 =", l[0])
s = l[0] + l[1] + l[2] + l[3] + l[4] + l[5] + l[6]
print("평균값 =", s/7)

# # ===================== Q3. 요일 찾기 =====================
# 변수 3개를 입력 받아옵니다. (x년, y월, z일)
# 서기 1년 1월 1일이 월요일일 때 입력 받아온 날짜의 요일을 구하시오
# 요일을 구할 떄에는 윤년을 고려해야 합니다


# 윤년을 구하는 공식

# - 4로 나누어지는 해는 윤년이다.
# - 100으로 나누어지는 해는 윤년이 아니다.
# - 400으로 나누어지는 해는 윤년이다.
# * datetime 모듈을 사용하지 않고 스스로 만들어야 합니다!!!

# 예시
# 입력값, 2022 04 01
# 출력값 금요일

date = input().split()
day = 0
day2 =0
yyear = 0

for i in range(1,int(date[0])):
    if(i%4 == 0):
        if(i%100 == 0):
            if(i%400 == 0):
                yyear+=1
                day += 366
            else:
                day += 365
        else:
            day += 366
            yyear += 1
    else:
        day += 365



month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


leapyear = False
if (int(date[0]) % 4 == 0):
    if (int(date[0]) % 100 == 0):
        if (int(date[0]) % 400 == 0):
            leapyear = True
        else:
            pass
    else:
        leapyear = True
else:
    pass


if leapyear:
    month[1] = 29
for i in range(int(date[1])-1):
    day2 += month[i]
    print(i,"월")
    print(month[i])
    print(day2)

요일 = ["M", "T","W","TH","F","SA","SU"]

print(day+day2+int(date[2]))
reslut = (day + day2 + int(date[2])-1)%7
print(요일[reslut])


from datetime import datetime, timedelta

time1 = datetime(1, 1, 1)
time2 = datetime(int(date[0]), int(date[1]), int(date[2]))

print(time2-time1) # 9 days, 23:18:54.66662