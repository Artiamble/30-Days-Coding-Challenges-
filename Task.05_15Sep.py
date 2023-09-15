def second_largest_num(arr):
    n = len(arr)
    large = -100000
    sen_large = -100000
    for i in range(0, n):
        large = max(large, arr[i])
    
    for i in range(0, n):
        if (arr[i]!=large):
            sen_large = max(sen_large, arr[i])

    if (sen_large == -100000):
        print("There is no second largest element in the given array")
    else:
        print("The second largest element in the given array is ", sen_large)

arr = [9, 9, 9]
print("The given array is ", str(arr))
second_largest_num(arr)
print("-------------------------------")
arr1 = [2, 4, 1787, 1278, 18, 1]
print("The given array is ", str(arr1))
second_largest_num(arr1)
print("-------------------------------")
arr2 = [9, 78, 17]
print("The given array is ", str(arr2))
second_largest_num(arr2)