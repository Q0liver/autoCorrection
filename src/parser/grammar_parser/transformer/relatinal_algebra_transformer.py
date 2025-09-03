from lark import Transformer
from . import sort_rules

class AstRaTransformer(Transformer):
    # shared
    def start(self, children):
        return children[0]
    
    def operation(self, children):
        return children[0]
    
    def priority_operation(self, children):
        return {
            "associative": children[0]
            }

    def suboperation(self, children):
        return children[0]
    
    def attributes(self, children):
        return sorted(children, key=sort_rules.order)
    
    def attribute(self, children):
        return children[0]
    
    def relation(self, children):
        return children[0]
    
    #def value(self, children):
        return children[0]
    
    def NAME(self, token):
        return str(token)
    
    # project methods
    def projection(self, children):
        return {
            "project": children[0], 
            "relation": children[1]
            }
    
    # select methods
    def selection(self, children):
        return {
            "select": children[0], 
            "relation": children[1]
            }
    
    def condition(self, children):
        return children[0]

    def priority_condition(self, children):
        return {
            "type": "priority_condition",
            "operator": "()", 
            "operands": children
            }

    def logical_condition(self, children):
        return children[0]
    
    def not_condition(self, children):
        return {
            "type": "logical_condition",
            "operator": "NOT",
            "operands": sorted([children[0]], key=sort_rules.order)}
    
    def flattening(self, condition):
        flatten = []
        operator = condition["operator"]

        for operand in condition["operands"]:
            if isinstance(operand, dict):
                operand_type = operand["type"]
                if operand_type in ("logical_condition", "priority_condition"):
                    operand = self.flattening(operand)
                    if operand["type"] == "logical_condition" and operand["operator"] == operator:
                        flatten.extend(operand["operands"])
                    else:
                        flatten.append(operand)
                elif operand_type == "compare_condition":
                    flatten.append(operand)

            else:
                flatten.append(operand)
        return {
            "type": "logical_condition",
            "operator": operator,
            "operands": sorted(flatten, key=sort_rules.order) 
        }

    def and_condition(self, children):
        return self.flattening({
            "type": "logical_condition",
            "operator": "AND", 
            "operands": children
            })

    def or_condition(self, children):
        return self.flattening({
            "type": "logical_condition",
            "operator": "OR", 
            "operands": children
            })
    
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
    
    # rename methods

    def renaming(self, children):
        if  children[0][1] == "->":
            children[0][1] = "<-"
            children[0] = children[0][::-1]
        return {
            "rename": children[0], 
            "relation": children[1]
            }
    
    def rename_direction(self, children):
        return children[0]
    
    def new_old(self, children):
        return "<-"
    
    def old_new(self, children):
        return "->"
    
    def rename_attributes(self, children):
        return children
    
    def attribute_names(self, children):
        return sorted(children, key=sort_rules.order)

    # set operation methods
    def set_operation(self, children):
        if children[1] in ("UNION", "INTERSECTION", "JOIN", "CROSS"):
            operands = sorted([children[0], children[2]], key=sort_rules.order)
        else: operands = [children[0], children[2]]
        return {
            "type": "set_operation",
            "operator": children[1], 
            "operands": operands
            }

    def set_operator(self, children):
        return children[0] 
    
    def union(self, children):
        return "UNION"
    
    def intersection(self, children):
        return "INTERSECTION"    
    
    def difference(self, children):
        return "DIFFERENCE"
    
    def crossproduct(self, children):
        return "CROSS"
    
    def divide(self, children):
        return "DIVIDE"
    
    def join(self, children):
        if len(children) != 0:
            return "JOIN", children[0]
        else:
            return "JOIN"
    
    def theta_condition(self, children):
        return children[0]