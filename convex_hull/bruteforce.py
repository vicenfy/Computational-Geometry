import turtle
import random
import time

# 随机生成10个点
f = open('point.txt', 'w')
for i in range(10):
    x = random.randrange(0, 100, 1)
    y = random.randrange(0, 100, 1)
    f.write(str(x) + ',' + str(y) + '\n')
f.close()

point = []

f = open('point.txt')
for i in f:
    try:
        temp = i.split(',')
        x = float(temp[0]); y = float(temp[1])
        point.append((x, y))
    except:
        print('a err')
f.close()

def toTheLeft(p, q, s):
    if p[0]*q[1]+s[0]*p[1]+q[0]*s[1]-s[0]*q[1]-q[0]*p[1]-p[0]*s[1] > 0:
        return True  # if result>0, on the left
    else:
        return False

def isInTriangle(p, q, r, s):
    if toTheLeft(p, q, s) and toTheLeft(q, r, s) and toTheLeft(r, p, s):
        return True
    else:
        return False

for i in range(len(point)):
    for j in range(i+1, len(point)):
        for k in range(j+1, len(point)):
            for s in range(len(point)):
                if isInTriangle(point[i], point[j], point[k], point[s]):
                    print(point[s])
