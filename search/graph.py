import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if end == None:
            return self._bfs_traversal(start)
        return self._bfs_shortest_path(start, end)
    
    def _bfs_traversal(self, start):
        queue = []
        visited = []
        queue.append(start)
        visited.append(start)
        while len(queue) != 0:
            current_vertext = queue.pop(0)
            neighbors = self.graph.successors(current_vertext)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
        return visited
    
    def _bfs_shortest_path(self, start, end):
        parents = {}
        queue = []
        queue.append(start)
        parents[start] = None
        while len(queue) != 0:
            current_vertext = queue.pop(0)
            neighbors = self.graph.successors(current_vertext)
            for neighbor in neighbors:
                if neighbor not in parents:
                    parents[neighbor] = current_vertext
                    queue.append(neighbor)
        # check if path exists
        if parents.get(end) is None:
            return None
        # now gather shortest path from start->end in reverse order
        shortest_path_reverse = [end]
        current_vertext = end
        while parents[current_vertext] != None:
            current_vertext = parents[current_vertext]
            shortest_path_reverse.append(current_vertext)
        # now reverse child->parent ordering, make it parent->child
        shortest_path = []
        i = len(shortest_path_reverse) - 1
        while i >= 0:
            shortest_path.append(shortest_path_reverse[i])
            i -= 1
        return shortest_path


        

