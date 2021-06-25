def pluses(str1,index):
    i = 0
    sum1 =0
    str2=''
    list1 = str1.split('=')
    print(list1)
    str1=list1[0]
    res = int(list1[-1])

    for i in str1:

        if i!='+':
            str2+=i
        else:
            sum1+=int(str2)
            str2=''
        sum1+=int(str2)



