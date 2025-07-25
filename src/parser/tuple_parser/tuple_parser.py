asw = """A = direkt abhängig
B = transitiv abhängig
C = transitiv abhängig
D = direkt abhängig
E = direkt abhängig"""

asw2 = """Min = 0 
Max = n"""

def tuple_parser(string_tuple):
    tuple_set = set()
    for string_tuple in string_tuple.splitlines():
        tuple_set.add(tuple(string_tuple.replace(" ", "").split("=")))
    return tuple_set

print(tuple_parser(asw2))