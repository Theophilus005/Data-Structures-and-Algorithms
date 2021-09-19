# Binary Search (Data Structures and Algorithms)

#Iterative version of binary search
#Returns the index of the target if  found
def binary_search(list, target):
    first = 0
    last = len(list)
    
    while (last - first) != 1:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            print("Target found at index: ", midpoint)
            return            
        elif list[midpoint] < target:
            first = midpoint
        else:
            last = midpoint
        
    print("Target not found")


#Recursion version of binary search
#Returns the index of the target if  found
def binary_search_recursion(list, target, index=0):
    if len(list) == 0:
        print("Target not found")
        return
    else:
        index += 1
        midpoint = len(list)//2
        if list[midpoint] == target:
            print("Target found at index ", index)
        elif list[midpoint] > target:
            return binary_search_recursion(list[:midpoint], target, index)
        else:
            return binary_search_recursion(list[midpoint:], target, index)



numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print("Using iterative method: ")
binary_search(numbers, 8)

print("Using recursion method: ")
binary_search(numbers, 8)

