import re
import ast

graph = """G = ({T1, T2, T3, T4}, {(T1, T2), (T1, T3), (T3, T4), (T2, T4)})"""

def graph_definition_parser(string_graph):
    string_graph = string_graph.split("=")
    string_graph = re.sub(r'\b(T\d+)\b', r'"\1"', string_graph[1])
    graph = ast.literal_eval(string_graph)
    return graph

#print(graph_definition_parser(graph))
