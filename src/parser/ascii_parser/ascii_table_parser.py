from pprint import pprint

table = """+----------+----------------+----------+-----------+
| Vorwahl  | Telefonnummer  | Vorname  | Nachname  |
+----------+----------------+----------+-----------+
| 0511     | 1548592        | Anna     | Eimer     |
| 069      | 5777120        | B.       | Schaufel  |
| 069      | 5777120        | C.       | Besen     |
| +49      | 15198524711    | D.       |    Hammer |
+----------+----------------+----------+-----------+"""

sched = """+------------+------+------+------+------+------+--------+--------+--------+
| Eingabe    | W0A  | W0B  | R1A  | R2B  | W1B  | W2B    | R∞A    | R∞B    |
+------------+------+------+------+------+------+--------+--------+--------+
| Zeit       | 0    | 1    | 2    | 3    | 4    | ∞      |        |        |
+------------+------+------+------+------+------+--------+--------+--------+
| R(A)       | 0    |      | 1    |      |      |        | ∞      |        |
+------------+------+------+------+------+------+--------+--------+--------+
| W(A)       | 0    |      |      |      | ABORT|        | ∞      |        |
+------------+------+------+------+------+------+--------+--------+--------+
| R(B)       |      | 0    |      | 2    |      |        |        | ∞      |
+------------+------+------+------+------+------+--------+--------+--------+
| W(B)       |      | 0    |      |      |      | 2      |        | ∞      |
+------------+------+------+------+------+------+--------+--------+--------+
"""


def ascii_table_parser(table):
    table = [line for line in table.splitlines() if "+" not in line ]
    
    header = table[0].replace(" ", "").strip("|").split("|")
    content = table [1:]
    parsed_table = []
    
    for row in content:
        filled_row = []
        row = row.strip("|").split("|")
        for cell in row:
            if cell.strip() != "":
                filled_row.append(cell.strip())
            else:
                cell = "-"
                filled_row.append(cell)
        parsed_table.append(dict(zip(header, filled_row)))
    return parsed_table

# def ascii_table_parser(table):
#     table = table.replace("+", "").replace("-", "").replace("\n\n", "\n")
#     table = table.lstrip("\n").rstrip("\n")
#     table = table.split("\n")
    
#     header = table[0].replace(" ", "").strip("|").split("|")
#     content = table [1:]
#     parsed_table = []

#     for row in content:
#         parsed_table.append(dict(zip(header, row.replace(" ", "").strip("|").split("|"))))
    
#     print(table)
#     return parsed_table

pprint(ascii_table_parser(table))
