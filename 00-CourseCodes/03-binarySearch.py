def binary_search(a, x, low, high):
    if low <= high :
        mid = (low + high)//2
        if a[mid] == x :
            return mid
        elif a[mid] > x :
            return binary_search(a, x, low, mid-1)
        else:
            return binary_search(a, x, mid+1, high)
    else:
        return -1


a = [x for x in range(100)]
print(binary_search(a, 99, 0, len(a)-1))


