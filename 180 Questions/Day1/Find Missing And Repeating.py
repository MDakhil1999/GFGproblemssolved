test = int(input())
for t in range(test):
    n = int(input())
    array = input().split()
    wplusyplusy = 0
    wsqrplusysqrplusysqr = 0
    for i in array:
        if i != " ":
            wplusyplusy += int(i)
            wsqrplusysqrplusysqr += (int(i))**2
    wplusxplusy = 0
    wsqrplusxsqrplusysqr = 0
    for i in range(n+1):
        wplusxplusy += i
        wsqrplusxsqrplusysqr += i**2
    xminusy = wplusxplusy - wplusyplusy
    xsqrminusysqr = wsqrplusxsqrplusysqr - wsqrplusysqrplusysqr
    xplusy = xsqrminusysqr//xminusy
    twox = xminusy + xplusy
    miss = twox//2
    rep = miss - xminusy
    print(rep,miss)