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
bl = [0]
rl = [0]
br = [0]
rr = [0]
for i in range(2*num_beads):
    if list_beads[i] == 'w':
        bl.append(bl[i]+1)
        rl.append(rl[i]+1)
    else:
        if list_beads[i] == 'b':
            bl.append(bl[i]+1)
        else:
            bl.append(0)
        if list_beads[i] == 'r':
            rl.append(rl[i]+1)
        else:
            rl.append(0)

    if list_beads[2*num_beads-1-i] == 'w':
        br.append(br[i]+1)
        rr.append(rr[i]+1)
    else:
        if list_beads[2*num_beads-1-i] == 'b':
            br.append(br[i]+1)
        else:
            br.append(0)
        if list_beads[2*num_beads-1-i] == 'r':
            rr.append(rr[i]+1)
        else:
            rr.append(0)
m = 0
for i in range(2*num_beads):
    x = (max(bl[i+1],rl[i+1])+max(br[2*num_beads-1-i],rr[2*num_beads-1-i]))
    m = max(x,m)
a = min(m,num_beads)
print(bl)
print(rl)
print(br)
print(rr)
fout = open ('beads.out', 'w')
fout.write(str(a) +'\n')