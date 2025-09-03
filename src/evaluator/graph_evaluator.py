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
(T1, T2), (T1, TIxNF), 
(T3, T1), (T3, T2), (T3, TINF)})"""

def graph_evaluator(ref, sub):
    """This funtion checks two formal graph definitions on equality.

    Args:
        ref (str): formal graph definition
        sub (str): formal graph definition

    Returns:
        Boolean: When False, the source of error is added
    """
    diff = DeepDiff((gp.graph_definition_parser(ref)), (gp.graph_definition_parser(sub)))
    if not diff:
        return True
    else:
        return False, diff

#for testing purposes
#print(graph_evaluator(ref,sub))