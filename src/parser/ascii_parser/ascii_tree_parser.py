from pprint import pprint

test_tree = """
root
├── A
│   ├── A1
│   │   ├── A1a
│   │   └── A1b
│   └── A2
│       ├── A2a
│       └── A2b
├── B
│   ├── B1
│   │   └── B1a
│   └── B2
└── C
    ├── C1
    ├── C2
    │   └── C2a
    └── C3
        ├── C3a
        └── C3b
"""


def ascii_tree_parser(tree):
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
            
pprint(ascii_tree_parser(test_tree))
#print(repr(tree.strip("\n").split("\n")))    


