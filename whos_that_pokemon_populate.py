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
pokemon51 = onto.Pokemon("Dugtrio")
pokemon51.hasType = [solo]
pokemon51.hasColor = [marrom]
pokemon51.hasCategory = [normal]
pokemon51.hasPhysicalTrait = [focinho, cauda, boca]
pokemon51.hasDiverseTraits = [evolucao, cabecas]

# Meowth
pokemon52 = onto.Pokemon("Meowth")
pokemon52.hasType = [normal]
pokemon52.hasColor = [marrom_claro]
pokemon52.hasCategory = [normal]
pokemon52.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon52.hasDiverseTraits = [anda_de_dois]

# Persian
pokemon53 = onto.Pokemon("Persian")
pokemon53.hasType = [normal]
pokemon53.hasColor = [marrom_claro]
pokemon53.hasCategory = [normal]
pokemon53.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon53.hasDiverseTraits = [anda_de_quatro, evolucao]

# Psyduck
pokemon54 = onto.Pokemon("Psyduck")
pokemon54.hasType = [agua]
pokemon54.hasColor = [amarelo]
pokemon54.hasCategory = [normal]
pokemon54.hasPhysicalTrait = [pes, maos, bico, cauda, boca]
pokemon54.hasDiverseTraits = [anda_de_dois]

# Golduck
pokemon55 = onto.Pokemon("Golduck")
pokemon55.hasType = [agua]
pokemon55.hasColor = [azul]
pokemon55.hasCategory = [normal]
pokemon55.hasPhysicalTrait = [pes, maos, bico, cauda, boca]
pokemon55.hasDiverseTraits = [anda_de_dois, evolucao]

# Mankey
pokemon56 = onto.Pokemon("Mankey")
pokemon56.hasType = [lutador]
pokemon56.hasColor = [marrom_claro]
pokemon56.hasCategory = [normal]
pokemon56.hasPhysicalTrait = [pes, maos, focinho, cauda, orelhas]
pokemon56.hasDiverseTraits = [anda_de_dois]

# Primeape
pokemon57 = onto.Pokemon("Primeape")
pokemon57.hasType = [lutador]
pokemon57.hasColor = [marrom_claro]
pokemon57.hasCategory = [normal]
pokemon57.hasPhysicalTrait = [pes, maos, focinho, orelhas]
pokemon57.hasDiverseTraits = [anda_de_dois, evolucao]

# Growlith
pokemon58 = onto.Pokemon("Growlith")
pokemon58.hasType = [fogo]
pokemon58.hasColor = [laranja]
pokemon58.hasCategory = [normal]
pokemon58.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon58.hasDiverseTraits = [anda_de_quatro]

# Arcanine
pokemon59 = onto.Pokemon("Arcanine")
pokemon59.hasType = [fogo]
pokemon59.hasColor = [laranja]
pokemon59.hasCategory = [normal]
pokemon59.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon59.hasDiverseTraits = [anda_de_quatro, evolucao]

# Poliwag
pokemon60 = onto.Pokemon("Poliwag")
pokemon60.hasType = [agua]
pokemon60.hasColor = [azul]
pokemon60.hasCategory = [normal]
pokemon60.hasPhysicalTrait = [pes, focinho, boca, cauda]
pokemon60.hasDiverseTraits = [anda_de_dois, redondo]

# Poliwhirl
pokemon61 = onto.Pokemon("Poliwhirl")
pokemon61.hasType = [agua]
pokemon61.hasColor = [azul]
pokemon61.hasCategory = [normal]
pokemon61.hasPhysicalTrait = [pes, maos]
pokemon61.hasDiverseTraits = [anda_de_dois, redondo, evolucao]

# Poliwrath
pokemon62 = onto.Pokemon("Poliwrath")
pokemon62.hasType = [agua, lutador]
pokemon62.hasColor = [azul]
pokemon62.hasCategory = [normal]
pokemon62.hasPhysicalTrait = [pes, maos]
pokemon62.hasDiverseTraits = [anda_de_dois, redondo, evolucao]

# Abra
pokemon63 = onto.Pokemon("Abra")
pokemon63.hasType = [psiquico]
pokemon63.hasColor = [amarelo]
pokemon63.hasCategory = [normal]
pokemon63.hasPhysicalTrait = [pes, maos, orelhas, focinho, boca, cauda]
pokemon63.hasDiverseTraits = [anda_de_dois]

