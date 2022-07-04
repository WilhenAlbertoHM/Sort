from LinkedDeque import LinkedDeque


# A program that sorts words from user input, line by line, inside a linked deque.
def main():
    # Create a deque and accept user input.
    d = LinkedDeque()
    print("Enter words here:")
    w = input()
    d.insertHead(w)

    # While user input is not empty...
    while w:
        w = input()
        # If the word from input, w, comes before the word in the front of the deque,
        # insert w into the front of the deque.
        if less(w, d.peekHead()):
            d.insertHead(w)

        # Also, if the word from input, w, comes after the word in the back of the deque,
        # insert w into the back of the deque.
        elif less(d.peekTail(), w):
            d.insertTail(w)

        # Otherwise, remove words that come before w from the front of the deque and
        # store them in a stack s. Then, add w to the front of the deque and add
        # words from s also to the front of the deque.
        else:
            s = []
            while less(d.peekHead(), w):
                s.append(d.deleteHead())
            d.insertHead(w)
            while not s:
                d.insertHead(s.pop())

    # Print the deque.
    print(d)


# Helper function that returns true if v is less than w.
def less(v, w):
    return v < w


if __name__ == '__main__':
    main()
