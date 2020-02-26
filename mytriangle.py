import math
mypoints = []
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(instring):
    mypoints = []
    x_dict = {}
    y_dict = {}
    x_set = set()
    y_set = set()
    num_points = int(instring[0])
    for i in range(1,num_points+1):
        temp = instring[i].split()
        x = int(temp[0])
        y = int(temp[1])
        
        
        if x in x_set:
            x_dict[x].append(y)
        else:
            x_set.add(x)
            x_dict[x] = [y]
        if y in y_set:
            y_dict[y].append(x)
        else:
            y_set.add(y)
            y_dict[y] = [x]
        mypoints.append(temp)

    area = 0
    for x in x_set:
        x_list = x_dict[x]
        length = len(x_list)
        if not length == 1:
            for f in range(length-1):
                for j in range(f+1,length):
                    y1 = x_list[f]
                    y2 = x_list[j]
                    yd = abs(y2-y1)
                    if y1 in y_set:
                        y_list = y_dict[y1]
                        for number in y_list:
                            xd = abs(number-x)
                            area += xd*yd
                    if y2 in y_set:
                        y_list = y_dict[y2]
                        for number in y_list:
                            xd = abs(number-x)
                            area += xd*yd
                    






    vv = 10**9 +7
    area = area%vv
    fout = open('triangles.out', 'w')
    fout.write(str(area) + '\n')
                


main(read_in('triangles.in'))