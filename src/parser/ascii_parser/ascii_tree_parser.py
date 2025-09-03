trees = [
    """PROJECT station, str, nr
└── SELECT linie=1
    └── CROSS
        ├── Halt
        └── Station""",

    """PROJECT datum,fahrer
└── JOIN
    ├── Einsatzplan
    └── RENAME id->bus
        └── SELECT marke="Man"
            └── Bus""",

    """\\ 
├── RENAME name->fahrer
│   └── PROJECT fahrer
│       └── Fahrer 
└── PROJECT fahrer
    └── JOIN
        ├── Einsatzplan
        └── PROJECT linie
            └── SELECT station="Uni"
                └── Halt""",

    """[|37||73|]
├── [|22|||]
│   ├── [22,013|]
│   └── [29,023|37,033]
├── [|45||61|]
│   ├── [41,043|45,053]
│   ├── [53,063|61,073]
│   └── [68,083|73,093]
└── [|81||94|]
    ├── [81,103|]
    ├── [89,113|94,123]
    └── [98,133|]""",

    """[|60|||]
├── [|37|||]
│   ├── [|22|||]
│   │   ├── [22,013|]
│   │   └── [29,023|37,033]
│   └── [|45|||]
│       ├── [41,043|45,053]
│       └── [53,063|60,143]
└── [|73|||] 
    ├── [|61|||]
    │   ├── [61,073|]
    │   └── [68,083|73,093]
    └── [|81||94|]
        ├── [81,103|]
        ├── [89,113|94,123]
        └── [98,133|]"""
]

def ascii_tree_parser(tree):
    """This function parses an Ascii tree into  python datastructure

    Args:
        tree (str): Ascii tree

    Returns:
        Tree structure: Parent = Dict(), Children = [], Leaf = "str"
    """
    tree = tree.strip("\n").split("\n")
    
    root = tree[0]
    content = tree[1:]
    parsed_tree = {
        "root": root,
        "children": []
        }
    
    depth = -1
    stack =[(parsed_tree, depth)]

    for level in content:
        level = level.replace("│", "").replace("├", "").replace("└", "").replace("─", "")
        current_depth = len(level) - len(level.lstrip(" "))

        if current_depth > depth:
            depth = current_depth
            node = {
                "node": level.replace(" ", ""), 
                "children": []
                }
            stack[-1][0]["children"].append(node)
            stack.append((node, depth)) 
        elif current_depth == depth:
            del stack[-1]
            node = {
               "node": level.replace(" ", ""), 
                "children": []
                }
            stack[-1][0]["children"].append(node)
            stack.append((node, depth))
        else:
            depth = current_depth
            while stack[-1][1] >= current_depth:
                del stack[-1]
            node = {
               "node": level.replace(" ", ""), 
                "children": []
                }
            try:
                stack[-1][0]["children"].append(node)
                stack.append((node, depth))
            except:
                pass
    return parsed_tree
            
# For testing purposes
for i in range(len(trees)):
    print(i)
    print(ascii_tree_parser(trees[i]))
    print("\n")
  


