import re
import parser.relational_schema_parser.fd_bases_and_key_parser as asp
from pprint import pprint

schemas = [
    """Mannschaft = ({Name}, {{Name} -> {Name}})""",
    "Spiel = ({Termin, Mannschaft}, {{Termin, Mannschaft} -> {Termin, Mannschaft}})",
    "Person = ({PersonID, Vorname, Nachname, Straße, Nummer, Ort}, {{PersonID} -> {Vorname, Nachname, Straße, Nummer, Ort}})",
    "Item = ({I, N, H}, {I -> N, N -> H})",
    "Lieferant = ({L, S, Nr, O, P}, {L -> S, L -> Nr, L -> O, L -> P})",
    "Lieferung = ({I, L, M}, {IL -> M})",
    "Produzenten = ({N, H}, {N -> H})",
    "Item = ({I, N}, {I -> N})",
    "Lieferant = ({L, S, Nr, O, P}, {L -> S, L -> Nr, L -> O, L -> P})",
    "Lieferung = ({I, L, M}, {IL -> M})",
    "R1 = ({I, N}, {I -> N})",
    "R2 = ({L, S, Nr, O, P}, {L -> S, L -> Nr, L -> O, L -> P})",
    "R3 = ({N, H}, {N -> H})",
    "R4 = ({I, L, M}, {IL -> M})",
    "A = ({a, x},{a -> x})",
    "B = ({b, y},{b -> y})",
    "C = ({a, b, p, q},{ab -> pq})",
    "R1 = ({a, x},{a -> x})",
    "R2 = ({b, y},{b -> y})",
    "R3 = ({a, b, p, q},{ab -> p, ab -> q})",
    "F = ({u, h},{uh -> uh})",
    "D = ({d, u, h},{uh -> d})",
    "E = ({e, u, h},{uh -> e})",
    "R1 = ({u, h, d, e},{uh -> d, uh -> e})"
]



def relational_schema_parser(nf):
    """This function performs string-to-data structure transformations of realtional schema

    Args:
        str: formal notation of relational schema

    Returns:
        dict: data structure representation of th erelational schema
    """
    relation, definition = nf.split("=")
    attributes, fds = re.findall(r"\{(?:[^{}]|{[^{}]*})*\}", definition)
    attribute_set = asp.set_parser(attributes)
    fds_set = asp.functional_dependencies_parser(definition)
    normal_form = {
        "relation": relation,
        "attributes": attribute_set,
        "fds_set": fds_set
        }
    return normal_form 

# for i in range(len(schemas)): # for testing purposes
#     print(i)
#     print(relational_schema_parser(schemas[i]))
#     print("\n")