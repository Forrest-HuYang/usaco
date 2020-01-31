"""
ID: tony_hu1
PROG: castle
LANG: PYTHON3
"""
components = []
walls = dict()
total = []
area = 0
done = 0
ew_length = 0
ns_length = 0
searched = set()
room_area = [0]
max_combined_area = 0
m_number = 0
m_direction = ''

def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(filein):
    global ns_length
    global ew_length
    global max_combined_area
    global m_number
    global m_direction
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
    num_rooms = len(list(set(components)))

    for m in range(1,num_rooms+1):
        room_area.append(components.count(m))
    max_area = max(room_area)
    find_largest_possible(ew_length*(ns_length-1),ns_length,ew_length)

    largest_combined = max_combined_area
    wall_num = str(ns_length+1-m_number[1]) + ' '+str(m_number[0]) + ' ' +m_direction.swapcase()
    outstring = str(num_rooms) + '\n' + str(max_area) + '\n' + str(largest_combined) + '\n' + wall_num
    return outstring


def find_largest_possible(current,ns_length,ew_length):
    global max_combined_area
    global m_number
    global m_direction
    if current in searched:
        return
    searched.add(current)
    current_component = components[current]
    temp = walls[current]

    if current == ns_length*ew_length-1:
        return
    
    if current - ew_length >= 0:
        if (not temp['n']) or components[current-ew_length] == current_component:
            find_largest_possible(current - ew_length,ns_length,ew_length)
        else:
            next_room = current - ew_length
            combined_area = room_area[current_component] + room_area[components[next_room]]
            if combined_area > max_combined_area:
                max_combined_area = combined_area
                m_number = get_coordinates(current)
                m_direction = 'n'
            elif combined_area == max_combined_area:
                new = get_coordinates(current)
                if new < m_number:
                    m_number = new
                    m_direction = 'n'
            find_largest_possible(next_room,ns_length,ew_length)

    a = (current+1) % ew_length
    if not a == 0:
        if (not temp['e']) or components[current+1] == current_component:
            find_largest_possible(current+1,ns_length,ew_length)
        else:
            next_room = current + 1
            combined_area = room_area[current_component] + room_area[components[next_room]]
            if combined_area > max_combined_area:
                max_combined_area = combined_area
                m_number = get_coordinates(current)
                m_direction = 'e'
            elif combined_area == max_combined_area:
                new = get_coordinates(current)
                if new < m_number:
                    m_number = new
                    m_direction = 'e'
            find_largest_possible(next_room,ns_length,ew_length)


    
    return

def get_coordinates(number):
    global ew_length
    global ns_length
    number += 1
    x = number%ew_length
    if x == 0:
        x = ew_length

    y = (number - x) // ew_length
    y = ns_length-y
    return x,y

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
    

        
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('castle.out',main(read_in('castle.in')))