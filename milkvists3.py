import sys
sys.setrecursionlimit(100000000)
class Cow:
    def __init__(self,mytype):
        self.type = mytype
        self.next = None
        self.group = None
    
    def set_next(self,next):
        if not self.next:
            self.next = [next]
        else: 
            self.next.append(next)
    
    def set_group(self,group):
        self.group = group

class Friend:
    def __init__(self, preference, start, end):
        self.preference = preference
        self.start = start
        self.end = end


def dfs(cow,groupname):
    global cow_list
    if cow.type == groupname[0]:
        cow.set_group(groupname)
    else:
        return

    if cow.next:
        for nextcow in cow.next:
            dfs(cow_list[nextcow],groupname)

a = []
with open('milkvisits.in') as filename:
    for line in filename:
        a.append(line.rstrip())

no_farms = int(a[0].split(' ')[0])
no_friends = int(a[0].split(' ')[1])
cow_types = a[1]
friends_preference = dict()
friends_route = dict()
cow_list = [0]
friend_list = []
for i in range(len(cow_types)):
    cow_list.append(Cow(cow_types[i]))

for j in range(2,no_farms+1):
    temp = a[j].split()
    cow_list[int(temp[0])].set_next(int(temp[1]))

for k in range(no_farms+1,no_farms+1+no_friends):
    temp = a[k].split()
    preference = temp[2]
    start = int(temp[0])
    end = int(temp[1])
    friend_list.append(Friend(preference,start,end))

current_num = 0
for cow in cow_list[1:]:
    if not cow.group:
        current_type = cow.type
        current_group = current_type + str(current_num)
        dfs(cow,current_group)
        current_num += 1

fout = open('milkvisits.out','w')
for friend in friend_list:
    start = cow_list[friend.start].group
    end = cow_list[friend.end].group
    if start == end:
        if start[0] == friend.preference:
            fout.write('1')
        else: 
            fout.write('0')
    else:
        fout.write('1')

fout.write('\n')
fout.close()

