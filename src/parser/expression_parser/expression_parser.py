from lark import Lark 
import json
from pprint import pprint
from transformer.er_transformer import AstErTransformer
from transformer.relatinal_algebra_transformer import AstRaTransformer
from transformer.relational_calculus_transformer import AstRcTransformer

er_definition = [ #10
       "Mannschaft = ( {Name, {Spieltermin}}, {Name} )",
       "Person = ({Name, {Telefonnummer}, Adresse(Straße, PLZ, Stadt)}, {Name, Telefonnummer})",
       "dom(Spieltermin) = 2^Date",
       "Person = ({PersonID, Name(Vorname, Nachname), Adresse(Strasse, Nummer, Ort)}, {PersonID})",
       "dom(Adresse) = char(20) x int x char(20)",
       "verschreibt = ((Ärzt*in, Medikament, Patient*in), (Datum))",
       "grad(verschreibt) = 3",
       "comp(verschreibt, Ärzt*in)     = (0, n)",
       "comp(verschreibt, Medikament)  = (0, n)",
       "comp(verschreibt, Patient*in)  = (0, n)"
      ]

relationale_algebra = [ #17
    "PROJECT A, B, C (SELECT ((A = 1 AND (B = 2 OR C = 3)) OR (NOT D = 4 AND E = 5)) (RelationName))",
    'SELECT (datum="01.07.2023" OR schicht="spät" AND mi = mo) AND arsch="clown" AND oi = oi(Einsatzplan)',
    'PROJECT fahrer (SELECT schicht="spät" (SELECT datum="01.07.2023" (Einsatzplan)))',
    'PROJECT fahrer, id, station (SELECT Bus.sitze > 31 (Bus JOIN id=bus (Einsatzplan JOIN Halt)))',
    'PROJECT Einsatzplan.bus, Halt.station (Einsatzplan JOIN Halt)',
    'RENAME id->bus (PROJECT id (SELECT marke="MAN" (Bus)))',
    'PROJECT bus, station (Einsatzplan JOIN Halt) DIVIDE RENAME id->bus (PROJECT id (SELECT marke="MAN" (Bus)))',
    'PROJECT nr, start (SELECT ende="Hauptbahnhof" (Linie))',
    'PROJECT linie, minuten (Halt JOIN station=name SELECT str="Taunusstraße" AND nr=17 (Station))',
    'PROJECT linie, minuten (Halt JOIN (station=name AND str="Taunusstraße" AND nr=17) Station)',
    'PROJECT fahrer, datum, schicht, start, ende (Einsatzplan JOIN linie=nr Linie)',
    "RENAME kollege datum schk stk endk <- fahrer datum schicht start ende (r)",
    'SELECT datum=datk AND schicht=schk AND (start=stk OR ende=endk) (r × rk)',
    'SELECT datum=datk AND schicht=schk AND start=stk (r × rk) UNION SELECT datum=datk AND schicht=schk AND ende=endk (r × rk)',
    '(PROJECT nr (Linie)) × (PROJECT nrk (RENAME nr->nrk (Linie)))',
    'SELECT start != stk AND ende != endk ((PROJECT nr, start, ende (Linie)) × (PROJECT nrk, stk, endk (RENAME nr start ende -> nrk stk endk (Linie))))',
    's1 DIFFERENCE PROJECT nr, nrk (s2)',
    'PROJECT fahrer, kollege (SELECT datum=datk AND schicht=schk ((RENAME linie->nr (E) × PROJECT x (RENAME a->b (E))) JOIN s))'
    ]

drc = ["""MegaTest = {
  (a1, b2, c3) |
    ALL x, y (
      NOT (
        f1(x, y) AND 
        (g2(x) < h3(y) OR "Admin(1)" != u9)
      )
      AND
      EXIST z1, z2 (
        r(a1, b2) OR 
        s(x, y, z1) AND 
        t("abc.def", 'xyz') = v(1)
      )
    )
}
""",
        "Q = { (x, y, z) | EXIST v, w, s (Halt(v, x, w) AND Station(s, y, z) AND v = 1) }",
       "Q = { (x, y) | EXIST a, b, c, d, e (Einsatzplan(x, y, a, b, c) AND Bus(b, d, e) OR d = 'MAN') }",
       "Q = { (x) | EXIST y (Fahrer(x, y) OR NOT(EXISTa, b, c, d, e, f (Einsatzplan(a, x, b, c, d) AND Halt(b, e, f) OR e = 'Uni'))) }"
       ]

#parser = Lark.open("src/parser/expression_parser/lark_grammar/er_definition.lark")
#parser = Lark.open("src/parser/expression_parser/lark_grammar/relational_algebra.lark")
parser = Lark.open("src/parser/expression_parser/lark_grammar/relational_calculus.lark")

for i in range(1):
    #pTree = parser.parse(er_definition[i])
    #pTree = parser.parse(relationale_algebra[i])
    pTree = parser.parse(drc[0])
    #print(pTree.pretty())
    #print(json.dumps(AstRaTransformer().transform(pTree), indent=4))
    #print(AstErTransformer().transform(pTree))
    pprint(AstRcTransformer().transform(pTree))
    #print(pTree.pretty())
