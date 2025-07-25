from pprint import pprint
import re

basis = r"""Rechts-minimal
F' = {B -> A, B -> C, CE -> B, BC -> B, BC -> E, E -> C, E -> D}

Links-minimal
F' ⊨ C -> B oder F' ⊨ E -> B? Ja, CE -> B wird durch E -> B ersetzt
F' ⊨ B -> B oder F' ⊨ C -> B? Ja, BC -> B wird durch B -> B ersetzt
F' ⊨ B -> E oder F' ⊨ C -> E? Ja, BC -> E wird durch B -> E ersetzt

F'' = {B -> A, B -> C, E -> B, B -> B, B -> E, E -> C, E -> D}

Redundanz
F'' \ {B -> A} ⊨ B -> A? Nein
F'' \ {B -> C} ⊨ B -> C? Ja
F'' \ {E -> B} ⊨ E -> B? Nein
F'' \ {B -> B} ⊨ B -> B? Ja
F'' \ {B -> E} ⊨ B -> E? Nein
F'' \ {E -> C} ⊨ E -> C? Nein
F'' \ {E -> D} ⊨ E -> D? Nein

F''' = {B -> A, E -> B, B -> E, E -> C, E -> D}"""

key = r"""K := ABCDE, F ⊨ K \ {A} → V? Ja  
K := BCDE, F ⊨ K \ {B} -> V? Ja  
K := CDE, F ⊨ K \ {C} -> V? Ja  
K := DE, F ⊨ K \ {D} -> V? Ja  
K := E, F ⊨ K \ {E} -> V? Nein  
Schlüssel: E"""

def membership_test_parser(basis_string):
    basis = [line for line in basis_string.splitlines() if line != ""]
    membership_test = {
        "Rechts-minimal": [], 
        "Links-minimal": [],
        "Redundanz": []
        }
    step = ""
    for line in basis:
        if line in {"Rechts-minimal", "Links-minimal", "Redundanz"}:
            step = line
        else:
            membership_test.get(step).append(line)
    
    r_min = membership_test["Rechts-minimal"]
    l_min = membership_test["Links-minimal"]
    redundand = membership_test["Redundanz"]

    for i in range(len(r_min)):
         if r_min[i].startswith("F'"):
             r_min[i] = functional_dependencies_parser(r_min[i])
    for i in range(len(l_min)):
        if l_min[i].startswith("F''"):
            l_min[i] = functional_dependencies_parser(l_min[i])
    for i in range(len(redundand)):
        if redundand[i].startswith("F'''"):
            redundand[i] = functional_dependencies_parser(redundand[i])

    return membership_test

def key_detemination_procedure(steps_string):
    steps = steps_string.replace(" ", "")
    return steps.split("\n")

def functional_dependencies_parser(fds_string):
    fds_string = re.findall(r"\{(?:[^{}]|{[^{}]*})*\}", fds_string)[0] # extract the funcional dependencies set
    fds_set = re.findall(r"(?:\{[^{}]+\}|\w+)\s*->\s*(?:\{[^{}]+\}|\w+)", fds_string) # splits the single dependencies
    parsed_set = []
    for dependency in fds_set: 
        parsed_set.append(single_dependency(dependency))
    return frozenset(parsed_set)

def single_dependency(dependency_string):
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

#pprint(membership_test_parser(basis))
#pprint(key_detemination_procedure(key))