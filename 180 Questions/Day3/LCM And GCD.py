#haiakhilmd
def lcm(x,y,g):
    x = x//g
    y = y//g
    return x*y*g


def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x%y)


test = int(input())
for t in range(test):
    x,y = list(map(int,input().split()))
    g = gcd(x,y)
    l = lcm(x,y,g)
    print(l,g)