from lark import Transformer
from . import sort_rules

class AstErTransformer(Transformer):
    # shared
    def start(self, children):
        return children[0]
    
    def attributes(self, children):
        return sorted(children, key=sort_rules.order)
    
    def attribute(self, children):
        return children[0]    

    def monovalent(self, children):
        return children[0]
    
    def polyvalent(self, children):
        return "{" + children[0] + "}"
    
    def composed(self, children):
        attribute = children[0]
        composition = children[1]
        return (attribute, composition)

    def NAME(self, token):
        return str(token)    

    # entity  methods
    def entity_declaration(self, children):
        definition = "entity_declaration"
        name = children[0]
        definition_value = "entity_schema"
        value = children[1]
        return {definition: name, definition_value: value}
    
    def entity_schema(self, children):
        attributes, keys = children
        return {"attributes": attributes,
                "keys": keys}
    
    def format_x(self, children):
        return children[0]
    
    def primary_key_k(self, children):
        return sorted(children, key=sort_rules.order)
    
    def key(self, children):
        return children[0]
    
    # genralization

    def generalization(self, children):
        return {"generalization": children[0]}
    # domain methods

    def domain(self, children):
        definition = "domain"
        name = children[0]
        definition_value = "value_range"
        value = children[1]
        return {definition: name, definition_value: value}
    
    def value_range(self, children):
        return children[0]

    def range(self, children):
        return children[0]
    
    def power_set(self, children):
        return ("power_set", (children[0] ,children[1]))

    def cartesian_product(self, children):
        return ("cartesian_product", sorted(children, key=sort_rules.order))

    def simple_set(self, children):
        return children [0]

    # relation methods

    def relationship(self, children):
        definition = "relationship"
        name = children[0]
        definition_value = "relation"
        value = children[1]
        return {definition: name, definition_value: value}
    
    def relation(self, children):
        entities, attributes = children
        return {"entities": entities, "attributes": attributes}

    def relation_entities(self, children):
        return sorted(children, key=sort_rules.order)
    

    def entity(self, children):
        return children[0]
    
    # order methods

    def order(self, children):
        definition = "order"
        name = children[0]
        definition_value = "order_number"
        value = children[1]
        return {definition: name, definition_value: value}
    
    def order_number(self, children):
        return children[0]
    
    # cardinality methods

    def complexity(self, children):
        definition = "complexity"
        name = [children[0], children[1]]
        definition_value = "cardinality"
        value = children[2]
        return {definition: name, definition_value: value}
    
    def cardinality(self, children):
        return (children[0], children[1])