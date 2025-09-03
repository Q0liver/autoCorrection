import re

asw = """Teilabhängig = {N, H, S, Nr, O, P}"""

asw2 = """Min = 0 
Max = n"""

def tuple_parser(string_tuple):
    tuple_set = set()
    for string_tuple in string_tuple.splitlines():
        tuple_set.add(tuple(string_tuple.replace(" ", "").split("=")))
    return tuple_set

def set_parser(string):
    """This function extracts a set "{a,b,c,...}" structure in a string.

    Args:
        string:

    Returns:
        set: string depiction of set turns into actuall set
    """
    sset = re.search(r"\{([^}]*)\}" ,string)
    if sset:
        inside = sset.group(1)
    return set(inside.split(","))

#print(set_parser(asw))