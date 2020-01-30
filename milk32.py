"""
ID: tony_hu1
PROG: milk3
LANG: PYTHON3
"""

def pour(aa,bb,cc):
    
    ##A->B
    ##if a != 0:
    a,b,c = aa, bb, cc
    b,a  = exchange(a,b,A,B)
    check_state(a,b,c)
    
    ##A->C
    a,b,c = aa, bb, cc
    c,a= exchange(a,c,A,C)
    check_state(a,b,c)

    #B->A, 
    ##if b != 0:
    a,b,c = aa, bb, cc
    a,b = exchange(b,a,B,A)
    check_state(a,b,c)

    #B->C
    a,b,c = aa, bb, cc
    c,b = exchange(b,c,B,C)
    check_state(a,b,c)
    
    ##if c != 0:
    #C->A
    a,b,c = aa, bb, cc 
    a,c = exchange(c,a,C,A)
    check_state(a,b,c)

    a,b,c = aa, bb, cc
    b,c  = exchange(c,b,C,B)
    check_state(a,b,c)



def check_state(a,b,c):
    x = str(a)+' '+str(b)+' '+str(c)
    if not x in tried:
        tried.add(x)
        print(a,b,c)
        if a == 0:
            m.append(c)
        pour(a,b,c)

def exchange(old,new,index1,largest):
    if old + new <= largest:
        #old,new = 0,old + new
        new += old
        old = 0
    else:
        #old,new = old + new - capacity[index2],capacity[index2]
        old = old + new - largest
        new = largest
    return new,old



 



def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')
filein = []
with open('milk3.in') as filename:
    for line in filename:
        filein.append(line.rstrip())

filein = filein[0].split(' ')
A = int(filein[0])
B = int(filein[1])
C = int(filein[2])
capacity = [A,B,C]
m = []
tried = set()
pour(0,0,C)


m.sort()
outstring = ''
for i in range(len(m)-1):
    outstring = outstring + str(m[i]) + ' '
outstring += str(m[len(m)-1])
print(outstring)
write_out('milk3.out',outstring)
