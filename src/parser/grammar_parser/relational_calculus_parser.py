from lark import Lark 
from transformer.relational_calculus_transformer import AstRcTransformer

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

def relationale_calculus_parser(str_notation):
  """This function performs a string-to-data structure transformation of formal relational calculus expressions

  Args:
      str_notation str: formal notation

  Returns:
      dict: data structue representation of notation
  """
  parser = Lark.open("src/parser/grammar_parser/lark_grammar/relational_calculus.lark")
  pTree = parser.parse(str_notation)
  return AstRcTransformer().transform(pTree)


# # for i in range(len(drc)):
#     print(i)
#     print(relationale_calculus_parser(drc[i]))
#     print("\n")