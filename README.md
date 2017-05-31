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
Note that values is a list of any kind of object.

```python
    values = range(14) # elements are tagged from 0 to 13
    weights = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0] # e.g element #1 has a priority of 27
    h.build_heap(values, weights)
```

3) to retrieve the maximum value in the heap, use 

```python
    print "MAX :", h.maximum   # {'k': 27, 'v': 0}
```

4) to retrieve the maximum value in the heap and extract it from the heap, use

```python
    print "POP :", h.pop        # prints {'k': 27, 'v': 0} and remove this element from the heap
```

5) to change the weight of a element, use increase(element position, new weight value).
Note that as this is a max-priority queue, you can only increase the priority.

```python
    h.increase(1, 18) # old: {'k': 16, 'v': 3}  new: {'k': 18, 'v': 3}
```
