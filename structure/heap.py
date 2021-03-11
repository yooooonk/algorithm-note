class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        heap = self.items;
        heap.append(value)
        cur = len(heap)-1
        while cur>1:
            parent = cur//2
            if heap[cur]>heap[parent] :
                heap[cur],heap[parent] = heap[parent],heap[cur]
                cur = parent
            else :
                break;        
    
    def delete(self):
        # 구현해보세요!
        return 8  # 8 을 반환해야 합니다.

""" max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!  

 """

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]