# Kadabra
pokemon64 = onto.Pokemon("Kadabra")
pokemon64.hasType = [psiquico]
pokemon64.hasColor = [amarelo]
pokemon64.hasCategory = [normal]
pokemon64.hasPhysicalTrait = [pes, maos, orelhas, focinho, boca, cauda]
pokemon64.hasDiverseTraits = [anda_de_dois, evolucao, segura_objeto]

# Alakazam
pokemon65 = onto.Pokemon("Alakazam")
pokemon65.hasType = [psiquico]
pokemon65.hasColor = [amarelo]
pokemon65.hasCategory = [normal]
pokemon65.hasPhysicalTrait = [pes, maos, orelhas, focinho, boca]
pokemon65.hasDiverseTraits = [anda_de_dois, evolucao, segura_objeto]

# Machop
pokemon66 = onto.Pokemon("Machop")
pokemon66.hasType = [lutador]
pokemon66.hasColor = [cinza]
pokemon66.hasCategory = [normal]
pokemon66.hasPhysicalTrait = [pes, maos, focinho, boca, cauda]
pokemon66.hasDiverseTraits = [anda_de_dois]

# Machoke
pokemon67 = onto.Pokemon("Machoke")
pokemon67.hasType = [lutador]
pokemon67.hasColor = [lilas]
pokemon67.hasCategory = [normal]
pokemon67.hasPhysicalTrait = [pes, maos, focinho, boca]
pokemon67.hasDiverseTraits = [anda_de_dois, evolucao]

# Machamp
pokemon68 = onto.Pokemon("Machamp")
pokemon68.hasType = [lutador]
pokemon68.hasColor = [lilas]
pokemon68.hasCategory = [normal]
pokemon68.hasPhysicalTrait = [pes, maos, focinho, boca]
pokemon68.hasDiverseTraits = [anda_de_dois, evolucao]

# Bellsprout
pokemon69 = onto.Pokemon("Bellsprout")
pokemon69.hasType = [grama, venenoso]
pokemon69.hasColor = [amarelo]
pokemon69.hasCategory = [normal]
pokemon69.hasPhysicalTrait = [boca]
pokemon69.hasDiverseTraits = [anda_de_dois]

# Weepinbell
pokemon70 = onto.Pokemon("Weepinbell")
pokemon70.hasType = [grama, venenoso]
pokemon70.hasColor = [amarelo]
pokemon70.hasCategory = [normal]
pokemon70.hasPhysicalTrait = [boca]
pokemon70.hasDiverseTraits = [evolucao]

# Victreebel
pokemon71 = onto.Pokemon("Victreebel")
pokemon71.hasType = [grama, venenoso]
pokemon71.hasColor = [amarelo]
pokemon71.hasCategory = [normal]
pokemon71.hasPhysicalTrait = [boca]
pokemon71.hasDiverseTraits = [evolucao]

# Tentacool
pokemon72 = onto.Pokemon("Tentacool")
pokemon72.hasType = [agua, venenoso]
pokemon72.hasColor = [azul]
pokemon72.hasCategory = [normal]
pokemon72.hasPhysicalTrait = [bico]
pokemon72.hasDiverseTraits = []

# Tentacruel
pokemon73 = onto.Pokemon("Tentacruel")
pokemon73.hasType = [agua, venenoso]
pokemon73.hasColor = [azul]
pokemon73.hasCategory = [normal]
pokemon73.hasPhysicalTrait = [bico]
pokemon73.hasDiverseTraits = [evolucao]

# Geodude
pokemon74 = onto.Pokemon("Geodude")
pokemon74.hasType = [rocha, solo]
pokemon74.hasColor = [marrom]
pokemon74.hasCategory = [normal]
pokemon74.hasPhysicalTrait = [boca, maos]
pokemon74.hasDiverseTraits = [redondo]

# Graveler
pokemon75 = onto.Pokemon("Graveler")
pokemon75.hasType = [rocha, solo]
pokemon75.hasColor = [marrom]
pokemon75.hasCategory = [normal]
pokemon75.hasPhysicalTrait = [boca, maos]
pokemon75.hasDiverseTraits = [redondo, evolucao]

