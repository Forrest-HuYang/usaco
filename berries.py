def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def main(instring):
    N = int(instring[0].split(' ')[0])
    K = int(instring[0].split(' ')[1])
    A = []
    m = 0
    instring = instring[1].split(' ')
    for i in range(0,N):
        A.append(int(instring[i]))
        m = max(m,int(instring[i]))
    best = 0
    for b in range(1,m+1):
        full = 0
        for i in range(0,N):
            full += A[i]/b
        if full < K/2:
            break
        if full > K:
            best = max(best,b*(K/2))
        mod = b
        A.sort()
        cur = b*(full - K/2)
        for i in range(min(N,K-int(full))):
            cur += A[i]/b
        best = max(best,cur)
    
    print('shit')

main(read_in('berries.in'))
    