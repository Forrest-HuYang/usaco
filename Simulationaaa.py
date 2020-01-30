import random
def generate():
    m = []
    for i in range(6):
        temp = random.randint(1,10)
        list_total.append(temp)
        total += temp
        if temp == 1:
            m.append(False)
        else:
            m.append(True)

    
    if m[0:5].count(True) == 5:
        five_hits += 1
        if not m[5]:
            five_hits_and_miss += 1

total = 0 
list_total = []
five_hits = 0
five_hits_and_miss = 0
for i in range(2000):
    generate()

