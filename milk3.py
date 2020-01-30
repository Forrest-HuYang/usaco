"""
ID: tony_hu1
PROG: milk3
LANG: PYTHON3
"""
filein = []
with open('milk3.in') as filename:
    for line in filename:
        filein.append(line.rstrip())

filein = filein[0].split(' ')
a = int(filein[0])
b = int(filein[1])
c = int(filein[2])
list_possibilities = [[[False]*c]*b]*a
m = get_possible(a,b,c)
outstring = ''
for i in range(len(m)-1):
    outstring = outstring + str(m[i]) + ' '
outstring += str(m[len(m)-1])


def get_possible(a,b,c):
    possible = []
    if (a>=b and b>=c) or ( b>=a and a>=c):
        possible.append(0)
        possible.append(c)
        return possible
    if (a>=c and c>=b):
        possible.append(c)
        possible.append(c-b)
        ctemp = b
        while ctemp <= c:
            possible.append(ctemp)
            ctemp += b
        return list(set(possible))
    if (b>=c and c>=a):
        possible.append(c)
        possible.append(0)
        btemp = a
        while btemp <= c:
            possible.append(btemp)
            possible.append(c-btemp)
            btemp += a
        return list(set(possible))
    if (c>=b and b>=a):
        possible.append(c)
        possible.append(c-b)
        if c-b <= a:
            possible.append(b)
        temp = a
        while temp <= b:
            possible.append(c-b+temp)
            temp += a
        temp = a
        while temp <= c and c-temp <= b:
            possible.append(temp)
            temp += a
        temp = a
        while temp <= b:
            possible.append(c-temp)
            temp += a
        possible.sort()
        return list(set(possible))

        




def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')
    print(outstring)

write_out('milk3.out',milk3_main(read_in('milk3.in')))