test = int(input())
for t in range(test):
    string = input()
    arr = list(map(str,string))
    new = []
    for i in arr:
        new.append(ord(i) - ord("A") + 1)
    ans = 0
    new = new[::-1]
    for i in range(len(new)):
        ans += (new[i] * (26**i))
    print(ans)