"""
ID: tony_hu1
PROG: sprime
LANG: PYTHON3
"""
import math
def generate_primes(current,primes_last):
    primes_temp = []
    for i in range(len(primes_last)):
        for j in range(4):
            prime = int(str(primes_last[i])+str(primes_possible[j]))
            if is_prime(prime):
                list_primes.append(prime)
                primes_temp.append(prime)
                if current == num_digits:
                    x.append(prime)
    primes_last = primes_temp
    if current < num_digits:
        generate_primes(current+1,primes_last)


def is_prime(num):
    upper = int(math.sqrt(num))
    for i in range(2,upper+1):
        if num%i == 0:
            return False
    return True

a = []
x= []
outstring = '' 
list_primes = [2,3,5,7]
primes_last = [2,3,5,7]
primes_possible = [1,3,7,9]
current = 2
with open('sprime.in') as filename:
    for line in filename:
        a.append(line.rstrip())
num_digits = int(a[0])
generate_primes(current,primes_last)
print(x)
for i in range(len(x)):
    outstring = outstring + str(x[i]) +'\n'
print(outstring)

fout = open ('sprime.out', 'w')
fout.write(outstring)
