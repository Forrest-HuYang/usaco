"""
ID
LANG: PYTHON3
"""  
import sys
sys.setrecursionlimit(1000000)
def run(speed,position,max_speed):
    position += speed
    if position >= length:
        return
    p.append(1)
    deceleration_stable = plus(max_speed,speed)
    deceleration_plus = plus(max_speed,speed+1)
    deceleration_minus = plus(max_speed,speed-1)
    distance_left = length - position
    if deceleration_plus <= distance_left:
        run(speed+1,position,max_speed)
    elif deceleration_stable <= distance_left:
        run(speed,position,max_speed)
    elif deceleration_minus <= distance_left:
        run(speed-1,position,max_speed)
    
    return
    



def plus(max_speed,x):
    if max_speed >= x:
        return 0
    total = 0
    for i in range(max_speed,x+1):
        total += i
    return total


a = []
record = []
with open('race.in') as filename:
    for line in filename:
        a.append(line.rstrip())
length = int(a[0].split(' ')[0])
different_x = int(a[0].split(' ')[1])
finish_speed_list = list()
for i in range(different_x):
    p = []
    run(0,0,int(a[i+1]))
    record.append(len(p))

fout = open ('race.out', 'w')
for j in range(different_x):
    fout.write(str(record[j]) + '\n')