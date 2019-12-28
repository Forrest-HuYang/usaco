name_no = {'Beatrice':0,'Belinda':1,'Bella':2,'Bessie':3,'Betsy':4,'Blue':5,'Buttercup':6,'Sue':7}
no_name = {0:'Beatrice',1:'Belinda',2:'Bella',3:'Bessie',4:'Betsy',5:'Blue',6:'Buttercup',7:'Sue'}
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(filein):
    scores = []
    paired = []
    m = []
    novalid = 0
    no_lessons = int(filein[0].split(' ')[0])
    no_students = int(filein[0].split(' ')[1])
    for i in range(no_lessons):
        scores.append(filein[i+1].split(' '))
    print (scores)
    
    for j in range(1,no_students+1):
        for k in range(1,no_students+1):
            m = [j,k]
            m.sort()
            if j == k or m in paired:
                pass
            else:
                scores = []
                for i in range(no_lessons):
                    scores.append(filein[i+1].split(' '))
                paired.append(m)
                if is_valid_pair(j,k,scores,no_students):
                    print(i,j)
                    novalid += 1
    return novalid

def is_valid_pair(j,k,scores,no_students):
    print (scores)
    for i in range(1,no_students+1):
        if i != j and i != k:
            for x in range(len(scores)):
                scores[x].remove(str(i))
    
    for y in range(len(scores)-1):
        if scores[y] != scores[y+1]:
            return False

    return True
        
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('gymnastics.out',main(read_in('gymnastics.in')))