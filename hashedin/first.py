s = input()
t = input()
stack1 = []
for i in range(len(s)):
    if s[i] != "#":
        stack1.append(s[i])
    else:
        if len(stack1) > 0:
            stack1.pop()
stack2 = []
for i in range(len(t)):
    if t[i] != "#":
        stack2.append(t[i])
    else:
        if len(stack2) > 0:
            stack2.pop()
print(stack1)
print(stack2)
if stack1==stack2:
    print(True)
else:
    print(False)
