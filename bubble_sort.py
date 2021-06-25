def bubble_sort(list1):
    size = len(list1)
    for i in range(size):
        swapped = False
        for j in range(size-1-i):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1],list1[j]
                swapped = True
        if not swapped:
            break
if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    bubble_sort(list1)
    print(list1)