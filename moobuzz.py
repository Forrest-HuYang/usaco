with open('moobuzz.in') as filename:
    for line in filename:
       n = int(line.rstrip())
remainder = n%8
cycles_done = n//8
convert = {0:-1,1:1,2:2,3:4,4:7,5:8,6:11,7:13,8:14}
fout = open('moobuzz.out', 'w')
fout.write(str(cycles_done*15+convert[remainder]) + '\n')