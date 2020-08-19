#haiakhilmd
test = int(input())
for t in range(test):
    ans = []
    n = int(input())
    while n > 0:
        rem = n%26
        if rem == 0:
            ans.append('Z')
            n = (n//26) - 1
        else:
            ans.append(chr(rem + ord('A')-1))
            n = n//26
    #print(ans)
    ans = ans[::-1]
    print("".join(ans))