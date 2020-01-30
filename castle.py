components = []
walls = dict()
total = []
area = 0
done = 0
ew_length = 0
ns_length = 0

def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(filein):
    ew_length = int(filein[0].split(' ')[0])
    ns_length = int(filein[0].split(' ')[1])
    area = ew_length*ns_length
    for i in range(1,ns_length+1):
        total.extend(filein[i].split())
    
    for k in range(area):
        total[k] = int(total[k])
        components.append(0)

    for l in range(area):
        temp = {'n':False,'e':False,'s':False,'w':False}
        current = total[l]
        if current >= 8:
            temp['s'] = True
            current = current%8
        if current >= 4:
            temp['e'] = True
            current = current%4
        if current >= 2:
            temp['n'] = True
            current = current%2
        if current >= 1:
            temp['w'] = True
        walls[l] = temp

    current_component = 0
    while 0 in components:
        current = components.index(0)
        current_component += 1
        components[current] = -2
        flood(current_component,ns_length,ew_length)
    print(components)


    

def flood(current_component,ns_length,ew_length):
    visited = 1
    while not visited == 0:
        visited = 0
        while -2 in components:
            visited += 1
            tbd = components.index(-2)
            components[tbd] = current_component
            temp = walls[tbd]
            if not temp['n']:
                neighbour = get_neighbour_pos(tbd,'n',ns_length,ew_length)
                if components[neighbour] == 0:
                    components[neighbour] = -2
            if not temp['e']:
                neighbour = get_neighbour_pos(tbd,'e',ns_length,ew_length)
                if components[neighbour] == 0:
                    components[neighbour] = -2
            if not temp['s']:
                neighbour = get_neighbour_pos(tbd,'s',ns_length,ew_length)
                if components[neighbour] == 0:
                    components[neighbour] = -2
            if not temp['w']:
                neighbour = get_neighbour_pos(tbd,'w',ns_length,ew_length)
                if components[neighbour] == 0:
                    components[neighbour] = -2


def get_neighbour_pos(current,direction,ns_length,ew_length):
    if direction == 'n':
        return current-ew_length
    elif direction == 'e':
        return current+1
    elif direction == 's':
        return current+ew_length
    else:
        return current-1
    

    

def test(a):
    f = list(a)
    new = ''
    for y in range(len(f)-1):
        new += f[y+1]
    for i in range(len(a)):
        if i == len(a)-1:
            return len(a)
        m = ''
        for j in range(i+1):
            m += f[j]
        if not m in new:
            return i+1
        
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('castle.out',main(read_in('castle.in')))