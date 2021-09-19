import random

def is_sorted(list):
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def bogo_sort(list):
    count = 0
    while not is_sorted(list):
        count += 1
        print(count)
        random.shuffle(list)
    return list

numbers = [4,2,52, 100, 43,54]
print(bogo_sort(numbers))

