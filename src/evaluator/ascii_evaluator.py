from parser.ascii_parser.ascii_table_parser import ascii_table_parser
from parser.ascii_parser.ascii_tree_parser import ascii_tree_parser
from deepdiff import DeepDiff

# sub = """PROJECT station, str, nr
# └── SELECT linie=1
#     └── DIFFERENCE
#         ├── Halt
#         └── Halt
# """
# ref = """PROJECT station, str, nr
# └── SELECT linie=1
#     └── DIFFERENCE
#         ├── Station
#         └── Halt
# """

ref = """
+----------+----------------+----------+-----------+
| Vorwahl  | Telefonnummer  | Vorname  | Nachname  |
+----------+----------------+----------+-----------+
| 0511     | 1548592        | Anna     | Eimer     |
| 069      | 5777120        | B.       | Schaufel  |
| 069      | 5777120        | C.       | Besen     |
| +49      | 15198524711    | D.       | Hammer    |
+----------+----------------+----------+-----------+
"""
sub = """
+----------+----------------+----------+---------------+
| Vorname  | Nachname       | Vorwahl  | Telefonnummer |
+----------+----------------+----------+---------------+
| C.       | Besen          | 069      | 5777120       |
| D.       | Hamdmer         | +49      | 15198524711   |
| Anna     | Eimer          | 0511     | 1548592       |
| B.       | Schaufel       | 069      | 5777120       |
+----------+----------------+----------+---------------+
"""

def ascii_representation_evaluator(ref, sub, repesentation_type):
    """This function checks ASCII trees or tables for equality.

    Args:
        ref (str): reference string
        sub (str): submission string
        repesentation_type (str): information about ASCII representation: "tree" or "table"

    Returns:
        Booloean: When False a notation is added pin pointing the error source
    """
    if repesentation_type == "tree":
        func = ascii_tree_parser
    elif repesentation_type == "table":
        func = ascii_table_parser
    diff = DeepDiff(func(ref), func(sub))
    if func(ref) == func(sub) or not diff:
        return True
    else:
        return False, diff

# for test purposes 
print(ascii_representation_evaluator(ref, sub, "table"))
