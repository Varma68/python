def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        #print(1)
        while start < len(arr) and arr[start]<=pivot:
            start+=1
        while arr[end]>pivot:
            end-=1
        if start < end:
            arr[start],arr[end]=arr[end],arr[start]
    arr[pivot_index],arr[end] = arr[end],arr[pivot_index]
    return end

def quick_sort(arr,start,end):
    if start<end:
        pi = partition(arr,start,end)
        quick_sort(arr,0,pi-1)
        quick_sort(arr,pi+1,end)
if __name__ == "__main__":
    arr=[5,1,8,2,3]
    quick_sort(arr,0,len(arr)-1)
    print(arr)