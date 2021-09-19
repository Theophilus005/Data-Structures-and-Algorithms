def selection_sort(list):
    if len(list) <= 1:
        return 

    new_list = []

    while len(list) > 0: # Checks if all numbers have been moved or not
        index = 0
        min_index = 0
        while index != len(list): # Gets the smallest index
            if list[index] < list[min_index]:
                min_index = index 
            index += 1
        smallest_number = list[min_index]
        list.pop(min_index) # Removes the number with the smallest index
        new_list.append(smallest_number) # Appends the smallest the number to the new list
    return new_list

def is_sorted(list):
    for i in range(0, len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True


def sort_in_place(list):
    size = len(list)-1
    if size <= 1:
        return 

    while not is_sorted(list): 
        index = 0
        min_index = 0
        while index != size: 
            print(index)
            if list[index] < list[min_index]:
                min_index = index 
            index += 1
        #print(len(list))
        smallest_number = list.pop(min_index)
        list.append(smallest_number)         
    return list    

numbers = [4,2,52, 100, 43,54,32, 12, 1, 51]
print(sort_in_place(numbers))
