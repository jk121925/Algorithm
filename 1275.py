import sys
input = sys.stdin.readline

n,m = map(int,input().split(" "))
l = list(map(int, input().split(" ")))
tree = [0] * (4*n+1)

def init_tree(start,end,node):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    
    mid = (start+end)//2
    tree[node] = init_tree(start,mid,node*2) + init_tree(mid+1,end,node*2+1)
    return tree[node]
init_tree(0,len(l)-1,1)

def sum(start,end,node,left,right):
    if left >end or right <start:
        return 0
    elif left <=start and end<=right:
        return tree[node]
    mid = (start+end)//2
    return sum(start,mid,node*2,left,right) + sum(mid+1,end,node*2+1,left,right)

def update(start,end,node,key,value):
    if key < start or end < key:
        return 
    tree[node] += value
    if start == end:
        return
    mid = (start+end)//2
    update(start,mid,node*2,key,value)
    update(mid+1,end,node*2+1,key,value)

for _ in range(m):
    s,e,key,value = map(int,input().split(" "))
    if e < s:
        print(sum(0,len(l)-1,1,e-1,s-1))
    else:
        print(sum(0,len(l)-1,1,s-1,e-1))
    update(0,len(l),1,key-1, value-l[key-1])
    # print(tree)
