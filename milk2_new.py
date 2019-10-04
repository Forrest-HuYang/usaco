"""
ID: tony_hu1
PROG: milk2
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a 

def milk_cows_main(flines):     
    total = []
    num_cows = int(flines[0])
    for i in range(num_cows):
        b = flines[i+1].split(' ')
        total.append([int(b[0]),int(b[1])])
    arrange(total)
    
def arrange(total):
    total.sort()
    time= [[0,0]]
    for i in range(len(total)):
        a = total[i][0]
        b =time[len(time)-1][0]
        c =time[len(time)-1][1]
        judgement = (a >= b )and (a <= c)
        if judgement:
            period = [time[len(time)-1][0],max(total[i][1],time[len(time)-1][1])]
            time[len(time)-1] = period
        else:
            time.append(total[i])
    if time[0]==[0,0]:
        del time[0]
    result(time)

def result(total):
    no_cows = 0
    for i in range(len(total)-1):
        x = total[i+1][0] - total[i][1]
        no_cows = max(no_cows,x)
    cows = 0
    for i in range(len(total)):
        x = total[i][1] - total[i][0]
        cows = max(cows,x)



    fout = open ('milk2.out', 'w')
    a = str(cows) + ' ' + str(no_cows)+'\n'
    fout.write(a)

flines = read_in("milk2.in")
milk_cows_main(flines)