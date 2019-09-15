"""
ID: tony_hu1
PROG: gift1
LANG: PYTHON3
"""
a = []
with open('gift1.in') as filename:
    for line in filename:
        a.append(line.rstrip())
num_friends = int(a[0])
del a[0]
print (a)
money = {}
list_friends = []
for i in range(num_friends):
    money[a[0]] = 0
    list_friends.append(a[0])
    del a[0]
print (money)
print (a)
while len(a) > 0:
    give_data = a[1].split(' ')
    if int(give_data[0]) != 0:
        give_residue = int(give_data[0]) % int(give_data[1])
        give_money = int(give_data[0]) // int(give_data[1])
        money[a[0]] = money[a[0]] - int(give_data[0]) + give_residue
        del a[0]
        del a[0]
        print (a)
        for i in range(int(give_data[1])):
            money[a[0]] += give_money
            del a[0]
    else:
        for i in range(int(give_data[1])+2):
            del a[0]
    print (a)
print (money)
fout = open ('gift1.out', 'w')
for i in range(num_friends):
    name = list_friends[i]
    fout.write(name + ' ' + str(money[name]) +'\n')
    
    