class Node:
    def __init__(self, data=None):
     self.data = data
     self.next = None


class LinkedList:
 def __init__(self):
   self.head = None
   
   

 def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

 def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

 def insert_after(self, prev_node: Node, data):
    if prev_node is None:
     print("Попереднього вузла не існує.")
     return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

 def delete_node(self, key: int):
   cur = self.head
   if cur and cur.data == key:
     self.head = cur.next
     cur = None
     return
   prev = None
   while cur and cur.data != key:
     prev = cur
     cur = cur.next
   if cur is None:
     return
   prev.next = cur.next
   cur = None

 def search_element(self, data: int) -> Node | None:
   cur = self.head
   while cur:
     if cur.data == data:
       return cur
     cur = cur.next
   return None

 def print_list(self):
   current = self.head
   while current:
     print(current.data,"-->", end="")
     current = current.next
   print('None')

 def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev    

 def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        # Розбиття списку на дві частини
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        # Рекурсивне сортування обох половин
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)
        # Злиття двох відсортованих половин
        sorted_list = self.sorted_merge(left, right)
        return sorted_list
 
 def get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
 
 def sorted_merge(self, a, b):
        result = None
        if a is None:
            return b
        if b is None:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        return result
 def merge_sorted_lists(self, list1, list2):
        # Використовуємо вище визначену функцію sorted_merge
        list1.head = list1.merge_sort(list1.head)
        list2.head = list2.merge_sort(list2.head)
        return self.sorted_merge(list1.head, list2.head)
if __name__ == '__main__':
    


 
 llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
    # Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)
    # Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()
llist.reverse()
    # Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()
llist.head = llist.merge_sort(llist.head)
    # Друк зв'язного списку
print("Зв'язний список відсортовано:")
llist.print_list()
new_llist = LinkedList()
    # Вставляємо вузли в початок
new_llist.insert_at_beginning(59)
new_llist.insert_at_beginning(20)
new_llist.insert_at_beginning(35)
new_llist.print_list()
llist.merge_sorted_lists(llist, new_llist)
    # Друк зв'язного списку
print("Зв'язний список відсортовано та замерджено:")
llist.print_list()


# def sortedMerge(self, a, b):
#     #result = None
        
#     if a.data <= b.data:
#         result = a
#         a = a.next
#     else:
#         result = b
#         b = b.next
#     current = result
#     while a and b:
#         if a.data <= b.data:
#             current.next = a
#             a = a.next
#         else:
#             current.next = b
#             b = b.next
#         current = current.next
#     if a is not None:
#         current.next = a
#     else:
#         current.next = b
#     return result    


#  def mergeSort(self, h):
        
#         # Base case if head is None
#         if h == None or h.next == None:
#             return h

#         # get the middle of the list 
#         middle = self.getMiddle(h)
#         nexttomiddle = middle.next

#         # set the next of middle node to None
#         middle.next = None

#         # Apply mergeSort on left list 
#         left = self.mergeSort(h)
        
#         # Apply mergeSort on right list
#         right = self.mergeSort(nexttomiddle)

#         # Merge the left and right lists 
#         sortedlist = self.sortedMerge(left, right)
#         return sortedlist
 
#  def getMiddle(self, head):
#         if (head == None):
#             return head

#         slow = head
#         fast = head

#         while (fast.next != None and 
#                fast.next.next != None):
#             slow = slow.next
#             fast = fast.next.next
            
#         return slow
