def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(filestring):
    temp = filestring[0].split()
    n = int(temp[0])
    l = int(temp[1])
    w = {}
    d = []
    x = {}
    total_w = 0
    right = 0
    right_list = []
    left_list = []
    for line in filestring[1:]:
        temp = line.split()
        dis = int(temp[1])
        d.append(dis)
        w[dis] = int(temp[0])
        total_w += int(temp[0])
        x[dis] = int(temp[2])
        if int(temp[2]) == 1:
            right += 1
            right_list.append(dis)
        else:
            left_list.append(dis)
    
    d.sort()
    right_list.sort()
    left_list.sort()
    time_list = []
    weight = {}
    for i in range(n-right):
        cow = d[i]
        weight_cur = w[cow]
        time = left_list[i]
        if time in weight:
            weight[time] += weight_cur
        else:
            weight[time] = weight_cur
            time_list.append(time)
    
    for i in range(n-right,n):
        cow = d[i]
        weight_cur = w[cow]
        time = l-right_list[i-n+right]
        if time in weight:
            weight[time] += weight_cur
        else:
            weight[time] = weight_cur
            time_list.append(time)
    
    time_list.sort()
    critical_w = total_w/2
    w_arrive = 0
    for t in time_list:
        w_arrive += weight[t]
        if w_arrive >= critical_w:
            break

    meetings = get_meeting(t,left_list,right_list)

    fout = open('meetings.out', 'w')
    fout.write(str(meetings) + '\n')

def get_meeting(time,left_list,right_list):
    meetings = 0
    for left in left_list:
        good = left - 2*time
        for right in right_list:
            if right > left:
                break
            if right >= good:
                meetings += 1
    
    return meetings

    


main(read_in('meetings.in'))

