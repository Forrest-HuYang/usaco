"""
ID: tony_hu1
PROG: milk2
LANG: PYTHON3
"""


a = []
m=[]
total = []
with open('milk2.in') as filename:
    for line in filename:
        a.append(line.rstrip())
num_cows = int(a[0])
for i in range(num_cows):
    b = a[i+1].split(' ')
    m.append(int(b[0]))
    m.append(int(b[1]))
    total.append(m)
    m = []
time = []
print(total)
def is_sorted(record):
    for i in range(len(record)-1):
        b1 = record[i+1][0]
        b2 = record[i][1]
        if b1 <= b2:
            return False
    return True

total.sort()
while is_sorted(total) == False:
    time= [[0,0]]
    for i in range(len(total)):
        a = total[i][0]
        b =time[len(time)-1][0]
        c =time[len(time)-1][1]
        judgement = (a >= b )and (a <= c)
        if judgement:
            period = [time[len(time)-1][0],max(total[i][1],time[len(time)-1][1])]
            time[len(time)-1] = period
        else:
            time.append(total[i])
    if time[0]==[0,0]:
        del time[0]
    total = time
print(time)
no_cows = 0
for i in range(len(total)-1):
    x = total[i+1][0] - total[i][1]
    no_cows = max(no_cows,x)
cows = 0
for i in range(len(total)):
    x = total[i][1] - total[i][0]
    cows = max(cows,x)



fout = open ('milk2.out', 'w')
a = str(cows) + ' ' + str(no_cows)+'\n'
fout.write(a)