from lark import Lark 
from parser.grammar_parser.transformer.er_transformer import AstErTransformer

test = """person = ({id, first_name, last_name}, {id})   
pilot = ({license_valid_till, comment}, {})
customer = ({credit}, {})
customer_vip = ({comment}, {})
   ISA(pilot, person)
   ISA(customer, person)
   ISA(Customer_vip, customer)
address = ({id, town, zip_code, street}, {id})
   at = ((pilot, address), {})
      comp(at, pilot) = (1,1)
      comp(at, address) = (0,n)
   at = ((airport, address), {})
      comp(at, airport) = (1,1)
      comp(at, address) = (0,n)
airport = ({icao_code, airport_name}, {icao_code})
   from = ((flight, airport), {})
      comp(from, flight) = (1,1)
      comp(from, airport) = (0,n)
   to = ((flight, airport), {})
      comp(to, flight) = (1,1)
      comp(to, airport) = (0,n)
flight = ({flight_no, departure, duration}, {flight_no, departure})
   reserves = ((customer, flight), {no_seats, comment})
      comp(reserves, customer) = (0,n)
      comp(reserves, flight) = (0,n)
plane = ({id, type, name, no_seats}, {id})
   executes = ((plane, flight), {})
      comp(executes, plane) = (0,n)
      comp(executes, flight) = (1,1)
"""
test2 = """person = ({id, first_name, last_name}, {id})   
pilot = ({license_valid_till, comment}, {})
customer = ({credit}, {})
customer_vip = ({comment}, {})
   ISA(pilot, person)
   ISA(customer, person)
   ISA(Customer_vip, customer)
address = ({id, town, zip_code, street}, {id})
   at = ((pilot, address), {})
      comp(at, pilot) = (1,1)
      comp(at, address) = (0,n)
   at = ((airport, address), {})
      comp(at, airport) = (1,1)
      comp(at, address) = (0,n)
airport = ({icao_code, airport_name}, {icao_code})
   from = ((flight, airport), {})
      comp(from, flight) = (1,1)
      comp(from, airport) = (0,n)
   to = ((flight, airport), {})
      comp(to, flight) = (1,1)
      comp(to, airport) = (0,n)
flight = ({flight_no, departure, duration}, {flight_no, departure})
   reserves = ((customer, flight), {no_seats, comment})
      comp(reserves, customer) = (0,n)
      comp(reserves, flight) = (0,n)
plane = ({id, type, name, no_seats}, {id})
   executes = ((plane, flight), {})
      comp(executes, plane) = (0,n)
      comp(executes, flight) = (1,1)
"""

testset = test.splitlines()
testset2 = test2.splitlines()

parser = Lark.open("src/parser/grammar_parser/lark_grammar/er_definition.lark")

referenceset = [AstErTransformer().transform(parser.parse(lines)) for lines in testset] 

for line in testset2:
    try:
        ptree = parser.parse(line)
        ptree = AstErTransformer().transform(ptree)
        if ptree in referenceset:
            continue
        else:
            print("nicht gefudnen: ")
            print(line)
    except:
        print("nicht gefudnen: ")
        print(line)
