list1=[97, -27, 2, -34, 61, -39]
n = len(list1)
start = 0
end = 0
count = 0
list1.sort()
for i in range(n-2):
    start = i + 1
    end = n-1
    #print('i value',i)
    if list1[i]!='v' and list1[start]!='v' and list1[end]!='v':
        while start < end:
            #print(1)
            if list1[i] != 'v' and list1[start] != 'v' and list1[end] != 'v':
                sum1 = list1[i]+list1[start]+list1[end]
                if sum1==0:
                    #print(list1[i],list1[start],list1[end])
                    list1[i]='v'
                    list1[start]='v'
                    list1[end]='v'
                    start+=1
                    end-=1
                    count = +1
                    break
                elif sum1<0:
                    start+=1
                else:
                    end-=1
print(count)





