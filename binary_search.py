def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list)-1
    while left_index<=right_index:
        mid_index = (left_index + right_index) // 2
        #print(mid_index)
        if numbers_list[mid_index]==number_to_find:
            #print("mid")
            return mid_index
        if number_to_find < numbers_list[mid_index]:
            #print("left")
            right_index=mid_index-1
        else:
            #print("right")
            left_index = mid_index+1

    return -1
    #print(left_index, right_index, mid_index)
def binary_search_recursion(numbers_list, number_to_find, left_index, right_index):
    mid_index = (left_index+right_index)//2
    if right_index<left_index:
        return -1
    mid_number = numbers_list[mid_index]
    if mid_number == number_to_find:
        return mid_index
    if number_to_find < mid_number:
        right_index = mid_index - 1
    else:
        left_index = mid_index + 1
    return binary_search_recursion(numbers_list, number_to_find, left_index, right_index)
numbers_list = [1,2,3,4,5,6]
index = binary_search(numbers_list,5)
print(index)
index = binary_search_recursion(numbers_list,5,0,len(numbers_list)-1)
print(index)