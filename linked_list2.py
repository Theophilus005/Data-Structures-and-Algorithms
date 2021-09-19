# Node class
class Node:
    data = None
    next_node = None

    def  __init__(self, data):
        self.data = data

    def __repr__(self):
        return "[%s]" % self.data

# LinkedList
class LinkedList:
    head = None

    #prepend
    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    #append
    def append(self, data):
        new_node = Node(data)
        if self.head != None:
            current = self.head
        else:
            self.prepend(data)
            return
        while current.next_node != None:
            current = current.next_node
        current.next_node = new_node


    #insert_at
    def insert_at(self, data, position):
        if position > self.size():
            print("Invalid index")
        elif position == 0:
            self.prepend(data)
        else:
            index = 0
            current = self.head
            while index != position-1:
                index += 1
                current = current.next_node
            new_node = Node(data)
            prev_node = current
            target_node = prev_node.next_node
            prev_node.next_node = new_node
            new_node.next_node = target_node

    #delete_at
    def delete_at(self, position):
        current = self.head
        if position > self.size()-1:
            print("Invalid index")
        elif position == 0:
            next_node = current.next_node
            self.head = next_node
        else:
            index = 0
            while index != position-1:
                index =+ 1
                current = current.next_node
            prev_node = current
            target_node = prev_node.next_node
            prev_node.next_node = target_node.next_node

    #delete all
    def delete_all(self):
        self.head = None


    #size
    def size(self):
        index = 0
        current = self.head
        while current != None:
            index += 1
            current = current.next_node
        return index

    #Acessing node values
    def node(self, position):
        if position > self.size()-1:
            return "Invalid index"
        index = 0
        current = self.head
        while index != position:
            index += 1
            current = current.next_node
        return current.data
        

    # is_empty
    def is_empty(self):
        return self.head == None


    #reverse
    def reverse(self):
        reversed_list = LinkedList()
        size = self.size() - 1
        current = self.head
        index = 0
        while size >= 0:
            if index == size:
                reversed_list.append(current.data)
                size -= 1
                current = self.head
                index = 0
            else:
                index += 1
                current = current.next_node
            
        return reversed_list

    #reverse in place
    def reverse_in_place(self):
        size = self.size()-1
        initial_size = size
        current = self.head
        index = 0
        while size >= 0:
            if index == size:
                self.append(current.data)
                index = 0
                size -= 1
                current = self.head
            else:
                index += 1
                current = current.next_node
        #Set new head
        while initial_size > 0:
            current = current.next_node
            initial_size -= 1
        prev_tail = current
        self.head = prev_tail.next_node
        prev_tail.next_node = None

            

    def __repr__(self):
        nodes = []
        current = self.head
        if current == None:
            return "Empty"
        while(current is not None):
            nodes.append("[%s]" % current.data)
            current = current.next_node
        return "->".join(nodes)


l1 = LinkedList()
l1.append(12)
l1.append(13)
l1.append(14)
l1.append(11)
l1.append(17)
l1.append(10)
l1.append(16)
l1.insert_at(2, 3)

print(l1)