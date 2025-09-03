from deepdiff import DeepDiff
from parser.graph_definition_parser import graph_definition_parser as gp

sub="""G = ({T0, T1, T2, T3, TINF}, 
{(T0, T1), (T0, T2), 
(T1, T2), (T1, TINF), 
(T2, T1), (T2, T3), 
(T3, T1), (T3, T2), (T3, TINF)})"""
ref="""G = ({T1, T2, T0, T3, TINF}, 
{ (T2, T1), (T2, T3),
(T0, T1), (T0, T2), 
(T1, T2), (T1, TINF), 
(T3, T1), (T3, T2), (T3, TINF)})"""

print(gp.graph_definition_parser(sub) == gp.graph_definition_parser(ref))
