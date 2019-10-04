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
list_beads = []
total_maximus = 0
str_beads = a[1]
for i in range(len(str_beads)):
    list_beads.append(str_beads[i])
maximus = 0
for i in range(num_beads):
    temp_head = 'n'
    temp_tail = 'n'
    if list_beads[0] == 'w':
        temp_head = list_beads[1]
    if list_beads[num_beads-1] == 'w':
        temp_tail = list_beads[1]
    m = 0
    n = num_beads
    maximus = 0
    while list_beads[m] == list_beads[0] or list_beads[m] == 'w' or list_beads[m] == temp_head:
        maximus += 1
        m += 1
        if m >= num_beads:
            break
    while list_beads[n - 1] == list_beads[num_beads - 1] or list_beads[n - 1] == 'w'or list_beads[n-1] == temp_tail:
        if m == n:
            break
        maximus += 1
        n -= 1
    if maximus > total_maximus:
        total_maximus = maximus
    list_beads.append(list_beads[0])
    del list_beads[0]
fout = open ('beads.out', 'w')
fout.write(str(total_maximus) +'\n')

