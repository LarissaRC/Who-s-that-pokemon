from owlready2 import *

# Carregar a ontologia
onto = get_ontology("./pokemon_ontology.owl").load()

# Adicionar Tipos
grama = onto.Type("Grama")
fogo = onto.Type("Fogo")
agua = onto.Type("Água")
inseto = onto.Type("Inseto")
normal = onto.Type("Normal")
lutador = onto.Type("Lutador")
voador = onto.Type("Voador")
venenoso = onto.Type("Venenoso")
eletrico = onto.Type("Elétrico")
solo = onto.Type("Solo")
psiquico = onto.Type("Psíquico")
rocha = onto.Type("Rocha")
fantasma = onto.Type("Fantasma")
dragao = onto.Type("Dragão")
aco = onto.Type("Aço")
gelo = onto.Type("Gelo")

# Adicionar cores
verde = onto.Color("Verde")
laranja = onto.Color("Laranja")
azul = onto.Color("Azul")
roxo = onto.Color("Roxo")
marrom = onto.Color("Marrom")
amarelo = onto.Color("Amarelo")
rosa = onto.Color("Rosa")
vermelho = onto.Color("Vermelho")
marrom_claro = onto.Color("Marrom claro")
lilas = onto.Color("Lilás")
cinza = onto.Color("Cinza")
branco = onto.Color("Branco")

# Adicionar Categorias
normal = onto.Category("Normal")
lendario = onto.Category("Lendário")
mitico = onto.Category("Mítico")

# Adicionar características físicas
pes = onto.PhysicalTrait("Pés")
maos = onto.PhysicalTrait("Mãos")
asas = onto.PhysicalTrait("Asas")
cauda = onto.PhysicalTrait("Cauda")
bico = onto.PhysicalTrait("Bico")
focinho = onto.PhysicalTrait("Focinho")
orelhas = onto.PhysicalTrait("Orelhas")
chifres = onto.PhysicalTrait("Chifres")
boca = onto.PhysicalTrait("Boca")

# Adicionar características diversas
evolucao = onto.DiverseTrait("Evolução")
redondo = onto.DiverseTrait("Redondo")
anda_de_quatro = onto.DiverseTrait("Anda de quatro")
anda_de_dois = onto.DiverseTrait("Anda de dois")
parece_objeto = onto.DiverseTrait("Parece objeto")
cabecas = onto.DiverseTrait("Cabeças")
segura_objeto = onto.DiverseTrait("Segura objeto")

#Bulbasaur
pokemon1 = onto.Pokemon("Bulbasaur")
pokemon1.hasType = [grama, venenoso]
pokemon1.hasColor = [verde]
pokemon1.hasCategory = [normal]
pokemon1.hasPhysicalTrait = [pes, maos, focinho, orelhas, boca]
pokemon1.hasDiverseTraits = [anda_de_quatro]

# Ivysaur

# Venusaur

# Charmander
pokemon4 = onto.Pokemon("Charmander")
pokemon4.hasType = [fogo]
pokemon4.hasColor = [laranja]
pokemon4.hasCategory = [normal]
pokemon4.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon4.hasDiverseTraits = [anda_de_dois]

# Charmaleon

# Charizard

# Squirtle
pokemon7 = onto.Pokemon("Squirtle")
pokemon7.hasType = [agua]
pokemon7.hasColor = [azul]
pokemon7.hasCategory = [normal]
pokemon7.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon7.hasDiverseTraits = [anda_de_dois]

# Wartortle

# Blastoise

# Caterpie

# Metapod

# Butterfree

# Weedle

# Kakuna

# Beedrill

# Pidgey

# Pidgeotto

# Pidgeot

# Rattata

# Raticate

# Spearow

# Fearow

# Ekans

# Arbok

# Pikachu

# Raichu

# Sandshrew

# Sandslash

# Nidoran f

# Nidorina

# Nidoqueen

# Nidoran m

# Nidorino

# Nidoking

# Clefairy

# Clefable

# Vulpix

# Ninetales

# Jigglypuff

# Wigglytuff

# Zubat

# Golbat

# Odish

# Gloom

# Vileplume

# Paras

# Parasect

# Venonat

# Venomoth

# Diglet

# Dugtrio

# Meowth

# Persian

# Psyduck

