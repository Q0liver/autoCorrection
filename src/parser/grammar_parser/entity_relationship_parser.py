from lark import Lark 
from transformer.er_transformer import AstErTransformer

definitions = [
    "Anbieter = ({Name,Adresse},{Name, Adresse})",
    "Anbieter = ({}, {})",
    "Gericht = ({Name, Kategorie, Preis}, {Name, Preis})",
    "verkauft = ((Anbieter, Gericht), {})",
    "comp(verkauft, Anbieter) = (1,n)",
    "comp(verkauft, Gericht) = (1,1)",
    "Gericht = ({Name, Kategorie}, {Name})",
    "verkauft = ((Anbieter, Gericht), {Preis})",
    "comp(verkauft, Gericht) = (0,n)",
    "Fahrer = ({Mobil, Name}, {Mobil})",
    "Fahrzeug = ({Beschreibung, Kapazität, ID}, {ID})",
    "benutzt = ((Fahrer, Fahrzeug), {})",
    "comp(benutzt, Fahrer) = (1,1)",
    "comp(benutzt, Fahrzeug) = (1,1)",
    "Gericht = ({}, {})",
    "Bestellung = ({Datum, Uhrzeit, Adresse, Klingelname},{Datum, Uhrzeit, Adresse, Klingelname})",
    "Fahrer = ({}, {})",
    "bestellt = ((Bestellung, Gericht), {})",
    "liefert = ((Fahrer, Bestellung), {})",
    "comp(liefert, Fahrer) = (1,n)",
    "comp(liefert, Bestellung) = (1,1)",
    "comp(bestellt, Greicht) = (0,n)",
    "comp(bestellt, Bestellung) = (1,n)",
    "Mannschaft = ({Name, Spieltermin},{Name})",
    "dom(Spieltermin) = 2^Date",
    "Person = ({PersonID, Name(Vorname, Nachname), Adresse(Strasse, Nummer, Ort)},{PersonID})",
    "dom(Adresse) = char(20) x int x char(20)",
    "verschreibt = ((Arzt*in, Medikament, Patient*in), (Datum))",
    "grad(verschreibt) = 3",
    "comp(verschreibt, Arzt*in) = (0,n)",
    "comp(verschreibt, Medikament) = (0,n)",
    "comp(verschreibt, Patient*in) = (0,n)",
    "person = ({id, first_name, last_name}, {id})",
    "pilot = ({license_valid_till, comment}, {})",
    "customer = ({credit}, {})",
    "customer_vip = ({comment}, {})",
    "ISA(pilot, person)",
    "ISA(customer, person)",
    "ISA(Customer_vip, customer)",
    "address = ({id, town, zip_code, street}, {id})",
    "at = ((pilot, address), {})",
    "comp(at, pilot) = (1,1)",
    "comp(at, address) = (0,n)",
    "at = ((airport, address), {})",
    "comp(at, airport) = (1,1)",
    "airport = ({icao_code, airport_name}, {icao_code})",
    "from = ((flight, airport), {})",
    "comp(from, flight) = (1,1)",
    "comp(from, airport) = (0,n)",
    "to = ((flight, airport), {})",
    "comp(to, flight) = (1,1)",
    "comp(to, airport) = (0,n)",
    "flight = ({flight_no, departure, duration}, {flight_no, departure})",
    "reserves = ((customer, flight), {no_seats, comment})",
    "comp(reserves, customer) = (0,n)",
    "comp(reserves, flight) = (0,n)",
    "plane = ({id, type, name, no_seats}, {id})",
    "executes = ((plane, flight), {})",
    "comp(executes, plane) = (0,n)",
    "comp(executes, flight) = (1,1)",
    "ISA(Pilot, Person)",
    "Person = ({PersonID, Name(Vorname, Nachname), Adresse(Strasse, Nummer, Ort), {Telefonnummer}}, {PersonID})",
    "dom(Adresse) = char(50) x int x char(50)",
    "Mannschaft = ({TeamName, {Spieltermin}, Trainer(PersonID)}, {TeamName})",
    "Spiel = ({SpielID, Datum, Ort, Mannschaft1(TeamName), Mannschaft2(TeamName)}, {SpielID})",
    "verschreibt = ((Ärzt*in, Medikament, Patient*in), {Datum, Dosierung})",
    "comp(verschreibt, Ärzt*in) = (1, n)",
    "comp(verschreibt, Medikament) = (0, n)",
    "comp(verschreibt, Patient*in) = (1, n)"
]

def entity_relation_parser(str_notation):
  """This function performs a string-to-data structure transformation of formal entity relationship definitions

  Args:
      str_notation str: formal definitions

  Returns:
      dict: data structue representation of definitions
  """
  parser = Lark.open("src/parser/grammar_parser/lark_grammar/er_definition.lark")
  pTree = parser.parse(str_notation)
  return AstErTransformer().transform(pTree)

# # For testing purposes
# for i in range(len(definitions)):
#     print(i)
#     print(entity_relation_parser(definitions[i]))
#     print("\n")