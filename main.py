def count(l):
    c=0
    for i in l:
        if l.count(i)>1:
            l.remove(i)
            c+=1
    return c
l=list(map(int,input().split()))
print(count(l))