# Golduck

# Mankey

# Primaepe

# Growlith

# Arcanine

# Poliwag

# Poliwhirl

# Poliwrath

# Abra

# Kadabra

# Alakazam

# Machop

# Machoke

# Machamp

# Bellsprout

# Weepinbell

# Victreebel

# Tentacool

# Tentacruel

# Geodude

# Graveler

# Golem

# POnyta

# Rapidash

# Slowpoke

# Slowbro

# Magnemite

# Magneton

# Farfetch'd

# Doduo

# Dodrio

# Seel

# Dewgong

# Grimer

# Muk

# Shellder

# Cloyster

# Gastly

# Haunter

# Gengar

# Onix

# Drowzee

# Hypno

# Krabby

# Kingler

# Voltbord

# Electrode

# Exeggcute

# Exeggutor

# Cubone

# Marowak

# Hitmonlee

# Hitmonchan

# Lickitung

# Koffing

# Weezing

# Rhydorn

# Rhydon

# Chansey

# Tangela

# Kangaskhan

# Horsea

# Seadra

# Goldeen

# Seaking

# Staryu

# Starmie

# Mr. Mime

# Scyther

# Jynx

# Electabuzz

# Magmar

# Pinsir

# Tauros

# Magikarp

# Gyarados

# Lapras

# Ditto

# Eevee

# Vaporeon

# Jolteon

# Flareon

# Porygon

# Omanyte

# Omastar

# Kabuto

# Kabutops

# Aerodactyl

# Snorlax

# Articuno
pokemon144 = onto.Pokemon("Articuno")
pokemon144.hasType = [eletrico, voador]
pokemon144.hasColor = [azul]
pokemon144.hasCategory = [lendario]
pokemon144.hasPhysicalTrait = [pes, asas, bico, cauda, boca]
pokemon144.hasDiverseTraits = [anda_de_dois]

# Zapdos
pokemon145 = onto.Pokemon("Zapdos")
pokemon145.hasType = [eletrico, voador]
pokemon145.hasColor = [amarelo]
pokemon145.hasCategory = [lendario]
pokemon145.hasPhysicalTrait = [pes, asas, bico, cauda, boca]
pokemon145.hasDiverseTraits = [anda_de_dois]

# Moltres
pokemon146 = onto.Pokemon("Moltres")
pokemon146.hasType = [fogo, voador]
pokemon146.hasColor = [laranja]
pokemon146.hasCategory = [lendario]
pokemon146.hasPhysicalTrait = [pes, asas, bico, cauda, boca]
pokemon146.hasDiverseTraits = [anda_de_dois]

# Dratini
pokemon147 = onto.Pokemon("Dratini")
pokemon147.hasType = [dragao]
pokemon147.hasColor = [azul]
pokemon147.hasCategory = [normal]
pokemon147.hasPhysicalTrait = [focinho, boca, cauda]

# Dragonair
pokemon148 = onto.Pokemon("Dragonair")
pokemon148.hasType = [dragao]
pokemon148.hasColor = [azul]
pokemon148.hasCategory = [normal]
pokemon148.hasPhysicalTrait = [focinho, boca, cauda]
pokemon148.hasDiverseTraits = [evolucao]

# Dragonite
pokemon149 = onto.Pokemon("Dragonite")
pokemon149.hasType = [dragao, voador]
pokemon149.hasColor = [amarelo]
pokemon149.hasCategory = [normal]
pokemon149.hasPhysicalTrait = [focinho, boca, cauda, pes, maos, asas]
pokemon149.hasDiverseTraits = [anda_de_dois, evolucao]

# Mewtwo
pokemon150 = onto.Pokemon("Mewtwo")
pokemon150.hasType = [psiquico]
pokemon150.hasColor = [rosa]
pokemon150.hasCategory = [lendario]
pokemon150.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon150.hasDiverseTraits = [anda_de_dois]

# Mew
pokemon151 = onto.Pokemon("Mew")
pokemon151.hasType = [psiquico]
pokemon151.hasColor = [rosa]
pokemon151.hasCategory = [mitico]
pokemon151.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda]
pokemon151.hasDiverseTraits = [anda_de_dois]

# Salvar a ontologia em um arquivo RDF
onto.save("pokemon_ontology.owl", format="rdfxml")