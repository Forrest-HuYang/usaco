a = ''
m = []
for q in range(8):
    for w in range(8):
        if w != q:
            for e in range(8):
                if len(set([e,q,w])) == 3:
                    for r in range(8):
                        if len(set([e,q,w,r])) == 4:
                            for t in range(8):
                                if len(set([e,q,w,r,t])) == 5:
                                    for  y in range(8):
                                        if len(set([e,q,w,r,t,y])) == 6:
                                            for u in range(8):
                                                if len(set([e,q,w,r,t,y,u])) == 7:
                                                    for i in range(8):
                                                        if len(set([e,q,w,r,t,y,u,i])) == 8:

                                                            m = str(q)+str(w)+str(e)+str(r)+str(t)+str(y)+str(u)+str(i)
                                                            a += m
                                                            a += ' '
                                                            m = str(i)+str(u)+str(y)+str(t)+str(r)+str(e)+str(w)+str(q)
                                                            a += m
                                                            a += ' '


fout = open ('fuckingshit.txt', 'w')
fout.write(a)

                                
