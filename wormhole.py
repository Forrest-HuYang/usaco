"""
ID: tony_hu1
PROG: wormhole
LANG: PYTHON3
"""
def solve(x,y,next_on_right,N,partner):
    total = 0
    for i in range(1,N+1):
        if partner[i] == 0:
            break
    
    if i == N:
        if (cycle_exists(next_on_right,N,partner)):
            return 1
        else:
            return 0

    for j in range(i+1,N+1):
        if partner[j] == 0:
            partner[i],partner[j] = j,i
            total += solve(x,y,next_on_right,N,partner)
            partner[i] = 0 
            partner[j] = 0
    print(partner)
    print(total)
    return total
    

def cycle_exists(next_on_right,N,partner):
    for start in range(1,N+1):
        pos = start
        for count in range(0,N):
            pos = next_on_right[partner[pos]]
        if pos != 0:
            return True
    return False

a = []
with open('wormhole.in') as filename:
    for line in filename:
        a.append(line.rstrip())

x = [0]
y = [0]
index = {}
partner = [0]
next_on_right = [0]
N = int(a[0])
for i in range(1,N+1):
    x.append(int(a[i].split(' ')[0]))
    y.append(int(a[i].split(' ')[1]))
    partner.append(0)
    next_on_right.append(0)
    index[i-1] = 0
print(x)
print(y)


for i in range(1,N+1):
    for j in range(1,N+1):
        if x[j] > x[i] and y[i] == y[j]:
            if (next_on_right[i] == 0 or x[j] < index[i]):
                next_on_right[i] = j
                index[i] = x[j]
print(next_on_right)
mm = solve(x,y,next_on_right,N,partner)
print(mm)


fout = open ('wormhole.out', 'w')
fout.write(str(mm)+'\n')
fout.close()


