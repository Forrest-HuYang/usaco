"""
ID: tony_hu1
PROG: ariprog
LANG: PYTHON3
"""



def listing_bisquares(limit):
    bisquare = []
    for i in range(limit+1):
        for j in range(i,limit+1):
            f = i**2 + j**2
            if not bisquare_index[f]:
                bisquare.append(f)
                bisquare_index[f] = True

    return bisquare


def is_bisquare(a,b,bisquare,len_progression,maximum):
    m = a + (len_progression-1)*b
    current = a
    if m > maximum:
        return 2
    for i in range(len_progression-1):
            current += b 
            if not bisquare_index[current]:
                return False

    return True
        
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(outstring)

a = []
with open('ariprog.in') as filename:
    for line in filename:
        a.append(line.rstrip())
possible = []
difference = []
outstring = ''

len_progression = int(a[0])
limit = int(a[1])
maximum = 2*(limit**2)
bisquare_index = [False]*(maximum+1)
bisquare = listing_bisquares(limit)
bisquare.sort()
num_possible = len(bisquare)-1


for i in range(num_possible):
    difference.append(bisquare[i+1]-bisquare[i])
for j in range(num_possible):
    a = bisquare[j]
    if a == bisquare[j-1]:
        break
    difference_current = 0
    for k in range(j,num_possible):
        difference_current += difference[k]
        b = difference_current
        result = is_bisquare(a,b,bisquare,len_progression,maximum)
        if result == 2:
            break
        elif result:
            if not [b,a] in possible:
                possible.append([b,a])

if len(possible) == 0:
    outstring = 'NONE'+'\n'
else:
    possible.sort()
    print(possible)
    for k in range(len(possible)):
        outstring = outstring + str(possible[k][1]) + ' ' + str(possible[k][0]) + '\n'




write_out('ariprog.out',outstring)