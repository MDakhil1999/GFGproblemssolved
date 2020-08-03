if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    tmp = []
    for i in arr:
        if i not in tmp:
            tmp.append(i)
    tmp.sort()
    tmp = tmp[::-1]
    print(tmp[1])
