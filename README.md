Priority-queue
================

A class that implements max-heap and max-priority queue in python.

A priority queue is an data type similar to a queue, but where each element has a "priority" associated with it.
In a priority queue, an element with high priority is served before an element with low priority. 
If two elements have the same priority, they are served according to their order in the queue.


USAGE
=====

1) Create a max-priority queue object

```python
    h = MaxPriorityQueue()
```

2) Fill the heap using build_heap(values, weights).
Values is a list of the elements you want to keep in the heap, and weights is a list of integer that act as the keys (or weights/priorities) for the elements. Both list should be the same length.

```python
    h.build_heap(range(14), [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0])
```

3) to retrieve the maximum value in the heap, use 

```python
  print "MAX :", h.maximum
```

4) to retrieve the maximum value in the heap and extract it from the heap, use

```python
print "POP :", h.pop
```

5) to change the weight of a element, use increase(element position, new weight value).
Note that as this is a max-priority queue, you can only increase the priority.

```python
h.increase(1, 18) # old: {'k': 16, 'v': 3}  new: {'k': 18, 'v': 3}
```
