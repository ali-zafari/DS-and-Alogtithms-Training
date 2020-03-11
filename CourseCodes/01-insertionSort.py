import random
import time


def insertion_sort(a):
    for j in range(1, len(a)):
        to_compare = a[j]
        i = j-1
        while i >= 0 and to_compare < a[i]:
            a[i], a[i+1] = to_compare, a[i]
            # a[i+1] = a[i]
            i = i - 1
        # a[i+1] = to_compare


num_list = [x for x in range(1000)]
random.shuffle(num_list)

print('Unsorted list:', num_list)
start = time.time()
insertion_sort(num_list)
end = time.time()
print('Time elapsed:', end-start)
print('Sorted list:', num_list)
