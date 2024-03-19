import sys
input = sys.stdin.readline

s = input().strip()
m = input().strip()

stack = []
for i in s:
    stack.append(i)
    if stack[-1] == m[-1] and stack[-len(m):]:
        del stack[-len(m)]
if len(stack) !=0:
    print("".join(stack))
else:
    print("FRULA")
