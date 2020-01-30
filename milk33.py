"""
ID: tony_hu1
PROG: milk3
LANG: PYTHON3
"""
"""
ID: tony_hu1
PROG: milk3
LANG: PYTHON3
"""

def pour1(a,b,c):
    if a != 0:
        temp = exchange(a,b,0,1)
        b,a = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(a,c,0,2)
        c,a = temp[0],temp[1]
        check_state(a,b,c)
    if b != 0:
        temp = exchange(b,a,1,0)
        a,b = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(b,c,1,2)
        c,b = temp[0],temp[1]
        check_state(a,b,c)
    if c != 0:
        temp = exchange(c,a,2,0)
        a,c = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(c,b,2,1)
        b,c = temp[0],temp[1]
        check_state(a,b,c)


def pour2(a,b,c):
    if b != 0:
        temp = exchange(b,a,1,0)
        a,b = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(b,c,1,2)
        c,b = temp[0],temp[1]
        check_state(a,b,c)
    if a != 0:
        temp = exchange(a,b,0,1)
        b,a = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(a,c,0,2)
        c,a = temp[0],temp[1]
        check_state(a,b,c)

    if c != 0:
        temp = exchange(c,a,2,0)
        a,c = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(c,b,2,1)
        b,c = temp[0],temp[1]
        check_state(a,b,c)


def pour3(a,b,c):
    if c != 0:
        temp = exchange(c,a,2,0)
        a,c = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(c,b,2,1)
        b,c = temp[0],temp[1]
        check_state(a,b,c)
    if a != 0:
        temp = exchange(a,b,0,1)
        b,a = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(a,c,0,2)
        c,a = temp[0],temp[1]
        check_state(a,b,c)
    if b != 0:
        temp = exchange(b,a,1,0)
        a,b = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(b,c,1,2)
        c,b = temp[0],temp[1]
        check_state(a,b,c)



def pour4(a,b,c):

    if c != 0:
        temp = exchange(c,a,2,0)
        a,c = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(c,b,2,1)
        b,c = temp[0],temp[1]
        check_state(a,b,c)

    if b != 0:
        temp = exchange(b,a,1,0)
        a,b = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(b,c,1,2)
        c,b = temp[0],temp[1]
        check_state(a,b,c)
    if a != 0:
        temp = exchange(a,b,0,1)
        b,a = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(a,c,0,2)
        c,a = temp[0],temp[1]
        check_state(a,b,c)


def pour5(a,b,c):
    if a != 0:
        temp = exchange(a,b,0,1)
        b,a = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(a,c,0,2)
        c,a = temp[0],temp[1]
        check_state(a,b,c)
    if c != 0:
        temp = exchange(c,a,2,0)
        a,c = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(c,b,2,1)
        b,c = temp[0],temp[1]
        check_state(a,b,c)
    if b != 0:
        temp = exchange(b,a,1,0)
        a,b = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(b,c,1,2)
        c,b = temp[0],temp[1]
        check_state(a,b,c)

def pour6(a,b,c):

    if b != 0:
        temp = exchange(b,a,1,0)
        a,b = temp[0],temp[1]
        check_state(a,b,c,6)
        temp = exchange(b,c,1,2)
        c,b = temp[0],temp[1]
        check_state(a,b,c,6)

    if c != 0:
        temp = exchange(c,a,2,0)
        a,c = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(c,b,2,1)
        b,c = temp[0],temp[1]
        check_state(a,b,c)
    if a != 0:
        temp = exchange(a,b,0,1)
        b,a = temp[0],temp[1]
        check_state(a,b,c)
        temp = exchange(a,c,0,2)
        c,a = temp[0],temp[1]
        check_state(a,b,c)

    

def check_state(a,b,c,index):
    if not list_possibilities[a][b][c]:
        list_possibilities[a][b][c] = True
        if a == 0:
            m.append(c)
        
        pour(a,b,c)

def exchange(old,new,index1,index2):
    if old + new <= capacity[index2]:
        old,new = 0,old + new
    else:
        old,new = old + new - capacity[index2],capacity[index2]
    return new,old



 



def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')
filein = []
with open('milk3.in') as filename:
    for line in filename:
        filein.append(line.rstrip())

filein = filein[0].split(' ')
a = int(filein[0])
b = int(filein[1])
c = int(filein[2])
capacity = [a,b,c]
list_possibilities = [[[False]*20]*20]*20
m = []
check_state(0,0,c,1)
check_state(0,0,c,2)
check_state(0,0,c,3)
check_state(0,0,c,4)
check_state(0,0,c,5)
check_state(0,0,c,6)

m.sort()
outstring = ''
for i in range(len(m)-1):
    outstring = outstring + str(m[i]) + ' '
outstring += str(m[len(m)-1])

write_out('milk3.out',outstring)
