def tree(current_index,current_group,g_index,h_index):
    if current_index == no_farms-1:
        temp = roads[current_index-1]
        start = int(temp[0])
        end = int(temp[1])
        if type_cows[end] == current_group[0]:
            group[end] = current_group
        return

        if type_cows[end] == 'G':
            groupname = 'G' + str(g_index)
        else:
            groupname = 'H' + str(h_index)
            group[end] = groupname

    temp = roads[current_index]
    start = int(temp[0])
    end = temp[1]
    if start in already_done:
        tree(current_index+1,group[start],g_index,h_index)
        return
    already_done.add(start)

    if type_cows[start] == current_group[0]:
        group[start] = current_group
        tree(current_index+1,current_group,g_index,h_index)
        return

    if type_cows[start] == 'G':
        groupname = 'G' + str(g_index)
        g_index += 1
    else:
        groupname = 'H' + str(h_index)
        h_index += 1
        group[start] = groupname
    
    tree(current_index+1,groupname,g_index,h_index)

a = []
with open('milkvisits.in') as filename:
    for line in filename:
        a.append(line.rstrip())

no_farms = int(a[0].split(' ')[0])
no_friends = int(a[0].split(' ')[1])
type_cows = dict()
cows = a[1]
friends_preference = dict()
roads = []
friends_route = dict()
already_done = set()
group = dict()
h_index = 0
g_index = 0
for i in range(1,len(cows)+1):
    type_cows[i] = cows[i-1]

for j in range(2,no_farms+1):
    temp = a[j].split()
    roads.append([temp[0],temp[1]])

for k in range(no_farms+1,no_farms+1+no_friends):
    temp = a[k].split()
    friends_preference[k-no_farms] = temp[2]
    friends_route[k-no_farms] = [temp[0],temp[1]]

tree(0,'N',g_index,h_index)



print(group)

        
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')