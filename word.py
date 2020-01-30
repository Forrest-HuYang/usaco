a = []

with open('photo.in') as filename:
    for line in filename:
        a.append(line.rstrip())
no_cows = int(a[0].split(' ')[0])
total_a = 0
total_b = 0
b = a[1].split()
for i in range(no_cows-1):
    b[i] = int(b[i])
    total_b += b[i]
for j in range(1,no_cows+1):
    total_a += i
start_plus_end = total_a*2 - total_b
for k in range(1,min(start_plus_end,no_cows+1)):
    already_done = set()
    already_done.add(k)
    record = []
    record.append(k)
    if not 2*k == start_plus_end:
        current = k
        for l in range(no_cows-1):
            current = b[l] - current
            if (current in already_done) or (current <= 0):
                break
            already_done.add(current)
            record.append(current)
        if l == no_cows-2:
            break

print(record)
fout = open('photo.out','w')
for m in range(no_cows-1):
    fout.write(str(record[m])+' ')
fout.write(str(record[no_cows-1]))
fout.write('\n')
fout.close()

