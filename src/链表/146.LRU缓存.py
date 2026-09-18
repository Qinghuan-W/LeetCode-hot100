class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node):
        previousNode = node.prev
        nextNode = node.next

        previousNode.next = nextNode
        nextNode.prev = previousNode

    def insert(self,node):
        previousNode = self.right.prev
        previousNode.next = node
        node.prev = previousNode
        node.next = self.right
        self.right.prev = node

    def get(self,key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self,key,value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.insert(node)

        else:
            node = Node(key,value)

            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.capacity:
                lru = self.left.next

                self.remove(lru)
                del self.cache[lru.key]


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))   # 1

cache.put(3, 3)

print(cache.get(2))   # -1

cache.put(4, 4)

print(cache.get(1))   # -1
print(cache.get(3))   # 3
print(cache.get(4))   # 4