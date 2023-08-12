class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) +"->", end="")
        head = head.next
    print("None")
    return

def length(head):
    count = 0
    temp = head
    while temp is not None:
        temp = temp.next
        count = count+1
    return count

def insertIth(head, data, i):
    cnt = 1
    prev = None
    curr = head
    new_node = Node(data)
    if i == 0:
        new_node.next = head
        head = new_node
        return head
    elif i > length(head) or i < 0:
        print("Can't insert linked out of range")
        return head
    else:
        while curr is not None and cnt <= i:
            prev = curr
            curr = curr.next
            cnt = cnt+1
        prev.next = new_node   #type: ignore
        new_node.next = curr
        return head

def delete_node(head, pos):
    if pos < 0 or head is None:
        return head
    if pos == 0:
        head = head.next
        return head
    curr = head
    prev = None
    count = 0
    while curr.next is not None and count < pos:
        prev = curr
        curr = curr.next
        count = count +1
    if curr is None:
        return head
    prev.next = curr.next   #type: ignore
    return head

def find_node(head, x):
    count = 0
    curr = head
    while curr.next is not None:
        if curr.data == x:
            return count
        count = count +1
        curr = curr+1
    return -1

#print ith node
def ithNode(head, i):
    count = 0
    temp = head
    while temp.next is not None:
        if count == i:
            return temp.data
        temp = temp.next
        count = count+1
    return -1

def take_input():
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currdata in inputList:
        if currdata == -1:
            break
        newNode = Node(currdata)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode   #type: ignore
            tail = newNode
    return head

def lastNodetoFirst(head, n):
    slow = head
    fast = head
    mid = head
    count = 1
    if n == 0 or head is None:
        return head
    while count < n-1:
        fast = fast.next
        count = count+1
    mid = fast.next
    temp = mid
    fast.next = None
    while mid.next is not None:
        mid = mid.next
    mid.next = slow
    head = temp
    return head

def removeDuplicate(head):
    if head is None or head.next is None:
        return head
    curr = head
    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
        
    return head

def reverse_linkedList(head):
    curr = head
    prev = None
    while curr is not None:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def isPalidrome(head):
    num = []
    while head is not None:
        num.append(head.data)
        head = head.next
    l = 0
    r = len(num) -1
    while l <= r:
        if num[l] != num[r]:
            return False
        l  = l+1
        r = r-1
    return True

def reverse_recursion(head):
    if head is None or head.next is None:
        return head
    small_head = reverse_recursion(head.next)
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = head
    head.next = None
    return small_head

def midpoint(head):
    if head is None:
        return head
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow.data

def mergeTwoSortedLinkedLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    new_head, new_tail = None, None
    if head1.data < head2.data:
        new_head = head1
        new_tail = head1
        head1 = head1.next
    else:
        new_head = head2
        new_tail = head2
        head2 = head2.next
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            new_tail.next = head1
            new_tail = new_tail.next
            head1 = head1.next
        else:
            new_tail.next = head2
            new_tail = new_tail.next
            head2 = head2.next
    if head1 is not None:
        new_tail.next = head1
    if head2 is not None:
        new_tail.next = head2
    return new_head

head = take_input()
printLL(head)

head2 = take_input()
printLL(head2)

head = mergeTwoSortedLinkedLists(head, head2)
printLL(head)