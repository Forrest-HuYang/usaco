def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(instring):
    l = []
    r = []
    p = {}
    a = instring[0].split(' ')
    num_cows = int(a[0])
    num_rotates = int(a[1])
    num_times = int(a[2])
    cow_list = list(range(num_cows))
    final = {}
    
    for i in range(1,num_rotates+1):
        temp = instring[i].split(' ')
        l.append(int(temp[0])-1)
        r.append(int(temp[1])-1)
    for j in range(num_cows):
        p[j] = j
        for k in range(num_rotates):
            if(p[j] >= l[k] and p[j] <= r[k]):
                p[j] = r[k] + l[k] - p[j]

    remaining = {}

    for i in range(num_cows):
        original = i
        current = i
        is_cycle = False
        times_done = 0
        while times_done < num_times and not is_cycle:
            new = p[current]
            current = new
            times_done += 1
            if current == original:
                is_cycle = True
                remaining[i] = num_times%times_done
        if not is_cycle:
            final[current]  = original
        
    for element in remaining:
        tbd = remaining[element]
        if tbd == 0:
            final[element] = element
        else:
            current = element
            for i in range(tbd):
                current = p[current]
            final[current] = element
            
            
            



    print('shit')

main(read_in('swap.in'))