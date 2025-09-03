from lark import Lark 
from transformer.relatinal_algebra_transformer import AstRaTransformer

relationale_algebra = [ #17
    r"""PROJECT fahrer, bus, station ((SELECT datum="01.07.2023" AND schicht="spät" ((Einsatzplan JOIN bus=id (RENAME id->bus (Bus))) JOIN station=name (Halt))) UNION (PROJECT fahrer, bus, station (((Einsatzplan JOIN linie=nr (Linie)) CROSS (PROJECT nrk (RENAME nr->nrk (Linie)))) DIFFERENCE (PROJECT fahrer, bus, station (Einsatzplan JOIN Halt) DIVIDE RENAME id->bus (PROJECT id (SELECT marke="MAN" (Bus)))))))""",
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
    'SELECT datum=datk AND schicht=schk AND (start=stk OR ende=endk) (r CROSS rk)',
    'SELECT datum=datk AND schicht=schk AND start=stk (r CROSS rk) UNION SELECT datum=datk AND schicht=schk AND ende=endk (r CROSS rk)',
    '(PROJECT nr (Linie)) CROSS (PROJECT nrk (RENAME nr->nrk (Linie)))',
    'SELECT start != stk AND ende != endk ((PROJECT nr, start, ende (Linie)) CROSS (PROJECT nrk, stk, endk (RENAME nr start ende -> nrk stk endk (Linie))))',
    's1 DIFFERENCE PROJECT nr, nrk (s2)',
    'PROJECT fahrer, kollege (SELECT datum=datk AND schicht=schk ((RENAME linie->nr (E) CROSS PROJECT CROSS (RENAME a->b (E))) JOIN s))'
    ]

def relationale_algebra_parser(str_notation):
  """This function performs a string-to-data structure transformation of formal relational algebra expressions

  Args:
      str_notation str: formal notation

  Returns:
      dict: data structue representation of notation
  """
  parser = Lark.open("src/parser/grammar_parser/lark_grammar/relational_algebra.lark")
  pTree = parser.parse(str_notation)
  return AstRaTransformer().transform(pTree)

# #for i in range(len(relationale_algebra)):
#     print(i)
#     print(relationale_algebra_parser(relationale_algebra[i]))
#     print 
#     print("\n")
