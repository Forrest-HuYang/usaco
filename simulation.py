import random
import numpy as np
def generate(total,list_total,five_hits,five_hits_and_miss):
    m = []
    for i in range(6):
        temp = random.randint(1,10)
        if temp == 1:
            m.append(False)
        else:
            m.append(True)

    num_hits = m.count(True)
    total += num_hits
    list_total.append(num_hits)
    if m[0:5].count(True) == 5:
        five_hits += 1
        if not m[5]:
            five_hits_and_miss += 1
    
    return [total,list_total,five_hits,five_hits_and_miss]

total = 0 
list_total = []
five_hits = 0
five_hits_and_miss = 0
for i in range(200000):
    result = generate(total,list_total,five_hits,five_hits_and_miss)
    total = result[0]
    list_total = result[1]
    five_hits = result[2]
    five_hits_and_miss = result[3]

print(np.std(list_total))
print(total/1200000)
print(five_hits/200000)
print(five_hits_and_miss/five_hits)
