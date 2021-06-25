n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
amt = int(input())
sum1 = 0
i = 0
num=0
num1=0
count=0
j = n-1
flag = False
while i<j and sum1<=amt:
    sum1+=list1[i]
    num = list1[i]
    i+=1
    count+=1
sum1=sum1-num
if(sum1 == amt):
    print(count-1)
    flag = True
if sum1!=amt and flag != True:
    while i<j and sum1<=amt:
        sum1+=list1[j]
        num = list1[j]
        j-=1
        count+=1
    sum1=sum1-num
    if amt == sum1 :
        print(count-2)
    else:
        print(-1)







