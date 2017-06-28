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
                     you can use this class if you a heap that keeps that of a tuple
                     a value -> is an object that you want to retrieve from the heap
                     a key   -> is a weight that sorts the heap
"""


class MaxHeap:

    def __init__(self):
        self.heap = []

    def clear(self):
        self.heap = []

    @property
    def size(self):
        return len(self.heap)

    def parent(self, i):
        assert isinstance(i, int) and i < self.size, "i is a number less than %d" % self.size
        return (i-1) / 2 if i > 0 else 0

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
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def max_Heapify(self, i, heap_size):
        assert isinstance(i, int) and i < self.size and heap_size > 0, "i is a number less than %d" % self.size
        l = self.left(i)
        r = self.right(i)

        largest = i
        if l is not None and (l < heap_size) and (self.heap[l]['k'] > self.heap[i]['k']):
            print '\nLEFT: ', l, '=>', self.heap[l]['k'], ' x ', i, '=>', self.heap[i]['k']
            largest = l

        if r is not None and (r < heap_size) and (self.heap[r]['k'] > self.heap[largest]['k']):
            print 'RIGHT: ', r, '=>', self.heap[r]['k'], ' x ', largest, '=>', self.heap[largest]['k']
            largest = r

        print "%s:(%s, %s)" % (str(i),str(l),str(r)), 'largest = ', largest, 'k:', self.heap[largest]['k']
        if largest != i:
            print "follow ", largest
            self.exchange(i, largest)
            self.print_heap_keys()
            self.max_Heapify(largest, heap_size)

    def append(self, key, value):
        self.heap.append({'k':key, 'v': value, })

    def print_heap_keys(self):
        keys = [ "%i:%s" % (i, str(self.heap[i]['k'])) for i in range(self.size)]
        print keys

    def build_heap(self, values, keys):
        assert len(values) == len(keys), "the lists should be the same length"
        n = len(values)
        for i in range(n):
            self.append(key=keys[i], value=values[i])
        last = (self.size-1)/2
        print "\n\n\nBUILD HEAP"
        #print ">>>", range(last, -1, -1)
        for i in range(last, -1, -1):
            print "*** processing ", i
            self.max_Heapify(i, self.size)
            self.print_heap_keys()


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
        print "POP ==> ",max['k']
        self.print_heap_keys()
        if self.size > 1:
            self.max_Heapify(0, self.size)
        self.print_heap_keys()
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
        print i, "=>", new_weight
        self.heap[i]['k'] = new_weight
        while i > 0 and self.heap[self.parent(i)]['k'] < self.heap[i]['k']:
            self.print_heap_keys()
            self.exchange(i, self.parent(i))
            i = self.parent(i)
        self.print_heap_keys()

    def add(self, key, value):
        from sys import maxint
        self.append(key=-maxint, value=value)
        self.increase(self.size-1, key)


if __name__ == "__main__":
    import sys

    if False:
        a = MaxHeap()
        a.build_heap( keys=[27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0], values=range(14))
        print "only inserted the elements"
        print a.heap
        sys.exit(0)

    keys = []

    h = MaxPriorityQueue()
    h.build_heap(range(14), [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])

    print "SIZE", h.size,'\n'
    print "HEAP: ", h.heap
    print "MAX :", h.maximum
    print "SIZE", h.size,'\n'

    value = h.pop
    key = value['k']
    keys.append(key)
    print "POP :", key
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    value = h.pop
    key = value['k']
    keys.append(key)
    print "POP :", key
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'
    print keys

    print "MAX :", h.maximum
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'

    print "h.increase(1, 18)"
    h.increase(1, 18) # old: {'k': 9, 'v': 12}  new: {'k': 18, 'v': 12}
    print "HEAP: ", h.heap
    print "MAX :", h.maximum
    print "SIZE", h.size,'\n'
    print keys

    print "h.add(1000, 19)"
    h.add(key=19, value=1000)
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'
    print keys

    print "h.add(value=1001, key=17)"
    h.add(value=1001, key=18)
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'
    print keys

    # clean heap
    for i in range(h.size-1):
        value = h.pop
        key = value['k']
        keys.append(key)
        print "POP :", key
        print "HEAP: ", h.heap
        print "SIZE", h.size,'\n'
        print keys

    # pop last one
    value = h.pop
    key = value['k']
    keys.append(key)
    print "POP :", key
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'
    print keys

    # try to pop an empty heap
    print "POP :", h.pop
    print "HEAP: ", h.heap
    print "SIZE", h.size,'\n'
    print keys

    sys.exit(0)
