# Linear search (Data structures and algorithms)

# Iterative search of linear search using a for loop
# Returns the index of the target if found
def linear_search(list, target):
    for index in range(0, len(list)-1):
        if list[index] == target:
            print("Target found at index: ", index)
            return
    print("Target not found")


#Recursion of version of linear search
#Returns the index of the target if found
def linear_search_recursion(list, target, index=0):
    if len(list) == 0:
        print("Target not found")
        return
    elif list[0] == target:
        print("Target found at index: ", index)
        return
    index += 1
    return linear_search_recursion(list[1:], target, index)


numbers = [1,5,3,56,4,6,764,4364,7]

print("Using iterative method: ")
linear_search(numbers, 4)

print("Using recursion method: ")
linear_search_recursion(numbers, 4)
