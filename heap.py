#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
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

"""


class MaxHeap:

    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def clear(self):
        self.heap = []
        self.heap_size = 0

    @property
    def size(self):
        return len(self.heap)

    def parent(self, i):
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        return i / 2

    def left(self, i):
        """left child position or None if it doesn't exist """
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        v = 2 * i
        return v if v < self.size else None

    def right(self, i):
        """right child position or None if it doesn't exist """
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        v = 2 * i + 1
        return v if v < self.size else None

    def exchange(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def max_Heapify(self, i):
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        l = self.left(i)
        r = self.right(i)
        if l is not None and (l < self.heap_size) and (self.heap[l]['k'] > self.heap[i]['k']):
            largest = l
        else:
            largest = i
        if r is not None and (r < self.heap_size) and (self.heap[r]['k'] > self.heap[largest]['k']):
            largest = r
        if largest != i:
            self.exchange(i, largest)
            self.max_Heapify(largest)

    def append(self, v, k):
        self.heap.append({'k':k, 'v': v, })

    def build_heap(self, values, weights):
        assert len(values) == len(weights), "the lists should be the same length"
        n = len(values)
        for i in range(n):
            self.append(values[i], weights[i])
        self.heap_size = len(self.heap)

    def sort(self):
        self.heap_size = len(self.heap)
        for i in range(n/2, 1, -1):
            self.exchange(0, i)
            self.heap_size -= 1
            self.max_Heapify(0)

        self.heap_size = len(self.heap)

        return self.heap


class MaxPriorityQueue(MaxHeap):
    """
        max-priority queue keeps track of the values and their relative priorities
        implements
        * MAXIMUM: returns the element of heap with the largest key.
        * POP: inserts the element x into the heap, is equivalent to EXTRACT-MAX that removes and returns the element of heap with the largest key
        * INCREASE: implements INCREASE-KEY. increases the value of element x’s key to the new value k, which is assumed to be at least as large as x’s current key value.
        * ADD
    """

    @property
    def maximum(self):
        """just returns the maximum, doesn't modifies the heap 
            :return max value in the heap
        """
        return self.heap[0]

    @property
    def pop(self):
        """ pop is HEAP-EXTRACT-MAX
            it extracts the maximum e rebuilds the heap
            The running time of is O(lg n)
            :return max value in the heap
        """
        if len(self.heap) == 0:
            return None
            #raise Exception('heap is empty')
        max = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.heap.pop() # remove the last item
        self.heap_size -= 1
        if self.heap_size > 0:
            self.max_Heapify(0)
        return max

    def increase(self,i,new_weight):
        """
        HEAP-INCREASE-KEY on an n-element heap is O(lg n)
        :param i: element we want to increase the key (weight)
        :param new_weight: nwe value
        """
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        if new_weight < self.heap[i]['k']:
            raise Exception('new key is smaller than current key')
        self.heap[i]['k'] = new_weight
        while i > 0 and self.heap[self.parent(i)]['k'] < self.heap[i]['k']:
            self.exchange(i, self.parent(i))
            i = self.parent(i)

    def add(self, v, k):
        from sys import maxint
        self.append(v, -maxint)
        self.heap_size += 1
        self.increase(self.heap_size-1, k)


if __name__ == "__main__":
    h = MaxPriorityQueue()
    h.build_heap(range(14), [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
    print "SIZE", h.size,'\n'
    print "HEAP: ", h.heap
    print "MAX :", h.maximum

    print "POP :", h.pop
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    print "POP :", h.pop
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    print "MAX :", h.maximum
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    h.increase(1, 18) # old: {'k': 9, 'v': 12}  new: {'k': 18, 'v': 12}
    print "HEAP: ", h.heap
    print "MAX :", h.maximum
    print "SIZE", h.size,'\n'

    print "h.add(1000, 19)"
    h.add(1000, 19)
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    print "h.add(1001, 18)"
    h.add(1001, 18)
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    # clean heap
    for i in range(h.size-1):
        print "POP :", h.pop
        print "HEAP: ", h.heap
        print "SIZE", h.size,'\n'

    # pop last one
    print "POP :", h.pop
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    # try to pop an empty heap
    print "POP :", h.pop
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'
