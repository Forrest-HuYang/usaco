"""
ID: tony_hu1
PROG: beads
LANG: PYTHON3
"""
a = []
with open('beads.in') as filename:
    for line in filename:
        a.append(line.rstrip())
num_beads = int(a[0])
list_beads = a[1]*2
bl = [0]*(num_beads*2+1)
rl = [0]*(num_beads*2+1)
br = [0]*(num_beads*2+1)
rr = [0]*(num_beads*2+1)
for i in range(2*num_beads):
    if list_beads[i] == 'w':
        bl[i+1]= bl[i] + 1
        rl[i+1]= rl[i] + 1
    elif list_beads[i] == 'b':
        bl[i+1]= bl[i] + 1
    elif list_beads[i] == 'r':
        rl[i+1]= rl[i] + 1
for i in range(2*num_beads-1,0,-1):
    if list_beads[i] == 'w':
        br[i-1]= br[i] + 1
        rr[i-1]= rr[i] + 1
    elif list_beads[i] == 'b':
        br[i-1]= br[i] + 1
    elif list_beads[i] == 'r':
        rr[i-1]= rr[i] + 1
m = 0
for i in range(2*num_beads):
    x = (max(bl[i+1],rl[i+1])+max(br[i],rr[i]))
    m = max(x,m)
a = min(m,num_beads)
fout = open ('beads.out', 'w')
fout.write(str(a) +'\n')