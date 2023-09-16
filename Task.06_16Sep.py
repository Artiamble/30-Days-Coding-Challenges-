def mid(arr):
    if len(arr)<3:
        return arr
    return mid(arr[1:-1])
print(mid(input(" Enter Elements...")))