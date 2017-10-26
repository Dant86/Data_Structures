class Node:

    def __init__(self, value):
        '''
            Initializes a node with a value
            and a pointer to its next node
        '''
        self.value = value
        self.next = None

class TreeNode:

    def __init__(self, value):
        '''
            Initializes a node with a value and
            two pointers, each of which is pointing
            to one of its children
        '''
        self.value = value
        self.l_child = None
        self.r_child = None

class LinkedList:

    def __init__(self):
        '''
            Initializes a linked list with two nodes,
            one being the head (front), and the tail
            (back)
        '''
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, newVal):
        '''
            Adds a value to the end of the list
            by traversing to the end and setting
            its next to the new value
        '''
        newVal = Node(newVal)
        if self.head is None or self.tail is None:
            self.head = newVal
            self.tail = newVal
            self.length += 1
            return
        self.tail.next = newVal
        self.tail = newVal
        self.length += 1

    def prepend(self, newVal):
        '''
            Adds a value to the very beginning of a
            list by setting its next to the head, then
            setting the new value as head
        '''
        newVal = Node(newVal)
        if self.head is None or self.tail is None:
            self.head = newVal
            self.tail = newVal
            self.length += 1
            return
        newVal.next = self.head
        self.head = newVal
        self.length += 1

    def add(self, newVal, index):
        '''
            Adds a value at a given index by going to
            the node before it, then smushing it in between
            that node and its next node. If index is greater
            than the length, append zeros until we get to the
            specified index
        '''
        newNode = Node(newVal)
        if index < 0:
            raise ValueError("Index < 0")
        elif index == 0:
            self.prepend(newVal)
        elif index > 0 and index < self.length:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            self.length += 1
        elif index == self.length:
            self.append(newVal)
        else:
            for i in range(index - self.length):
                self.append(0)
            self.append(newVal)

    def set(self, newVal, index):
        '''
            Replaces a value at a given index
        '''
        if index < 0:
            raise ValueError("Index < 0")
        elif index >= self.length:
            raise ValueError("Index >= length")
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = newVal

    def remove_from_back(self):
        '''
            Removes the tail by traversing to the penultimate
            node, then cutting its next link
        '''
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        self.length -= 1

    def remove_from_front(self):
        self.head = self.head.next
        self.length -= 1

    def remove(self, index):
        '''
            Removes a node in a similar way to remove_from_back;
            however, this time, you traverse to the node before it
            instead of the penultimate one
        '''
        if index < 0:
            raise ValueError("Index < 0")
        elif index == 0:
            self.remove_from_front()
        elif index > 0 and index < self.length - 1:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.length -= 1
        elif index == self.length - 1:
            self.remove_from_back()
        else:
            raise ValueError("Index >= length of list")

    def __getitem__(self, index):
        '''
            Gets an item at a given index. Since this is a magic, or
            "dunder", method, we're now allowed to index this linked list
            as we would a regular list
        '''
        if index < 0:
            raise ValueError("Index < 0")
        elif index >= 0 and index < self.length:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.value
        elif index >= self.length:
            raise ValueError("Index >= length of list")

    def indexOf(self, value):
        '''
            Gets the index of an item in the linked list. If the item is
            not there, it returns -1
        '''
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == value:
                return idx
            idx += 1
        return -1

    def __len__(self):
        '''
            Returns the length attribute of the linked list
        '''
        return self.length

    def __str__(self):
        '''
            Nice way to cast a linked list into a string
        '''
        temp = self.head
        strVal = "["
        while temp is not None:
            strVal += str(temp.value)
            if temp.next is not None:
                strVal += ", "
            temp = temp.next
        return strVal + "]"

class Stack:

    def __init__(self):
        '''
            Initializes a stack, which is just a wrapper for
            a linked list
        '''
        self.values = LinkedList()

    def add(self, value):
        '''
            Adds like a stack would –– to the beginning
        '''
        self.values.prepend(value)

    def remove(self):
        '''
            Removes like a stack would –– from the beginning
        '''
        i = self.values.head.value
        self.values.remove_from_front()
        return i

    def __getitem__(self, index):
        '''
            Calls __getitem__ from the linked list
        '''
        return self.values.__getitem__(index)

    def indexOf(self, value):
        '''
            Calls indexOf from the linked list
        '''
        return self.values.indexOf(value)

    def __len__(self):
        '''
            Calls __len__ from the linked list
        '''
        return self.values.length

    def __str__(self):
        '''
            Calls __str__ from the linked list
        '''
        return str(self.values)

class Queue:

    def __init__(self):
        '''
            Initializes a queue, which is just a wrapper for
            a linked list
        '''
        self.values = LinkedList()

    def add(self, newVal):
        '''
            Adds like a queue would –– to the end
        '''
        self.values.append(newVal)

    def remove(self):
        '''
            Removes like a queue would –– from the beginning
        '''
        i = self.values.head.value
        self.values.remove_from_front()
        return i

    def __getitem__(self, index):
        '''
            Calls __getitem__ from the linked list
        '''
        return self.values.__getitem__(index)

    def indexOf(self, value):
        '''
            Calls indexOf from the linked list
        '''
        return self.values.indexOf(value)

    def __len__(self):
        '''
            Calls __len__ from the linked list
        '''
        return self.values.length

    def __str__(self):
        '''
            Calls __str__ from the linked list
        '''
        return str(self.values)

