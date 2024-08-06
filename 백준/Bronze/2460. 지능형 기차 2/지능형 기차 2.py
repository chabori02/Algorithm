sum=[]
total=0
for i in range(10):
    num=list(map(int,input().split(" ")))
    total+=num[1]-num[0]
    sum.append(total)
print(max(sum))