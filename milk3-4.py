"""
ID: tony_hu1
PROG: milk3
LANG: PYTHON3
"""

def pour(aa,bb,cc):
    
    a,b,c = aa, bb, cc
    if a != 0:
        ##A->B
        a,b,c = aa, bb, cc
        b,a  = exchange(a,b,A,B)
        check_state(a,b,c)
        
        ##A->C
        a,b,c = aa, bb, cc
        c,a= exchange(a,c,A,C)
        check_state(a,b,c)

    a,b,c = aa, bb, cc
    if b != 0:
        #B->A, 
        a,b,c = aa, bb, cc
        a,b = exchange(b,a,B,A)
        check_state(a,b,c)

        #B->C
        a,b,c = aa, bb, cc
        c,b = exchange(b,c,B,C)
        check_state(a,b,c)
    
    a,b,c = aa, bb, cc
    if c != 0:
        #C->A
        a,b,c = aa, bb, cc 
        a,c = exchange(c,a,C,A)
        check_state(a,b,c)

        #C->B
        a,b,c = aa, bb, cc
        b,c  = exchange(c,b,C,B)
        check_state(a,b,c)



def check_state(a,b,c):
    x = str(a)+' '+str(b)+' '+str(c)
    if not x in tried:
        tried.add(x)
        print(a,b,c)
        if a == 0:
            result.append(c)
        pour(a,b,c)

def exchange(old,new,index1,largest):
    if old + new <= largest:
        old,new = 0,old + new
    else:
        old,new = old + new - largest,largest
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
result = []
tried = set()
pour(0,0,C)


result.sort()
outstring = ''
for i in range(len(result)-1):
    outstring = outstring + str(result[i]) + ' '
outstring += str(result[len(result)-1])
print(outstring)
write_out('milk3.out',outstring)