class Binary_Search_Tree:

    def __init__(self):
        '''
            Initializes a binary search tree, which
            just has a root to begin with
        '''
        self.root = None

    def add(self, newVal):
        '''
            Adds a value using the binary rules: if less,
            left. If greater or equal, right
        '''
        newNode = TreeNode(newVal)
        if self.root is None:
            self.root = newNode
            return
        temp = self.root
        while True:
            if newNode.value >= temp.value:
                if temp.r_child is None:
                    temp.r_child = newNode
                    return
                temp = temp.r_child
            else:
                if temp.l_child is None:
                    temp.l_child = newNode
                    return
                temp = temp.l_child

    def get_length(self, temp):
        '''
            Gets the amount of tree nodes within a binary search tree
        '''
        if temp is None:
            return 0
        if temp.l_child is None and temp.r_child is None:
            return 1
        return self.get_length(temp.l_child) + 1 + self.get_length(temp.r_child)

    def get_height(self, temp):
        '''
            Gets the height of a binary search tree
        '''
        if temp is None:
            return 0
        if temp.l_child is None and temp.r_child is None:
            return 1
        l_height = 1 + self.get_height(temp.l_child)
        r_height = 1 + self.get_height(temp.r_child)
        if r_height >= l_height:
            return r_height
        else:
            return l_height

    def height(self):
        '''
            Wrapper on top of get_height, which allows me to
            access root without altering it
        '''
        temp = self.root
        return self.get_height(temp)

    def lookup(self, lookup_val):
        '''
            Gives the node associated with a specified lookup
            value
        '''
        temp = self.root
        while True:
            if temp is None:
                return None
            if lookup_val == temp.value:
                return temp
            elif lookup_val >= temp.value:
                temp = temp.r_child
            else:
                temp = temp.l_child

    def remove_leaf(self, del_val):
        '''
            Goes all the way to the end and removes a leaf
        '''
        node_to_remove = self.lookup(del_val)
        temp = self.root
        link = ""
        while True:
            if del_val == temp.l_child.value:
                link = "left"
                break
            if del_val == temp.r_child.value:
                link = "right"
                break
            if del_val >= temp.value:
                temp = temp.r_child
            else:
                temp = temp.l_child
        if link == "left":
            temp.l_child = None
            return del_val
        else:
            temp.right = None
            return del_val

    def find_biggest_left(self):
        '''
            Helper function for delete, which finds
            the largest value on the left side of a node
        '''
        temp = self.root.left
        while temp.right is not None:
            temp = temp.right
        return temp.value

    def delete(self, del_val):
        '''
            Removes a value from the tree
        '''
        node_to_remove = self.lookup(del_val)
        temp = self.root
        link = ""
        while True:
            if del_val == temp.l_child.value:
                link = "left"
                break
            if del_val == temp.r_child.value:
                link = "right"
                break
            if del_val >= temp.value:
                temp = temp.r_child
            else:
                temp = temp.l_child
        if node_to_remove.l_child is None and node_to_remove.r_child is None:
            self.remove_leaf(del_val)
        else:
            biggest_left = self.find_biggest_left()
            node_to_remove.value = biggest_left
            self.remove_leaf(biggest_left)

    def __len__(self):
        '''
            Calls get_length, but now you can use len()
        '''
        temp = self.root
        return self.get_length(temp)

class HashTable:

    def __init__(self, size):
        '''
            Initializes a hash table with a table of <size>
            buckets, which are just empty linked lists
        '''
        self.buckets = [LinkedList() for i in range(size)]
        self.size = size

    def hash(self, key):
        '''
            Turns anything that has a __str__ function into
            an integer
        '''
        key = str(key)
        final_hash = 17
        for char in key:
            final_hash = (37 * final_hash) + ord(char)
        return final_hash % self.size

    def add_tuple(self, kv_pair):
        '''
            Adds a tuple to a list. Basically, this finds
            which bucket to insert the tuple into, and inserts
            it using the LinkedList functions
        '''
        hashed_key = self.hash(kv_pair[0])
        self.buckets[hashed_key].append(kv_pair)

    def add(self, key, value):
        '''
            Wrapper for add_tuple, but allows users to add a
            key/value pair instead of a tuple
        '''
        kv_pair = (key, value)
        self.add_tuple(kv_pair)

    def __getitem__(self, key):
        '''
            Allows you to index the hash table as one would a
            dictionary. Uses the hash function to find which
            bucket to insert into, then uses __getitem__ in the
            bucket
        '''
        hashed_key = self.hash(key)
        bucket = self.buckets[hashed_key]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket[i][1]
        return None

    def remove(self, key):
        '''
            Again: finds bucket, then finds value within bucket,
            then removes it using the LinkedList function
        '''
        hashed_key = self.hash(key)
        bucket = self.buckets[hashed_key]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                self.buckets[hashed_key].remove(i)
                return

    def __str__(self):
        '''
            Allows you to make this hashtable into a string
        '''
        retVal = ""
        for bucket in self.buckets:
            retVal += str(bucket) + "\n"
        return retVal

class Graph:

    def __init__(self, filename=None):
        if filename is None:
            self.amt_vertices = 0
            self.adj_list = [LinkedList() for i in range(amt_vertices)]
        else:
            with open(filename) as in_file:
                lines = [line.strip("\n") for line in in_file.readlines()]
                first_line = lines[0]
                amt_vertices = int(first_line)
                self.amt_vertices = int(first_line)
                self.adj_list = [LinkedList() for i in range(amt_vertices)]
                for line in lines[1:]:
                    nums = [int(num) for num in line.split(" ")]
                    self.mk_edge(nums[0], nums[1])

    def mk_edge(self, begin, end):
        self.adj_list[begin].append(end)

    def amt_vertices(self):
        return len(self.adj_list)

    def amt_edges(self):
        amt = 0
        for adj in self.adj_list:
            amt += len(adj)
        return amt

    def __str__(self):
        ret_val = ""
        for adj in self.adj_list:
            ret_val += str(adj) + "\n"
        return ret_val




