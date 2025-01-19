class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Додавання елемента в кінець списку
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Вивід списку
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування злиттям (merge sort)
    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head
        
        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None

        left = LinkedList()
        right = LinkedList()
        left.head = self.head
        right.head = next_to_middle

        left.merge_sort()
        right.merge_sort()

        self.head = self.sorted_merge(left.head, right.head)

    # Злиття двох відсортованих списків
    def sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left
        
        if left.value <= right.value:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        
        return result

    # Знайти середину списку
    def get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Об'єднання двох відсортованих списків
    @staticmethod
    def merge_lists(list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.value <= list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list