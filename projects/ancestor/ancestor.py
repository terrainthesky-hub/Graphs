
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, vertex):
            if vertex not in self.vertices:
                self.vertices[vertex] = set()

	def add_edge(self, v_from, v_to):
		if v_from in self.vertices and v_to in self.vertices:
			self.vertices[v_from].add(v_to)
		else:
			raise IndexError("nonexistent vertex")

def earliest_ancestor(ancestors, starting_node):
    #bfs queue
    g = Graph()
    for pair in ancestors:
            g.add_vertex(pair[0])
            g.add_vertex(pair[1])
            g.add_edge(pair[1], pair[0])

    q = Queue()
    max_path_len = 1
    
    oldest_ancestor = -1

    q.enqueue([starting_node])

    while q.size() > 0:

        path = q.dequeue()
        v = path[-1]

        if len(path) > max_path_len:
            max_path_len = len(path)
            oldest_ancestor = v
            print(v)
        elif len(path) >= max_path_len and v < oldest_ancestor:
            max_path_len = len(path)
            oldest_ancestor = v
            print(v)

        for neighbor in g.vertices[v]:
                new_path = path + [neighbor]
                print(new_path)
                q.enqueue(new_path)

    return oldest_ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 6)
