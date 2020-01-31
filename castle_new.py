"""
ID: tony_hu1
PROG: castle
LANG: PYTHON3
"""
a = []
roomsize = dict()
rooms = []
m = 0
room_area = []

def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(filein):
    global ns_length
    global ew_length

    global a
    global roomsize
    global rooms
    global m
    global mx
    global my
    global mc
    ew_length = int(filein[0].split(' ')[0])
    ns_length = int(filein[0].split(' ')[1])

    a = [[] for lines in range(ew_length)]
    for i in range(ew_length):
        for j in range(ns_length):
            a[i].append(0)
    for k in range(1,ns_length+1):
        filein[k] = filein[k].split()
    
    for y in range(1,ns_length+1):
        for x in range(0,ew_length):
            temp = int(filein[y][x])
            a[x][y-1] = Room()
            a[x][y-1].wall = temp
                          
    nroom = 0
    for y in range(0,ns_length):
        for x in range(0,ew_length):
            if not a[x][y].numbered:
                nroom += 1
                roomsize[nroom] = 0
                number(nroom,x,y)


    num_rooms = len(list(set(rooms)))
    for f in range(1,num_rooms+1):
        room_area.append(rooms.count(f))
    max_area = max(room_area)
    
    m = 0
    for x in range(0,ew_length):
        for y in range(ns_length-1,-1,-1):
            if a[x][y].room != a[x][y-1].room and y>0:
                n = roomsize[a[x][y].room] + roomsize[a[x][y-1].room]
                if n > m:
                    m = n
                    mx = x
                    my = y
                    mc = 'N'

            if x+1 < ew_length and a[x][y].room != a[x+1][y].room:
                n = roomsize[a[x][y].room] + roomsize[a[x+1][y].room]
                if n > m:
                    m = n
                    mx = x
                    my = y
                    mc = 'E'
    wall_num = str(my+1) + ' ' + str(mx+1) + ' ' + mc
    outstring = str(num_rooms) + '\n' + str(max_area) + '\n' + str(m) + '\n' + wall_num
    return outstring



def number(room,x,y):
    global ns_length
    global ew_length
    global roomsize
    global rooms

    if a[x][y].numbered:
        return

    
    a[x][y].numbered = True
    a[x][y].room = room
    roomsize[room] += 1
    rooms.append(room)

    w = a[x][y].wall

    if x >0 and (w&1 == 0):
        number(room,x-1,y)

    if x+1 < ew_length and (w&4 == 0):
        number(room,x+1,y)
    
    if y >0 and (w&2 == 0):
        number(room,x,y-1)
    
    if y+1 < ns_length and (w&8 == 0):
        number(room,x,y+1)
    
    return

    

        
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('castle.out',main(read_in('castle.in')))


