def merge_sort(list):
    if len(list) <= 1:
        return list
    else:
        left_half, right_half = split(list)
        left = merge_sort(left_half)
        right = merge_sort(right_half)
        return merge(left, right)

def split(list):
    midpoint = len(list)//2
    left = list[:midpoint]
    right = list[midpoint:]
    return left, right

def merge(left, right):
    new_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_list.append(left[i])
            i += 1
        else:
            new_list.append(right[j])
            j += 1
    
    while i < len(left):
        new_list.append(left[i])
        i += 1

    while j < len(right):
        new_list.append(right[j])
        j += 1

    return new_list


numbers = [12, 32, 54, 43, 4, 24, 67, 31]
print(merge_sort(numbers))


    
