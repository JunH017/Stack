import sys
N=int(sys.stdin.readline())

a=[]
count=1
for i in range(N):
    a.append(int(sys.stdin.readline()))
b=a[-1]
for i in range(len(a)-1,-1,-1):
    if a[i]>b:
        count+=1
        b=a[i]
print(count)
