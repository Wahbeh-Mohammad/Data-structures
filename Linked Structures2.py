class DoublyLinkedList: 
    class Node: 
        __slots__ = 'data','next','prev'
        def __init__(self, data): 
            self.data = data 
            self.next = None
            self.prev = None
        
        def __str__(self):
            return str(self.prev) + " <-> " + str(self.data) + " <->" + str(self.next)
         
    def __init__(self): 
        self.head = None

    def append(self, val): 
        new_node = DoublyLinkedList.Node(val) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 

    def insertAfter(self, prev_node, new_data): 
        if prev_node == None: 
            return 
        new_node = DoublyLinkedList.Node(new_data) 
        new_node.next = prev_node.next 
        prev_node.next = new_node  
        new_node.prev = prev_node
        if new_node.next is not None: 
            new_node.next.prev = new_node 
   
    def append(self, new_data): 
        new_node = DoublyLinkedList.Node(new_data) 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
    
    def min_item(self):
        head = self.head
        Min = head.data
        while(head != None):
            if head.data < Min:
                Min = head.data
            head = head.next
        return Min
        
    def delete_min(self):
        minitem = self.min_item()
        new = DoublyLinkedList()
        node = self.head
        while(node is not None):
            if node.data == minitem:
                node = node.next
                continue
            else:
                new.append(node.data)
            node = node.next
        self.head = new.head
    
    def printList(self): 
        node = self.head
        while(node is not None): 
            print(node.data,end=' -> ')
            node = node.next
        print(None)
        
L = DoublyLinkedList()
L.append(5);L.append(10);L.append(12)
L.append(1);L.append(50);L.append(1123)
L.printList()
print(L.min_item())
L.delete_min()
L.printList()