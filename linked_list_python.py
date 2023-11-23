#Linked List 
#007


#Create Node
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

#Create Linked List
class LinkedList:
  #Ceate a new node in LinkedList
  def __init__(self,value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1
  #Print the linked list
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next
  #Apeend will add a value into to end of the linked list
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
  #Prepend function will add value in the start of the Linked list
  def prepend(self,value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head = new_node
    self.length += 1
    return True
  #Delete a element from a linked list
  def pop(self):
    if self.length == 0:
      return None
    temp = self.head
    pre = self.head
    while(temp.next):
      pre = temp
      temp = temp.next
      temp.next = None
    self.tail = pre
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp.value
  #Delete the first element of a Linked List
  def pop_first(self):
    if self.length == 0:
      return None
    temp = self.head
    self.head = self.head.next
    temp.next = None
    self.length -= 1
    if self.length == 0:
      self.tail = None
    return temp
  #See a value in a speific index
  def get(self,index):
    if index < 0 or index >= self.length:
      return None
    temp = self.head
    for i in range(index):
      temp = temp.next
    return temp.value
  #Set Value to a LinkedList to a specific index
  def set_value(self, index, value):
    if index < 0 or index >= self.length:
        return False  # Index out of bounds

    temp = self.head
    for i in range(index):
        temp = temp.next

    temp.value = value
    return True
  #Insert
  def insert(self, index, value):
    if index < 0 or index > self.length:
        return False  # Index out of bounds

    if index == 0:
        return self.prepend(value)

    if index == self.length:
        return self.append(value)

    new_node = Node(value)
    temp = self.head
    for i in range(index - 1):
        temp = temp.next

    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
  #Remove any values form LinkedList
  def get(self, index):
    if index < 0 or index >= self.length:
        return None  # Index out of bounds

    temp = self.head
    for i in range(index):
        temp = temp.next

    return temp

  def remove(self, index):
    if index < 0 or index >= self.length:
        return None  # Index out of bounds

    if index == 0:
        return self.pop_first()

    prev = self.get(index - 1)
    if prev is None or prev.next is None:
        return None

    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -= 1

    if self.length == 1:
        self.tail = self.head

    if self.length == 0:
        self.head = None
        self.tail = None

    return temp.value
#Reverse a linked list
  def reverse(self):
    temp = self.head
    self.tail = temp
    after = temp.next
    before = None
    for i in range(self.length):
      after = temp.next
      temp.next = before
      before = temp 
      temp = after
    self.head = before

#Pop in linked list
#Remove item in the end

new_linked_list = LinkedList(1)
new_linked_list.append(45)
new_linked_list.append(50)
new_linked_list.append(43)
new_linked_list.append(109)
new_linked_list.prepend(36)
new_linked_list.append(7)
new_linked_list.set_value(0,8)
new_linked_list.set_value(1,45)
new_linked_list.insert(6,23)
new_linked_list.remove(0)
new_linked_list.remove(0)
# print(new_linked_list.pop_first())


new_linked_list.prepend(23)
new_linked_list.prepend(10)
# print(new_linked_list.pop())
# print(new_linked_list.pop())
# print(new_linked_list.pop())
# print(new_linked_list.pop())

new_linked_list.reverse()
new_linked_list.print_list()



#Nirban Mitra Joy