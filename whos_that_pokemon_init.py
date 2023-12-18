from owlready2 import *

# Criar uma ontologia vazia
onto_poke = get_ontology("http://www.example.org/pokemon_ontology.owl")

# Definir classes
class Pokemon(Thing):
    namespace = onto_poke

class Type(Thing):
    namespace = onto_poke

class Color(Thing):
    namespace = onto_poke

class Category(Thing):
    namespace = onto_poke

class PhysicalTrait(Thing):
    namespace = onto_poke

class DiverseTrait(Thing):
    namespace = onto_poke

# Definição de propriedades
class hasType(ObjectProperty):
    namespace = onto_poke
    domain = [Pokemon]
    range = [Type]

class hasColor(ObjectProperty):
    namespace = onto_poke
    domain = [Pokemon]
    range = [Color]

class hasCategory(ObjectProperty):
    namespace = onto_poke
    domain = [Pokemon]
    range = [Category]

class hasPhysicalTrait(ObjectProperty):
    namespace = onto_poke
    domain = [Pokemon]
    range = [PhysicalTrait]

class hasDiverseTraits(ObjectProperty):
    namespace = onto_poke
    domain = [Pokemon]
    range = [DiverseTrait]

# Salvar a ontologia em um arquivo RDF
onto_poke.save("pokemon_ontology.owl", format="rdfxml")