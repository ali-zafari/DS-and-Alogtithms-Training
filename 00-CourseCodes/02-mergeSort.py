import random
import time


def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):
    L = []
    R = []

    for i in range(p, q+1):
        L.append(a[i])
    L.append(999999999)

    for j in range(q+1, r+1):
        R.append(a[j])
    R.append(999999999)

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] < R[j] :
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1


num_list = [x for x in range(100000)]
random.shuffle(num_list)

print('Unsorted list:', num_list)
start = time.time()
merge_sort(num_list, 0, len(num_list)-1)
end = time.time()
print('Time elapsed:', end-start)
print('Sorted list:', num_list)
