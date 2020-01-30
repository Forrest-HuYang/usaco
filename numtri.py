"""
ID: tony_hu1
PROG: numtri
LANG: PYTHON3
"""
def get_max(row,position):
    current = rows[row][position]
    current_key = str(row)+' '+str(position)
    if current_key in max_record:
        return max_record[current_key]
    if row == num_rows-1:
        max_record[current_key] = current
        return current
    max_record[current_key] = current + max(get_max(row+1,position),get_max(row+1,position+1))
    return max_record[current_key]


max_record = {}
a = []
rows = []
with open('numtri.in') as filename:
    for line in filename:
        a.append(line.rstrip())
num_rows = int(a[0])
for i in range(1,num_rows+1):
    m = []
    b = a[i].split(' ')
    for j in range(len(b)):
        m.append(int(b[j]))
    rows.append(m)

if num_rows > 985:
    for i in range(980):
        get_max(979,i)

total = get_max(0,0)
print (total)

fout = open ('numtri.out', 'w')
x = str(total)+'\n'
fout.write(x)