import networkx as nx
import numpy as np

def compute_similarity(graph1, graph2):
    # Find the isomorphism between graph1 and graph2
    matcher = nx.algorithms.isomorphism.GraphMatcher(graph1, graph2)
    # Get the mapping between nodes in graph1 and graph2
    isomorphism = matcher.isomorphisms_iter()
    
    # Check if any isomorphisms were found
    try:
        mcs_nodes = max(isomorphism, key=len)
    except ValueError:
        # If no isomorphisms found, similarity is zero
        return 0.0
    
    # Extract the largest common subgraph from the isomorphism
    mcs = graph1.subgraph(mcs_nodes)
    # Calculate the similarity based on the size of the MCS
    similarity = len(mcs.edges) / min(len(graph1.edges), len(graph2.edges))
    return similarity

def knn_classify(test_graph, training_graphs, labels, k):
    distances = []
    for i, train_graph in enumerate(training_graphs):
        similarity = compute_similarity(test_graph, train_graph)
        distances.append((similarity, labels[i]))  # Store similarity and corresponding label
    # Sort the distances based on similarity in descending order
    distances.sort(reverse=True)
    # Select the k-nearest neighbors
    nearest_neighbors = distances[:k]
    # Count the occurrences of each class among the nearest neighbors
    class_counts = {}
    for _, label in nearest_neighbors:
        class_counts[label] = class_counts.get(label, 0) + 1
    # Determine the majority class
    majority_class = max(class_counts, key=class_counts.get)
    return majority_class

# Example usage:
# test_graph = ...
# training_graphs = [...]
# labels = [...]  # Corresponding labels for training graphs
# k = 5
# predicted_class = knn_classify(test_graph, training_graphs, labels, k)
