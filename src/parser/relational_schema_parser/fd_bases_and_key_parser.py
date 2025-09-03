from pprint import pprint
import re

base = r"""Rechts-minimal
F' = {B -> A, B -> C, CE -> B, BC -> B, BC -> E, E -> C, E -> D}

Links-minimal
F'' = {B -> A, B -> C, E -> B, B -> B, B -> E, E -> C, E -> D}

Redundanz
F''' = {B -> A, E -> B, B -> E, E -> C, E -> D}"""
test = r"""LAND = ({Name, Hauptstadt, Landkreis, Einwohnerzahl, Fläche}, {Name -> {Hauptstadt, Landkreis, Einwohnerzahl, Fläche}})"""
test2 = r"""F''' = {B -> A,  B -> E, E -> C,E -> B, EB -> D}"""

key = r"""K := ABCDE, F ⊨ K \ {A} → V? Ja  
K := BCDE, F ⊨ K \ {B} -> V? Ja  
K := CDE, F ⊨ K \ {C} -> V? Ja  
K := DE, F ⊨ K \ {D} -> V? Ja  
K := E, F ⊨ K \ {E} -> V? Nein  
Schlüssel: E"""

def membership_test_parser(membership_string):
    """This funktion collects in datastructure transformed bases in a dict

    Args:
        membership_string (str): The 3 bases of a membership test

    Returns:
        Dict: recht/ links-minimal and redendaz as keys for bases
    """
    bases = re.split(r"(?=F'{1,3})", membership_string)
    membership_test = {}
    for base in bases:
        if "F'''" in base:
            membership_test.update({"redundanz": functional_dependencies_parser(base)})
        elif "F''" in base:
            membership_test.update({"links-minimal": functional_dependencies_parser(base)})
        elif "F'" in base:
            membership_test.update({"rechts-minimal": functional_dependencies_parser(base)})
    return membership_test
def base_parser(base_string):
    base, fd = base_string.split("=")
    return (base, functional_dependencies_parser(fd))

def key_detemination_procedure(steps_string):
    steps = steps_string.replace("\n", "").replace(" ", "").replace(",", "")
    return steps

def functional_dependencies_parser(fds_string):
    """This function transforms a set of functional dependencies into datactructure

    Args:
        fds_string (str): i.e. F = {a->b, c->d, ...}

    Returns:
        Frozenset: Frozenset containing all dependencies
    """
    #fds_string = re.findall(r"\{(?:[^{}]|{[^{}]*})*\}", fds_string)[0] # extract the funcional dependencies set
    fds_set = re.findall(r"(?:\{[^{}]+\}|\w+)\s*->\s*(?:\{[^{}]+\}|\w+)", fds_string) # splits the single dependencies
    parsed_set = []
    for dependency in fds_set: 
        parsed_set.append(single_dependency(dependency))
    return frozenset(parsed_set)

def single_dependency(dependency_string):
    """This funktion takes a functional dependency (x -> y) and forms it into datastructure

    Args:
        dependency_string (string): functional dependency: x -> y

    Returns:
        Tuple(fSet, fSet): lhs -> rhs
    """
    dependency_string = clean_string(dependency_string)
    lhs, rhs = dependency_string.split("->")
    rhs_set = frozenset(rhs.split(","))
    lhs_set = frozenset(lhs.split(","))
    return (lhs_set, rhs_set) 

def set_parser(attributes):
    attributes = clean_string(attributes)
    attributes = attributes.split(",")
    return frozenset(attributes)

def clean_string(string):
    string = string.replace("{", "").replace("}", "").replace(" ", "")
    return string

#pprint(membership_test_parser(base))
#pprint(key_detemination_procedure(key))
#pprint(functional_dependencies_parser(test))