class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data


    def __repr__(self):
        return "<Node data: %s>" % self.data 
    
class LinkedList:
    #head = Node
    """
    singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self): 
        """
        Returns the number of nodes in the list 
        Takes 0(n) time
        """
        current = self.head
        count = 0

        while current != None: # can just do while current
            count += 1
            current = current.next_node

        return count
    
    def add(self, data): #prepend
        """
        adds a new node containing data at the head of the list. constant time [0(1)]
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns thee node or 'None' if not found
        Takes 0(n) time
        """

        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None    
    
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes 0(1) time but find the node at the insertion point takes 0(n) time
        Overall 0(n) time
        """
        if index == 0:
            self.add(data)
        
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def node_at_index(self, index):
        """
        Returns the Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        if index == 0:
            return self.head

        current = self.head
        position = 0

        while position < index:
            current = current.next_node
            position += 1

        return current


    def remove(self, key):
        """"
        Removes not containing data that matches the key
        Returns the node or Node if the key doesn't exist
        takes 0(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        return current
    
    
    def remove_at_index(self, index):
        """
        Removes Node at specified index
        Takes O(n) time
        """

        if index >= self.__count:
            raise IndexError('index out of range')

        current = self.head

        if index == 0:
            self.head = current.next_node
            self.__count -= 1
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        current = current.next_node
        next_node = current.next_node

        prev_node.next_node = next_node
        self.__count -= 1

        return current


    def __repr__(self):
        """
        Return a string representation of the list
        Taken 0(n) time
        """

        nodes = [] #python list not a linked list
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)