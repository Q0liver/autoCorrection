from parser.ascii_parser.ascii_table_parser import ascii_table_parser
from parser.ascii_parser.ascii_tree_parser import ascii_tree_parser

from deepdiff import DeepDiff

sub = """
Aufgabe 3
a) PROJECTE (s UNION s) CROSS (r ∩ (r JOIN r)) und PROJECTE (s) JOIN r
Den linken Ausdruck kann man folgendermaßen vereinfachen:
1. s UNION s = s (keine Duplikate bei Mengen).
2. r JOIN r = r (jedes Tupel passt mindestens zu sich selbst und es gibt keine zusätzlichen Attribute)
3. Aus 2. folgt dann r ∩ r = r (jedes Tupel in r ist ja auch in r…).
PROJECTE (s UNION s) CROSS (r ∩ (r JOIN r)) = PROJECTE (s) CROSS r
Da außerdem die Relationsschema R und S keine gemeinsamen Attribute haben ({A, B,D} ∩ {C, E, F} = ∅), 
sind der natürliche Join und das kartesische Produkt der Relationen r und s gleich. Es folgt:
PROJECTE (s UNION s) CROSS (r ∩ (r JOIN r)) = PROJECTE (s) CROSS r = PROJECTE (s) JOIN r
Offensichtlich ist der erste Ausdruck stark redundant und der zweite Ausdruck ist dahingegen wesentlich kürzer. 
Demnach ist der zweite Ausdruck performanter in der Ausführung. 
(Das Datenbanksystem würde den ersten Ausdruck aber dennoch hoffentlich vor der Berechnung vereinfachen 
und optimieren.)

b) PROJECTr.B(SELECT r.B=99 (r CROSS q)) und SELECT B=99(πB (r))
Das Ergebnis beider Ausdrücke ist eine Tabelle mit dem Attribut B und einer einzigen Zeile mit dem Wert 99 oder 
keinem Ergebnis, wenn es kein entsprechendes Tupel in r gibt. Das sieht man auch, 
wenn man den ersten Ausdruck in den zweiten folgendermaßen umformt:
Weil sowohl Projektion und Selektion nur Attribut r.B betreffen, kann man sie beide miteinander vertauschen:
PROJECTr.B(SELECT r.B=99 (r CROSS q)) = SELECT r.B=99(πr.B(r CROSS q))
Dann sieht man auch, dass das kartesische Produkt R CROSS Q hinfällig ist, wenn man danach auf das Attribut r.B 
projiziert, i.e., πr.B(r CROSS q) = πr.B(r). Daraus würde die Äquivalenz folgen:
PROJECTr.B(SELECT r.B=99 (r CROSS q)) = SELECT r.B=99(πr.B(r CROSS q)) = SELECT r.B=99(πr.B(r))
Da der zweite Ausdruck keinen Join erfordert und außerdem gleich alle unnötigen Attribute eliminiert, würden sowohl 
Laufzeit als auch Speicherplatz bei der Berechnung gespart.
Wäre statt des kartesischen Produkts dort ein natürlicher Join im rechten Ausdruck, dann wären die Ausdrücke nicht 
äquivalent. Gegenbeispiel:
r = {(a, 99, d)} und q = {(1, c)} → PROJECTr.B(SELECT r.B=99 (r JOIN q)) = ∅ und SELECT B=99(πB (r)) = {(99)}.

c) r JOIN (SELECT B=3 q) und (SELECT B=3 r) JOIN q
Die beiden Ausdrücke sind äquivalent, weil es egal ist, ob bei r oder q nach B = 3 selektiert wird. 
Formal kann man das zeigen durch die Umformung
r JOIN (SELECT B=3 q) = SELECT B=3 (r JOIN q) = (SELECT B=3 r) JOIN q
Welcher Ausdruck performanter ist, hängt hier tatsächlich vom Inhalt der Datenbank ab. 
Wenn bspw. die Relation r sehr viele Tupel im Vergleich zu q hat und die Selektion davon viele aussortieren würde, 
wäre der zweite Ausdruck schneller. Im Idealfall gibt es vielleicht einen Index über B und das Datenbanksystem 
kann die Ausdrücke dann als jeweils eine Operation ausführen, also Selektion und Join gleichzeitig 
mit Hilfe des Index.

Aufgabe 4
a) Sei X = Y und Z ⊆ X. Dann gilt πZ (r DIFFERENCE s) = πZ (r) DIFFERENCE πZ (s).
Diese Aussage ist i.A. falsch. Es kann passieren, dass durch die Projektion auf Z mehr Tupel in πZ (r) durch Tupel 
in πZ (s) eliminiert werden im Vergleich zu r DIFFERENCE s, wobei die anschließende Projektion keine Tupel als 
Duplikate eliminiert. Dann wäre |πZ (r) DIFFERENCE πZ (s)| < |πZ (r DIFFERENCE s)|
Gegenbeispiel: X = Y = {A, B}, Z = {A}, r = {(1,2)}, s = {(1,3)}
Dann wäre r DIFFERENCE s = {(1,2)} = r und πZ (r DIFFERENCE s) = {(1)}, wohingegen πZ (r) DIFFERENCE πZ (s) = {(1)} DIFFERENCE {(1)} = ∅.

b) Sei X ∩ Y = ∅. Dann gilt (r JOIN s) DIVIDE s = r.
Da X ∩ Y = ∅ gilt, ist r JOIN s das kartesische Produkt.
(r JOIN s) DIVIDE s = (r CROSS s) DIVIDE s
Durch Anwendung der Definition der relationalen Division unter Beachtung von X DIVIDE Y = X (weil X ∩ Y = ∅) folgt dann
(r CROSS s) DIVIDE s = πX(r CROSS s) DIFFERENCE πX((πX(r CROSS s) CROSS s) DIFFERENCE (r CROSS s))
Weiterhin lässt sich πX(r CROSS s) zu r vereinfachen, da ohnehin alle Attribute von s wegprojiziert werden:
πX(r CROSS s) DIFFERENCE πX((πX(r CROSS s) CROSS s) DIFFERENCE (r CROSS s)) = r DIFFERENCE πX((r CROSS s) DIFFERENCE (r CROSS s))
Ersetzt man nun noch (r CROSS s) DIFFERENCE (r CROSS s) durch ∅, folgt dass
r DIFFERENCE πX((r CROSS s) DIFFERENCE (r CROSS s)) = r DIFFERENCE πX(∅) = r

Aufgabe 5
a) 
Min=0 
Max=m

b) 
Min=0 
Max=n

c) 
Min=max{m,n} 
Max=m+n

d) 
Min=0 
Max=min{m,n}

e) 
Min=0 
Max=m

f) 
Min=0 
Max=mn (falls X∩Y≠∅) 
Min=mn 
Max=mn (falls X∩Y=∅)

g) 
Min=0 
Max=mn

h) 
Min=0 
Max=floor(m/n)
"""

ref = """PROJECT station, str, nr
└── SELECT linie=1
    └── CROSS
        ├── Halt
        └── 𝑆𝑡𝑎𝑡𝑖𝑜𝑛
"""

#dif = DeepDiff(ascii_table_parser(sub), ascii_table_parser(ref), ignore_order=True)
dif = DeepDiff(ascii_tree_parser(sub), ascii_tree_parser(ref), ignore_order=True)

print(dif)
