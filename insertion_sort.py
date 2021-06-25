def insertion_sort(arr):
    for i in range(1,len(arr)):
        anchor = arr[i]
        j = i - 1
        while j>=0 and anchor < arr[j]:
            arr[j+1]=arr[j]
            j = j - 1
        arr[j+1] = anchor
if __name__ == '__main__':
    arr = [5,6,2,8,1]
    insertion_sort(arr)
    print(arr)