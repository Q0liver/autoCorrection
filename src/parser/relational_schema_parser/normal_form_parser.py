import re
import relation_schema_parser as asp
from pprint import pprint

nf1 = """Person = ({ PersonID, Vorname,  Nachname, Straße, Nummer, Ort }, { {PersonID} -> {Vorname, Nachname, Straße, Nummer, Ort}, land -> {kontinent, welt} })"""
nf2 = r"""Mannschaft = ({Name}, {{Name} -> {Name}})"""
nf3 = r"""Spiel = ({Termin, Mannschaft}, {{Termin, Mannschaft} -> {Termin, Mannschaft}})"""

def normal_form_parser(nf):
    relation, definition = nf.split("=")
    attributes, fds = re.findall(r"\{(?:[^{}]|{[^{}]*})*\}", definition)
    attribute_set = asp.set_parser(attributes)
    fds_set = asp.functional_dependencies_parser(fds)
    normal_form = {
        "relation": relation,
        "attributes": attribute_set,
        "fds_set": fds_set
        }
    return normal_form

#pprint(normal_form_parser(nf3))
