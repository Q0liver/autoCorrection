def order(structure):
    if isinstance(structure, tuple):
        return structure[0]
    elif isinstance(structure, list):
        return structure[0]  
    elif isinstance(structure, dict):
        if structure.get("type") != "compare_condition":
            return structure["type"]
        else:
            return structure["operands"][0]
    else:
        return structure 