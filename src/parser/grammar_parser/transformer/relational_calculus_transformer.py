from lark import Transformer
from . import sort_rules

class AstRcTransformer(Transformer):

    # shared 
    
    def start(self, children):
        return children[0]
    
    def query(self, children):
        return {
            "query_name": children[0],
            "query_definition": children[1:] 
        }
    
    def conditioned_variables(self, children):
        return children[0]

    def priority_condition(self, children):
        return {
            "type": "priority_condition",
            "operator": "()", 
            "operands": children
            }
    
    def quantifiers(self, children):
        return children
    
    def all(self, children):
        return {
            "type": "quantifier",
            "operator": "ALL", 
            "operands": [sorted(children[0], key=sort_rules.order), children[1]]
            }
    
    def exist(self, children):
        return {
            "type": "quantifier",
            "operator": "Exist", 
            "operands": [sorted(children[0], key=sort_rules.order), children[1]]
            }

    def atomic(self, children):
        return {
            "type": "atomic",
            "relation": children[0], 
            "attributes": sorted(children[1], key=sort_rules.order)
            }
    
    def logical_condition(self, children):
        return children[0]
    
    def not_condition(self, children):
        return {
            "type": "logical_condition",
            "operator": "NOT",
            "operands": sorted([children[0]], key=sort_rules.order)}
    
    
    def and_condition(self, children):
        return {
            "type": "logical_condition",
            "operator": "AND", 
            "operands": children
            }

    def or_condition(self, children):
        return {
            "type": "logical_condition",
            "operator": "OR", 
            "operands": children
            }

    def compare_condition(self, children):
        return {
            "type": "compare_condition",
            "operator": children[1], 
            "operands": [children[0], children[2]]
            }
    
    def compare_operator(self, children):
        return children[0]
    
    def lt(self, children):
        return "<"
    
    def lte(self, children):
        return "<="
    
    def gt(self, children):
        return ">"
    
    def gte(self, children):
        return ">="
    
    def eq(self, children):
        return "="
    
    def neq(self, children):
        return "!="
    
    def free_variables(self, children):
        return{
            "free_variables": sorted(children, key=sort_rules.order)
        }
    
    def variables(self, children):
        return sorted(children, key=sort_rules.order)

    def NAME(self, token):
        return str(token)