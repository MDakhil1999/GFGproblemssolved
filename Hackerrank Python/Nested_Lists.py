arr = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
arr.sort(key=lambda x:x[1])
marks = []
for i in arr:
    if i[1] not in marks:
        marks.append(i[1])
names = [[] for i in range(len(marks))]
for i in arr:
    x = marks.index(i[1])
    names[x].append(i[0])
ans = names[1]
ans.sort()
for i in ans:
    print(i)
