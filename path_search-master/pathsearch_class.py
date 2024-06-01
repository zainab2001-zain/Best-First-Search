#3 classes
#1 queue
#2 Priority queue
#3 Node
#4 map

#Collections in Python are containers used for storing data and are commonly known as data structures,
# such as lists, tuples, arrays, dictionaries, etc.

import collections

#Heap queue is a special tree structure in which each parent node is less than or equal to its child node.
# In python it is implemented using the heapq module. It is very useful is implementing priority queues where
# the queue item with higher weight is given more priority in processing.

import heapq


class Queue:
    #constructor
    def __init__(self):
        self.elements = collections.deque()
        #A double-ended queue, or deque, has the feature of adding and removing elements from either end.

    #length of queue is 0 if queue is empty
    def empty(self):
        return len(self.elements) == 0

    #insertion
    def put(self, x):
        self.elements.append(x)

    #popleft() method is used to pop the first element or the element from the left side of the queue
    def get(self):
        return self.elements.popleft()

    #length of queue
    def len(self):
        return len(self.elements)

#a priority queue is an abstract data-type similar to a regular queue or stack data structure in which
# each element additionally has a "priority" associated with it. In a priority queue, an element with
# high priority is served before an element with low priority.

class PriorityQueue:
    def __init__(self):
        self.elements = [] #arary

    # length of queue is 0 if queue is empty
    def empty(self):
        return len(self.elements) == 0

    #Push the value item onto the heap, maintaining the heap invariant
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
                        #heap           item

    #Pop and return the smallest item from the heap, maintaining the heap invariant.
    def get(self):
        return heapq.heappop(self.elements)[1] #return second element

    #return leangth of the heap queue
    def len(self):
        return len(self.elements)

class Node:
    def __init__(self,position):
        self.pos = position
        self.xpos = position[0]
        self.ypos = position[1]
        self.parent = None
        self.visited = False
        self.queued = False
        self.distance = 10000
        self.priority = None


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
        self.Nodes = self.init_graph_node()

    def bounds_detect(self,result):

        return 0 <= result[0] <= self.width and 0 <= result[1] <= self.height
               #self<=value
    def collision_detect(self,result):
        for wall in self.walls:
            if wall[0]-1<result[0]<wall[0]+wall[2]+1 and wall[1]-1<result[1]<wall[1]+wall[3]+1:
                return False
        return True

    def neighbors(self, node):
        (x, y) = node
        results = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        results = filter(self.bounds_detect, results)#Python's filter() is a built-in function that allows you to
                                                     # process an iterable and extract those items that satisfy
                                                     # a given condition.
        results = filter(self.collision_detect, results)
        return results

    def init_graph_node(self):
        g = [[Node((j,i))for i in range(self.width+1)]
             for j in range(self.height+1)]

        return g



