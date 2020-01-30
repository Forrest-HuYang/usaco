"""
ID: tony_hu1
PROG: pprime
LANG: PYTHON3
"""
import math
def generate_primes(smallest,largest):
    outstring = ''
    if smallest == 5:
        outstring = '5\n'
    odd = {0,2,4,5,6,8}
    for i in range(smallest,largest+1):
        if not i in odd:
            if is_pal(i):
                if is_prime(i):
                    outstring = outstring + str(i) +'\n'
    return outstring

def generate_pals(smallest,largest):
    outstring = ''
    if smallest == 5:
        outstring += '5\n'
    if smallest <= 7:
        outstring += '7\n'
    if smallest <= 99 and largest >= 10:
        for i in range(1,10,2):
            if (not i == 5) and (not i == 9):
                x = 10*i+i
                if smallest <= x <= largest:
                    if is_prime(x):
                        outstring = outstring + str(x) +'\n'

    if smallest <= 999 and largest >= 100:
        for j in range(1,10,2):
            if not j == 5:
                for k in range(10):
                    x = 100*j + 10*k + j
                    if smallest <= x <= largest:
                        if is_prime(x):
                            outstring = outstring + str(x) +'\n'

    if smallest <= 9999 and largest >= 1000:
        for l in range(1,10,2):
            if not l == 5:
                for m in range(10):
                    x = 1000*l + +100*m + 10*m + l
                    if smallest <= x <= largest:
                        if is_prime(x):
                            outstring = outstring + str(x) +'\n'

    if smallest <= 99999 and largest >= 10000:
        for n in range(1,10,2):
            if not n == 5:
                for o in range(10):
                    for p in range(10):
                        x = 10000*n + 1000*o +100*p + 10*o + n
                        if smallest <= x <= largest:
                            if is_prime(x):
                                outstring = outstring + str(x) +'\n'

    if smallest <= 999999 and largest >= 100000:
        for q in range(1,10,2):
            if not q == 5:
                for r in range(10):
                    for s in range(10):
                        x = 100000*q + 10000*r + 1000*s +100*s + 10*r + q
                        if smallest <= x <= largest:
                            if is_prime(x):
                                outstring = outstring + str(x) +'\n'

    if smallest <= 9999999 and largest >= 1000000:
        for t in range(1,10,2):
            if not t == 5:
                for u in range(10):
                    for v in range(10):
                        for w in range(10):
                            x = 1000000*t +100000*u + 10000*v + 1000*w +100*v + 10*u + t
                            if smallest <= x <= largest:
                                if is_prime(x):
                                    outstring = outstring + str(x) +'\n'

    return outstring


def is_prime(num):  
    upper = int(math.sqrt(num))
    for i in range(2,upper+1):
        if num%i == 0:
            return False
    return True

def is_pal(num):
    num = str(num)
    x = len(num)
    for i in range(x//2):
        if not num[i]==num[x-1-i]:
            return False
    return True

a = []
x= []

with open('pprime.in') as filename:
    for line in filename:
        a.append(line.rstrip())
smallest = int(a[0].split(' ')[0])
largest = int(a[0].split(' ')[1])
outstring = generate_pals(smallest,largest)
print(outstring)
fout = open ('pprime.out', 'w')
fout.write(outstring)
