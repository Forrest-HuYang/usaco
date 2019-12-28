"""
ID: tony_hu1
PROG: friday
LANG: PYTHON3
"""
from collections import Counter
with open('friday.in') as f: 
    a = int(f.read())
no_months = 12 * a
index_month = 1
index_year = 1900
index_13 = [6]
no_days_inamonth = []
for i in range(no_months):

    if (index_month <= 7 and index_month % 2 == 1) or (index_month >7 and index_month % 2 == 0):
        no_days_inamonth.append(3)
    elif index_month == 2:
        if (index_year % 4 == 0 and index_year % 100 != 0) or index_year % 400 == 0:
            no_days_inamonth.append(1)
        else:
            no_days_inamonth.append(0)
    else:
        no_days_inamonth.append(2)
    
    index_month += 1

    if index_month == 13:
        index_month = 1
        index_year += 1

for i in range(no_months - 1):
    index_13.append((index_13[i] + no_days_inamonth[i]) % 7)
result = Counter(index_13)
print(result)
fout = open ('friday.out', 'w')
m = str(result[6]) + ' ' + str(result[0])  +' '+ str(result[1]) +' '+ str(result[2]) +' '+ str(result[3]) +' '+ str(result[4]) +' '+ str(result[5]) +'\n'
fout.write(m)