# Golem
pokemon76 = onto.Pokemon("Golem")
pokemon76.hasType = [rocha, solo]
pokemon76.hasColor = [marrom]
pokemon76.hasCategory = [normal]
pokemon76.hasPhysicalTrait = [boca, maos, focinho]
pokemon76.hasDiverseTraits = [redondo, evolucao]

# Ponyta
pokemon77 = onto.Pokemon("Ponyta")
pokemon77.hasType = [fogo]
pokemon77.hasColor = [branco]
pokemon77.hasCategory = [normal]
pokemon77.hasPhysicalTrait = [focinho, boca, orelhas, cauda]
pokemon77.hasDiverseTraits = [anda_de_quatro]

# Rapidash
pokemon78 = onto.Pokemon("Rapidash")
pokemon78.hasType = [fogo]
pokemon78.hasColor = [branco]
pokemon78.hasCategory = [normal]
pokemon78.hasPhysicalTrait = [focinho, boca, orelhas, cauda, chifres]
pokemon78.hasDiverseTraits = [anda_de_quatro, evolucao]

# Slowpoke
pokemon79 = onto.Pokemon("Slowpoke")
pokemon79.hasType = [agua, psiquico]
pokemon79.hasColor = [rosa]
pokemon79.hasCategory = [normal]
pokemon79.hasPhysicalTrait = [pes, maos, focinho, boca, orelhas, cauda]
pokemon79.hasDiverseTraits = [anda_de_dois, anda_de_quatro]

# Slowbro
pokemon80 = onto.Pokemon("Slowbro")
pokemon80.hasType = [agua, psiquico]
pokemon80.hasColor = [rosa]
pokemon80.hasCategory = [normal]
pokemon80.hasPhysicalTrait = [pes, maos, focinho, boca, orelhas, cauda]
pokemon80.hasDiverseTraits = [anda_de_dois, evolucao]

# Magnemite
pokemon81 = onto.Pokemon("Magnemite")
pokemon81.hasType = [aco, eletrico]
pokemon81.hasColor = [cinza]
pokemon81.hasCategory = [normal]
pokemon81.hasPhysicalTrait = []
pokemon81.hasDiverseTraits = [redondo, parece_objeto]

# Magneton
pokemon82 = onto.Pokemon("Magneton")
pokemon82.hasType = [aco, eletrico]
pokemon82.hasColor = [cinza]
pokemon82.hasCategory = [normal]
pokemon82.hasPhysicalTrait = []
pokemon82.hasDiverseTraits = [redondo, parece_objeto, cabecas, evolucao]

# Farfetchd
pokemon83 = onto.Pokemon("Farfetchd")
pokemon83.hasType = [normal, voador]
pokemon83.hasColor = [marrom]
pokemon83.hasCategory = [normal]
pokemon83.hasPhysicalTrait = [asas, pes, bico, boca, cauda]
pokemon83.hasDiverseTraits = [segura_objeto, anda_de_dois]

# Doduo
pokemon84 = onto.Pokemon("Doduo")
pokemon84.hasType = [normal, voador]
pokemon84.hasColor = [marrom]
pokemon84.hasCategory = [normal]
pokemon84.hasPhysicalTrait = [pes, bico, boca, cauda]
pokemon84.hasDiverseTraits = [anda_de_dois, cabecas]

# Dodrio
pokemon85 = onto.Pokemon("Dodrio")
pokemon85.hasType = [normal, voador]
pokemon85.hasColor = [marrom]
pokemon85.hasCategory = [normal]
pokemon85.hasPhysicalTrait = [pes, bico, boca, cauda]
pokemon85.hasDiverseTraits = [anda_de_dois, cabecas, evolucao]

# Seel
pokemon86 = onto.Pokemon("Seel")
pokemon86.hasType = [agua]
pokemon86.hasColor = [branco]
pokemon86.hasCategory = [normal]
pokemon86.hasPhysicalTrait = [maos, focinho, boca, cauda, chifres]
pokemon86.hasDiverseTraits = []

# Dewgong
pokemon87 = onto.Pokemon("Dewgong")
pokemon87.hasType = [agua, gelo]
pokemon87.hasColor = [branco]
pokemon87.hasCategory = [normal]
pokemon87.hasPhysicalTrait = [maos, focinho, boca, cauda, chifres]
pokemon87.hasDiverseTraits = [evolucao]

