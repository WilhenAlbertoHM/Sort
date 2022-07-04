# A data type that represents a node with the attributes of having a value and
# the node next to its current position.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# A data type representing a linked deque, where we can add/delete from the head and tail, check whether it is
# empty or not, and peek the first and last element of the deque.
class LinkedDeque:
    def __init__(self):
        self.head = None
        self.n = 0

    def size(self):
        return self.n

    # Returns whether the deque is empty or not.
    def isEmpty(self):
        return self.n == 0

    # Inserts a node from the head of the deque.
    def insertHead(self, val):
        node = Node(val)

        # If deque is empty, node is the only node.
        if not self.head:
            self.head = node
            self.n += 1

        # Otherwise, push front forward and add node to become the node in the front.
        else:
            node.next = self.head
            self.head = node
            self.n += 1

    # Inserts a node from the tail of the deque.
    def insertTail(self, val):
        node = Node(val)

        # If deque is empty, node is the only node.
        if not self.head:
            self.head = node
            self.n += 1

        # Otherwise, find the last node on the deque and add node to the last position.
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            self.n += 1

    # Deletes the node from the head of the deque.
    def deleteHead(self):
        # If the deque is empty, raise exception with the appropriate message.
        if self.isEmpty():
            raise Exception("Deque is empty")

        # Otherwise, set the head node to its next node and delete previous head node.
        temp = self.head
        self.head = self.head.next
        del temp
        self.n -= 1

    # Deletes the node from the tail of the deque.
    def deleteTail(self):
        # If the deque is empty, raise exception with the appropriate message.
        if self.isEmpty():
            raise Exception("Deque is empty")

        # Otherwise, find the second-to-last node and save it into prev,
        # push that second-to-last node to the tail node, and delete, making prev the tail node.
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = current.next
        del current
        self.n -= 1

    # Returns the value from the head node.
    def peekHead(self):
        # If the deque is empty, raise exception with the appropriate message.
        if self.isEmpty():
            raise Exception("Deque is empty")
        return self.head.val

    # Returns the value from the tail node.
    def peekTail(self):
        # If the deque is empty, raise exception with the appropriate message.
        if self.isEmpty():
            raise Exception("Deque is empty")
        current = self.head
        while current.next:
            current = current.next
        return current.val

    # Prints the deque.
    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += str(current.val) + ", "
            current = current.next

        # Remove last comma.
        res = res.strip(", ")

        if len(res):
            return "[" + res + "]"
        else:
            return "[]"


def _main():
    deque = LinkedDeque()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    deque.insertTail(n1)
    deque.insertHead(n2)
    deque.insertHead(n3)

    deque.head = n1
    n1.next = n2
    n2.next = n3

    print(deque)
    print("The size of this deque is:", deque.size())
    deque.deleteHead()
    print(deque)
    print("The size of the deque after deletion is:", deque.size())


if __name__ == '__main__':
    _main()
