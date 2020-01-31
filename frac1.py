"""
ID: tony_hu1
PROG: frac1
LANG: PYTHON3
"""
val_keys = [0,1]
fractions = {0:'0/1',1:'1/1'}

with open('frac1.in') as filename:
    for line in filename:
        denominator_max = int(line)

for denominator in range(2,denominator_max+1):
    for numerator in range(1,denominator):
        frac_value = numerator/denominator
        if not frac_value in val_keys:
            val_keys.append(frac_value)
            fractions[frac_value] = str(numerator) +'/' + str(denominator)

val_keys.sort()
fout = open('frac1.out', 'w')
for i in range(len(val_keys)):
    fout.write(fractions[val_keys[i]]+'\n')