# Grimer
pokemon88 = onto.Pokemon("Grimer")
pokemon88.hasType = [venenoso]
pokemon88.hasColor = [roxo]
pokemon88.hasCategory = [normal]
pokemon88.hasPhysicalTrait = [maos, boca]
pokemon88.hasDiverseTraits = []

# Muk
pokemon89 = onto.Pokemon("Muk")
pokemon89.hasType = [venenoso]
pokemon89.hasColor = [roxo]
pokemon89.hasCategory = [normal]
pokemon89.hasPhysicalTrait = [maos, boca]
pokemon89.hasDiverseTraits = [evolucao]

# Shellder
pokemon90 = onto.Pokemon("Shellder")
pokemon90.hasType = [agua]
pokemon90.hasColor = [roxo]
pokemon90.hasCategory = [normal]
pokemon90.hasPhysicalTrait = [boca]
pokemon90.hasDiverseTraits = []

# Cloyster
pokemon91 = onto.Pokemon("Cloyster")
pokemon91.hasType = [agua, gelo]
pokemon91.hasColor = [roxo]
pokemon91.hasCategory = [normal]
pokemon91.hasPhysicalTrait = [boca, chifres]
pokemon91.hasDiverseTraits = [evolucao]

# Gastly
pokemon92 = onto.Pokemon("Gastly")
pokemon92.hasType = [venenoso, fantasma]
pokemon92.hasColor = [roxo]
pokemon92.hasCategory = [normal]
pokemon92.hasPhysicalTrait = [boca]
pokemon92.hasDiverseTraits = [redondo]

# Haunter
pokemon93 = onto.Pokemon("Haunter")
pokemon93.hasType = [venenoso, fantasma]
pokemon93.hasColor = [roxo]
pokemon93.hasCategory = [normal]
pokemon93.hasPhysicalTrait = [boca, maos, orelhas, cauda]
pokemon93.hasDiverseTraits = [evolucao]

# Gengar
pokemon94 = onto.Pokemon("Gengar")
pokemon94.hasType = [venenoso, fantasma]
pokemon94.hasColor = [roxo]
pokemon94.hasCategory = [normal]
pokemon94.hasPhysicalTrait = [boca, maos, orelhas, pes, cauda]
pokemon94.hasDiverseTraits = [evolucao, anda_de_dois]

# Onix
pokemon95 = onto.Pokemon("Onix")
pokemon95.hasType = [solo, rocha]
pokemon95.hasColor = [cinza]
pokemon95.hasCategory = [normal]
pokemon95.hasPhysicalTrait = [boca, focinho, chifres, cauda]
pokemon95.hasDiverseTraits = []

# Drowzee
pokemon96 = onto.Pokemon("Drowzee")
pokemon96.hasType = [psiquico]
pokemon96.hasColor = [amarelo]
pokemon96.hasCategory = [normal]
pokemon96.hasPhysicalTrait = [boca, focinho, orelhas, pes, maos]
pokemon96.hasDiverseTraits = [anda_de_dois]

# Hypno
pokemon97 = onto.Pokemon("Hypno")
pokemon97.hasType = [psiquico]
pokemon97.hasColor = [amarelo]
pokemon97.hasCategory = [normal]
pokemon97.hasPhysicalTrait = [focinho, orelhas, pes, maos]
pokemon97.hasDiverseTraits = [anda_de_dois, evolucao, segura_objeto]

# Krabby
pokemon98 = onto.Pokemon("Krabby")
pokemon98.hasType = [agua]
pokemon98.hasColor = [laranja]
pokemon98.hasCategory = [normal]
pokemon98.hasPhysicalTrait = [boca, pes]
pokemon98.hasDiverseTraits = [anda_de_quatro]

# Kingler
pokemon99 = onto.Pokemon("Kingler")
pokemon99.hasType = [agua]
pokemon99.hasColor = [laranja]
pokemon99.hasCategory = [normal]
pokemon99.hasPhysicalTrait = [boca, pes]
pokemon99.hasDiverseTraits = [anda_de_quatro, evolucao]

# Voltborb
pokemon100 = onto.Pokemon("Voltborb")
pokemon100.hasType = [eletrico]
pokemon100.hasColor = [vermelho]
pokemon100.hasCategory = [normal]
pokemon100.hasPhysicalTrait = []
pokemon100.hasDiverseTraits = [parece_objeto, redondo]

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