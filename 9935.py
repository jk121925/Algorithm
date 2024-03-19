import sys
input = sys.stdin.readline

s = input().strip()
m = input().strip()

stack = []
i =len(s)-1
for i in s:
    stack.append(i)
    if stack[-1] == m[-1] and stack[-len(m):]:
        cnt =0 
        while cnt <len(m):
            stack.pop()
            cnt+=1
if len(stack) !=0:
    print("".join(stack))
else:
    print("FRULA")
