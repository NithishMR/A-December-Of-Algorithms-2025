s = input().strip()

if s[0] != "[":
    print(int(s))
    exit()

stack = []
num = 0
sign = 1
current = None

for ch in s:
    if ch == '[':
        new_list = []
        if stack:
            stack[-1].append(new_list)
        stack.append(new_list)
    elif ch == '-':
        sign = -1 # i have done for negative number identification
    elif ch.isdigit():
        num = num * 10 + int(ch)
    elif ch == ',':
        if sign is not None:
            stack[-1].append(sign * num)
            num = 0
            sign = 1
    elif ch == ']':
        if sign is not None and (num != 0 or sign == -1):
            stack[-1].append(sign * num)
        num = 0
        sign = 1
        current = stack.pop()

print(current)
