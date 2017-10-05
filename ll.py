class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class TreeNode:

    def __init__(self, value):
        self.value = value
        self.l_child = None
        self.r_child = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, newVal):
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
        temp = self.head
        for i in range(index):
            temp = temp.next
        temp.value = newVal

    def remove_from_back(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        self.length -= 1

    def remove_from_front(self):
        self.head = self.head.next
        self.length -= 1

    def remove(self, index):
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
        if index < 0:
            raise ValueError("Index < 0")
        elif index >= 0 and index < self.length:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            return temp.value
        elif index >= self.length:
            raise ValueError("Index >= length of list")

    def indexOf(self, value):
        temp = self.head
        index = 0
        while temp is not None:
            if temp.value == value:
                return idx
            idx += 1
        return -1

    def __len__(self):
        return self.length

    def __str__(self):
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
        self.values = LinkedList()

    def add(self, value):
        self.values.prepend(value)

    def remove(self):
        i = self.values.head.value
        self.values.remove_from_front()
        return i

    def itemAt(self, index):
        return self.values.itemAt(index)

    def indexOf(self, value):
        return self.values.indexOf(value)

    def __len__(self):
        return self.values.length

    def __str__(self):
        return str(self.values)

class Queue:

    def __init__(self):
        self.values = LinkedList()

    def add(self, newVal):
        self.values.append(newVal)

    def remove(self):
        i = self.values.head.value
        self.values.remove_from_front()
        return i

    def itemAt(self, index):
        return self.values.itemAt(index)

    def indexOf(self, value):
        return self.values.indexOf(value)

    def __len__(self):
        return self.values.length

    def __str__(self):
        return str(self.values)

class Binary_Search_Tree:

    def __init__(self):
        self.root = None

    def add(self, newVal):
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
        if temp is None:
            return 0
        if temp.l_child is None and temp.r_child is None:
            return 1
        return self.get_length(temp.l_child) + 1 + self.get_length(temp.r_child)

    def get_height(self, temp):
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
        temp = self.root
        return self.get_height(temp)

    def lookup(self, lookup_val):
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
        temp = self.root.left
        while temp.right is not None:
            temp = temp.right
        return temp.value

    def delete(self, del_val):
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
        temp = self.root
        return self.get_length(temp)
