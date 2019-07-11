
class MinHeap(object):
    """
    simple min heap implemention
    two methods for building min heap, one by insert method, the other by build_from_array
    """

    def __init__(self):
        self.heap = [None]

    def len(self):
        return len(self.heap) - 1

    def insert(self, val):
        self.heap.append(val)
        insert_id = self.len()
        parent_id = insert_id // 2
        while parent_id >=1 and self.heap[insert_id] < self.heap[parent_id]:
            #swap
            self.heap[parent_id], self.heap[insert_id] = self.heap[insert_id], self.heap[parent_id]
            insert_id = insert_id // 2
            parent_id = parent_id // 2

    def min_heapify(self, parent_id):
        """
        Args: parent_id 
        Return: the length of the min heap
        Raises: None
        """
        left_child_id = 2 * parent_id
        right_child_id = 2 * parent_id + 1
        min_id = parent_id
        if left_child_id <= self.len() and self.heap[left_child_id] <= self.heap[min_id]:
            min_id = left_child_id

        if right_child_id <= self.len() and self.heap[right_child_id] <= self.heap[min_id]:
            min_id = right_child_id

        if min_id is not parent_id:
            self.heap[min_id], self.heap[parent_id] = self.heap[parent_id], self.heap[min_id]
            self.min_heapify(min_id)

    def build_min_heap(self, arr):
        self.heap = self.heap + arr
        mid_id = self.len() // 2
        for parent_id in range(mid_id, 0, -1):
            self.min_heapify(parent_id)

    def min(self):
        return self.heap[1]
    def decrease_heap_len(self):
        self.heap = self.heap[:-1]

    def heap_sort(self):
        """
        sort the min heap and output to an new arrary, assume the min heap has been built
        """
        new_heap = []
        while self.len() > 0:
            new_heap.append(self.min())
            #swap head and tail element
            self.heap[1], self.heap[self.len()] = self.heap[self.len()], self.heap[1]
            self.decrease_heap_len()
            self.min_heapify(1)

        return new_heap


    def print_heap(self):
        print self.heap[1:]

if __name__ == '__main__':
    '''
    arr = [7, 5, 2, 4, 3, 1, 0]
    print "raw arrary is ", arr
    min_heap = MinHeap()
    min_heap.build_min_heap(arr)
    print "array build heap ",
    min_heap.print_heap()
    print "array heap sort ", min_heap.heap_sort()
    '''
    min_heap = MinHeap()
    min_heap.insert(7)
    min_heap.insert(5)
    min_heap.insert(2)
    min_heap.insert(4)
    min_heap.insert(3)
    min_heap.insert(1)
    min_heap.insert(0)
    min_heap.insert(2)
    min_heap.print_heap()
    print min_heap.heap_sort()


