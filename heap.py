# -*- coding: utf-8 -*-
"""
@@@  @@@  @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@@@@    @@@@@@
@@@  @@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@
@@!  @@@      @@@  @@!  @@@  @@!       @@! @@! @@!  @@!  @@@
!@!  @!@      @!@  !@!  @!@  !@!       !@! !@! !@!  !@!  @!@
@!@!@!@!  @!@!!@   @!@  !@!  @!!!:!    @!! !!@ @!@  @!@!@!@!
!!!@!!!!  !!@!@!   !@!  !!!  !!!!!:    !@!   ! !@!  !!!@!!!!
!!:  !!!      !!:  !!:  !!!  !!:       !!:     !!:  !!:  !!!
:!:  !:!      :!:  :!:  !:!  :!:       :!:     :!:  :!:  !:!
::   :::  :: ::::   :::: ::   :: ::::  :::     ::   ::   :::
 :   : :   : : :   :: :  :   : :: ::    :      :     :   : :

 * priority-queue, Copyright (c) 2016-2017, Henrique Moura (h3dema)
 * All rights reserved.
 *
 * If you have questions about your rights to use or distribute this
 * software, please contact h3dema@outlook.com.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. All advertising materials mentioning features or use of this software
 *    must display the following acknowledgement:
 * 4. Neither the name of author nor the names of its
 *    contributors may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE H3DEMA AND CONTRIBUTORS
 * ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
 * TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE FOUNDATION OR CONTRIBUTORS
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
"""
"""

This python module implements two classes:

* MaxHeap:  implements a max heap
* MaxPriorityQueue : implements a max-priority queue with HEAP
                     you can use this class if you a heap that keeps that of a tuple
                     a value -> is an object that you want to retrieve from the heap
                     a key   -> is a weight that sorts the heap
                     
Reference: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein. 
           Introduction to Algorithms. Third Edition. Chapter 6.                   
                    
"""


class MaxHeap(object):
    """
        this class implements a max heap, and performs some functions
        * clear: resets the heap to an empty heap
        * build_heap: constructs a heap for a list of values
        * max_heapify: performs the MAX HEAPIFY, see section 6.2 from CLRS
        * parent, left, right
    """
    def __init__(self):
        """initialize the heap internal variable"""
        self.__heap = []

    def clear(self):
        """clears the heap"""
        self.__heap = []

    @property
    def size(self):
        """
        Size of the Heap
        :return: number of objects in the heap 
        """
        return len(self.__heap)

    @property
    def peek(self):
        return self.__heap[0] if self.size > 0 else None

    @property
    def heap(self):
        return self.__heap

    def parent(self, element_id):
        """
        
        :param element_id: number of the element in the Heap
        :return: it's parent, if element_id = 0 (root) then returns the root 
        """
        assert isinstance(element_id, int) and element_id < self.size, "element_id is a number less than %d" % self.size
        return (element_id - 1) / 2 if element_id > 0 else 0

    def left(self, i):
        """left child position or None if it doesn't exist """
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        v = 2 * i + 1
        return v if v < self.size else None

    def right(self, i):
        """right child position or None if it doesn't exist """
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        v = 2 * i + 2
        return v if v < self.size else None

    def exchange(self, i, j):
        temp = self.__heap[i]
        self.__heap[i] = self.__heap[j]
        self.__heap[j] = temp

    def max_Heapify(self, i, heap_size):
        assert isinstance(i, int) and i < self.size and heap_size > 0, "i is a number less than %d" % self.size
        l = self.left(i)
        r = self.right(i)

        largest = i
        if l is not None and (l < heap_size) and (self.__heap[l]['k'] > self.__heap[i]['k']):
            largest = l

        if r is not None and (r < heap_size) and (self.__heap[r]['k'] > self.__heap[largest]['k']):
            largest = r

        if largest != i:
            self.exchange(i, largest)
            self.max_Heapify(largest, heap_size)

    def append(self, weight, value):
        self.__heap.append({'k':weight, 'v': value, })

    @property
    def keys(self):
        """        
        :return: a list of the keys (weights) in the order 
        """
        __keys = [ "%i:%s" % (i, str(self.__heap[i]['k'])) for i in range(self.size)]
        return __keys

    def reorder(self):
        last = (self.size-1)/2
        for i in range(last, -1, -1):
            self.max_Heapify(i, self.size)

    def build_heap(self, values, keys):
        """
        this method get a list of values and a list of keys (weights) and builds a __heap with them
        :param values: list of objects that you want to put in the __heap
        :param keys: list of values that provides the order of the objects in the __heap
        :return: nothing
        """
        assert len(values) == len(keys), "the lists should be the same length"
        n = len(values)
        for i in range(n):
            self.append(weight=keys[i], value=values[i])
        self.reorder()

    def heapsort(self):
        """ sorts the heap
            after this method, the self.heap list is ordered in ascending order
            so it is no longer a heap, it is a sorted array
            to repair it, run self.reorder()
        """
        heap_size = self.size
        for i in range(heap_size, 0, -1):
            self.exchange(0,i)
            heap_size -= 1
            self.max_Heapify(0,heap_size)


