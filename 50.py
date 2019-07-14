nn,kk=map(int,input().split())
ss=0
if kk<=nn:
    while nn>0 and nn>=kk:
        nn=nn-kk
        ss=ss+1
print(ss)
