#haiakhilmd
test = int(input())
for t in range(test):
    string = input()
    seen = {}
    start = 0
    maxlen = 0
    for end in range(len(string)):
        if string[end] in seen:
            start = max(start,seen[string[end]]+1)
        seen[string[end]] = end
        maxlen = max(maxlen,end-start+1)
    print(maxlen)
        