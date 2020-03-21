mypoints = []
x_dict = {}
y_dict = {}
rightVertexSum_x = {}
rightVertexSum_y = {}
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(instring):
    mypoints = []
    global x_dict
    global y_dict
    global rightVertexSum_x
    global rightVertexSum_y
    x_set = set()
    y_set = set()
    num_points = int(instring[0])
    for i in range(1,num_points+1):
        temp = instring[i].split()
        x = int(temp[0])+10000
        y = int(temp[1])+10000
        
        
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
        y_list = x_dict[x]
        num_ys = len(y_list)
        if num_ys > 1:
            for y in y_list:
                x_list = y_dict[y]
                num_xs = len(x_list)
                if num_xs > 1:
                    point = str(x) + ' ' + str(y)
                    if point in rightVertexSum_x:
                        x_sum = rightVertexSum_x[point]
                    else:
                        getVertexSum('x',y)
                        x_sum = rightVertexSum_x[point]
                    if point in rightVertexSum_y:
                        y_sum = rightVertexSum_y[point]
                    else:
                        getVertexSum('y',x)
                        y_sum = rightVertexSum_y[point]
                    
                    area += x_sum*y_sum




    vv = 10**9 +7
    area = area%vv
    fout = open('triangles.out', 'w')
    fout.write(str(area) + '\n')
                
def getVertexSum(mytype,value):
    global x_dict
    global y_dict
    global rightVertexSum_x
    global rightVertexSum_y
    if mytype == 'x':
        x_list = y_dict[value]
        length = len(x_list)
        index_initial = str(x_list[0])+' '+ str(value)
        temp = 0
        current = x_list[0]
        for element in x_list:
            result = element - current
            temp += result
        rightVertexSum_x[index_initial] = temp
        prev_val = temp
        prev = current
        for i in range(1,len(x_list)):
            current = x_list[i]
            temp = prev_val+(2*i  - length)*(current-prev)
            rightVertexSum_x[str(current)+' '+ str(value)] = temp
            prev_val = temp
            prev = current

    if mytype == 'y':
        y_list = x_dict[value]
        length = len(y_list)
        index_initial = str(value)+' '+ str(y_list[0])
        temp = 0
        current = y_list[0]
        for element in y_list:
            result = element - current
            temp += result
        rightVertexSum_y[index_initial] = temp
        prev_val = temp
        prev = current
        for i in range(1,len(y_list)):
            current = y_list[i]
            temp = prev_val+(2*i  - length)*(current-prev)
            rightVertexSum_y[str(value)+' '+ str(current)] = temp
            prev_val = temp
            prev = current


main(read_in('triangles.in'))