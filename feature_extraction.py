import networkx as nx
import pandas as pd
import numpy as np
import pysubgroup as ps

def graph_to_dataframe(graph):
    adjacency_matrix = nx.to_numpy_array(graph)
    return pd.DataFrame(adjacency_matrix, index=graph.nodes(), columns=graph.nodes())

class CustomNumericSelector(ps.SelectorBase):
    def __init__(self, attribute_name, lower_bound, upper_bound):
        self._attribute_name = attribute_name
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound

    def covers(self, data):
        attribute_values = data[self._attribute_name]
        return (attribute_values >= self._lower_bound) & (attribute_values <= self._upper_bound)

def frequent_subgraph_mining(training_graphs):
    # Combine all training graphs into a single graph
    combined_graph = nx.compose_all(training_graphs)
    
    # Convert the combined graph to DataFrame-like format
    combined_df = graph_to_dataframe(combined_graph)
    
    # Define the target variable
    target = ps.BinaryTarget('graph', True)
    
    # Create the search space (manually define selectors)
    custom_numeric_selector = CustomNumericSelector(attribute_name="weight", lower_bound=2, upper_bound=np.inf)
    searchspace = [custom_numeric_selector]
    
    # Define the subgroup discovery task
    task = ps.SubgroupDiscoveryTask(
        combined_df,
        target,
        searchspace,
        result_set_size=5,
        depth=3,
        qf=ps.WRAccQF())
    
    # Execute the task
    result = ps.DFS().execute(task)
    
    return result

def extract_features(training_graphs, frequent_subgraphs):
    # Extract features from training graphs based on frequent subgraphs
    feature_matrix = []
    for graph in training_graphs:
        features = []
        for subgraph in frequent_subgraphs:
            if nx.is_subgraph(graph, subgraph[0]):  # Subgraph is stored as (subgraph, score)
                features.append(1)
            else:
                features.append(0)
        feature_matrix.append(features)
    
    return np.array(feature_matrix)
