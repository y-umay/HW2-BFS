# write tests for bfs
import pytest
import search
import networkx as nx


def verify_bfs_order(graph_file, start_node):
    """
    Generates a traversal order as a comparision point 
    for BFS implementation validation
    """
    graph = nx.read_adjlist(graph_file, create_using=nx.DiGraph, delimiter=";")
    bfs_order = list(nx.bfs_edges(graph, start_node))
    nodes_in_order = [start_node] + [edge[1] for edge in bfs_order]
    return nodes_in_order

def verify_shortest_path(file, start, end):
    """
    Generates the shortest path as a comparision point 
    for BFS implementation validation
    """
    graph = nx.read_adjlist(file, create_using=nx.DiGraph, delimiter=";")
    shortest_expected_path = nx.shortest_path(graph, source=start, target=end)
    return shortest_expected_path
    
def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    graph = search.Graph("data/tiny_network.adjlist")
    # Generate traversal using BFS implementation
    traversal = graph.bfs("Luke Gilbert")
    len_traversal = len(traversal)
    # Generate expected order using networkx
    expected_traversal = verify_bfs_order("data/tiny_network.adjlist", "Luke Gilbert")
    len_expected_traversal = len(expected_traversal)
    # Assert both orders match
    assert traversal == expected_traversal, "The order of nodes is not right."
    # Assert both number of nodes match
    assert len_traversal == len_expected_traversal, "The number of nodes is not right."

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    # Get the shortest path using BFS implementation
    graph = search.Graph("data/citation_network.adjlist")
    shortest_path = graph.bfs("Luke Gilbert", "Hani Goodarzi")
    # Generate the shortest expected path using networkx
    expected_shortest_path = verify_shortest_path("data/citation_network.adjlist", "Luke Gilbert", "Hani Goodarzi")
    # Assert that the returned shortest path matches the expected shortest path
    assert shortest_path == expected_shortest_path, f"Expected {expected_shortest_path}, but got {shortest_path}."
    #Test disconnected nodes
    no_path = graph.bfs("34803213", "Brian Shoichet")
    assert no_path is None, "Nonexistent node is found."
    #Test non-existent start node
    with pytest.raises(KeyError):
        graph.bfs("NonExistentStartNode", "Luke Gilbert")
    #Test non-existent end node
    with pytest.raises(KeyError):
        graph.bfs("Luke Gilbert", "NonExistentEndNode")

    