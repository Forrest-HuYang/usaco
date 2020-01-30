
def tower(n,original,new,empty):
    if n == 1:
        print(original + ' to ' + new)
        return
    tower(n-1,original,empty,new)
    tower(1,original,new,empty)
    tower(n-1,empty,new,original)


tower(5,'a','b','c')
print(count)