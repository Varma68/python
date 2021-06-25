n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))
list1 = sorted(list1)
list2=[]
count=0
count+=1
flag = False
for i in range(len(list1)-2,-1,-1):
    num = list1[i + 1]
    if(list1[i]<num):
        list2.append(num)
        count+=1
        for j in range(len(list2)):
            list2[j]-=1
        if(0 in list2):
            print(count)
            flag =True
            break
if flag == False:
    print(count)