class MaxPriorityQueue(MaxHeap):
    """
        max-priority queue keeps track of the values and their relative priorities
        implements
        * MAXIMUM: returns the element of __heap with the largest key.
        * POP: inserts the element x into the __heap, is equivalent to EXTRACT-MAX that removes and returns the element of __heap with the largest key
        * INCREASE: implements INCREASE-KEY. increases the value of element x’s key to the new value k, which is assumed to be at least as large as x’s current key value.
        * ADD
    """
    def __init__(self):
        super(MaxPriorityQueue, self).__init__()

    @property
    def maximum(self):
        """just returns the maximum, doesn't modifies the heap 
            :return max value in the heap
        """
        return self.peek

    @property
    def pop(self):
        """ pop extracts the maximum e rebuilds the __heap
            The running time of is O(lg n)
            :return max value in the __heap, if the __heap is empty returns None
        """
        if self.size == 0:
            return None
        else:
            max = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap.pop() # remove the last item

            if self.size > 1:
                self.max_Heapify(0, self.size)
            return max

    def increase(self, element_id, new_weight):
        """
        HEAP-INCREASE-KEY on an n-element __heap is O(lg n)
        :param element_id: element we want to increase the key (weight)
        :param new_weight: nwe value
        """
        assert isinstance(element_id, int) and element_id < self.size, "element_id is a number less than %d" % self.size
        if new_weight < self.heap[element_id]['k']:
            raise Exception('new key is smaller than current key')
        self.heap[element_id]['k'] = new_weight
        while element_id > 0 and self.heap[self.parent(element_id)]['k'] < self.heap[element_id]['k']:
            self.exchange(element_id, self.parent(element_id))
            element_id = self.parent(element_id)

    def add(self, key, value):
        from sys import maxint
        self.append(weight=-maxint, value=value)
        self.increase(self.size-1, key)

    def print_heap_keys(self):
        print self.keys


if __name__ == "__main__":
    import sys

    if False:
        a = MaxHeap()
        a.build_heap( keys=[27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0], values=range(14))
        print a.print_heap_keys()
        sys.exit(0)

    poped_keys = []

    import random
    n = random.randint(5,30)
    #keys = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    keys = [random.randint(1,100) for i in range(n)]
    print "Original keys: ", keys
    h = MaxPriorityQueue()
    print "Creating a heap with", len(keys),"elements"
    h.build_heap(keys=keys, values=range(len(keys)))
    print "SIZE:", h.size,'\n'

    print "HEAP: ", h.keys
    print "MAX :", h.maximum
    print "SIZE:", h.size,'\n'

    value = h.pop
    key = value['k']
    poped_keys.append(key)
    print "POP :", key
    print "HEAP: ", h.print_heap_keys()
    print "SIZE:", h.size,'\n'

    value = h.pop
    key = value['k']
    poped_keys.append(key)
    print "POP  :", key
    print "HEAP : ", h.keys
    print "SIZE :", h.size,'\n'
    print "Poped: ", poped_keys

    print "MAX :", h.maximum
    print "HEAP: ", h.keys
    print "SIZE:", h.size,'\n'

    v = h.heap[1]['k'] + 5
    print "h.increase(1, %d)" % v
    h.increase(1, v)
    print "HEAP : ", h.keys
    print "MAX  :", h.maximum
    print "SIZE :", h.size,'\n'
    print "Poped: ", poped_keys

    print "h.add(1000, 19)"
    h.add(key=19, value=1000)
    print "HEAP : ", h.keys
    print "SIZE :", h.size,'\n'
    print "Poped: ", poped_keys

    print "h.add(value=1001, key=17)"
    h.add(value=1001, key=17)
    print "HEAP : ", h.keys
    print "SIZE :", h.size,'\n'
    print "Poped: ", poped_keys

    # clean __heap
    for i in range(h.size-1):
        value = h.pop
        key = value['k']
        poped_keys.append(key)
        print "POP  :", key
        print "HEAP : ", h.keys
        print "SIZE :", h.size,'\n'
        print "Poped: ", poped_keys

    # pop last one
    value = h.pop
    key = value['k']
    poped_keys.append(key)
    print "POP  :", key
    print "HEAP : ", h.keys
    print "SIZE :", h.size,'\n'
    print "Poped: ", poped_keys

    # try to pop an empty __heap
    print "POP  :", h.pop
    print "HEAP : ", h.keys
    print "SIZE :", h.size,'\n'

    print "Poped   :", poped_keys
    keys.extend([19,17])
    print "Original:",sorted(keys, reverse=True) # original keys sorted (two discrepancies: we inserted 19 and 17)
    print "note: value ", v - 5, "changed to", v
