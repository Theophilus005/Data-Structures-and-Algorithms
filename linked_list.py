# Node class
# Class representation of a node
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "[Node: %s]" % self.data

# Linked list class
# Class representation of a linked list
class LinkedList:
    head = None

    # Adds a node to the head of the linked list
    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    # Adds a node to the tail of the linked list
    def append(self, data):
        new_node = Node(data)
        current = self.head
        if current == None:
            self.prepend(data)
        else: 
            while current != None:
                if(current.next_node == None):
                    current.next_node = new_node
                    return
                current = current.next_node

    # Adds a node at any position in the linked list
    def add_at(self, data, position):
        size = self.size()
        if position > size:
            print("Undefined index")
            return
        new_node = Node(data)
        current = self.head
        index = 0
        prev_node = None
        target_node = None
        if position == 0:
            self.prepend(data)
        else:
            while current != None:
                if index == position-1:
                    prev_node = current
                    target_node = prev_node.next_node

                    prev_node.next_node = new_node
                    if target_node != None:
                        new_node.next_node = target_node
                        return
                index += 1
                current = current.next_node

    # Deletes a node at any point in the linked list
    def delete_at(self, position):
        size = self.size()
        if position > size or size == 0:
            print("Undefined index")
            return
        current = self.head
        index = 0
        prev_node = None
        target_node = None
        if position == 0:
            next_node = current.next_node
            self.head = next_node
        else:
            while current != None:
                if index == position-1:
                    prev_node = current
                    target_node = prev_node.next_node
                    prev_node.next_node = target_node.next_node
                    return
                index += 1
                current = current.next_node

    # Returns the number of nodes in the linked list
    def size(self):
        current = self.head
        if current == None:
            return 0
        else:
            index = 0
            while current.next_node != None:
                current = current.next_node
                index += 1
            return index + 1      


    def __repr__(self):
        list = []
        if self.head != None:
            current = self.head
            list.append("[Head: %s]" % current.data)
            current = current.next_node
            while current != None:
                list.append("[Node: %s]" % current.data)
                if current == None and current != None:
                    list.append("[Tail: %s]" % current.data)
                current = current.next_node

            return "->".join(list)

        else: 
            return "Empty linked list"

list1 = LinkedList()
# Adds 45 at the head of the list
list1.prepend(45)

# Adds 25 at the tail of the list
list1.append(20)

# Add 10 at the specified position in the list
list1.add_at(10,2)

#Returns the size of the list
#list1.size()

#Deletes a node at the specified position in the list
#list1.delete_at(5)



print(list1)
