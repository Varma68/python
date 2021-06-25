n=3#int(input())
ai=[0,0,0,0,0]#list(map(int,input().split()))
bi=[1,10,13,5,3]#list(map(int,input().split()))
#print(n,ai,bi)
def nz(a,b,n):
    d={}
    c=0
    for i in range(n):
        if b[i]!=0 and a[i]!=0:
            v=(-1.0 *b[i])/a[i]
            d[v]=d.get(v,0)+1
        elif b[i]==0 and a[i]==0:
            c+=1
    #print(d,c)
    m=0
    if len(d.values())!=0:
        m = max(d.values())
    return m+c
print(nz(ai,bi,n))