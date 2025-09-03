import re
import ast

graphs = [
    # Graph 1
    "G = ({T0, T1, T2, T3, TINF}, {(T0, T1), (T0, T2), (T0, T3), (T1, TINF), (T2, T3), (T3, T1), (T3, TINF)})",
    
    # Graph 2
    "G = ({T0, T1, T2, T3, TINF}, {(T0, T1), (T0, T2), (T1, T2), (T1, TINF), (T2, T1), (T2, T3), (T3, T1), (T3, T2), (T3, TINF)})"
]

def graph_definition_parser(string_graph):
    """This function converts a formal definition of a graph as String into Python datastructure.

    Args:
        string_graph (str): fomral definition of graph

    Returns:
        Tuple: formal definition of graph
    """
    string_graph = string_graph.split("=")
    string_graph = re.sub(r'\b(T\w+)\b', r'"\1"', string_graph[1])
    graph = ast.literal_eval(string_graph)
    return graph

# # For testing purposes
# for i in range(len(graphs)):
#     print(i)
#     print(graph_definition_parser(graphs[i]))
#     print("\n")