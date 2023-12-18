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
fada = onto.Type("Fada")

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

pokemon2 = onto.Pokemon("Ivysaur")
pokemon2.hasType = [grama, venenoso]
pokemon2.hasColor = [verde]
pokemon2.hasCategory = [normal]
pokemon2.hasPhysicalTrait = [pes, maos, focinho, orelhas, boca]
pokemon2.hasDiverseTraits = [evolucao, anda_de_quatro]

# Venusaur

pokemon3 = onto.Pokemon("Venusaur")
pokemon3.hasType = [grama, venenoso]
pokemon3.hasColor = [verde]
pokemon3.hasCategory = [normal]
pokemon3.hasPhysicalTrait = [pes, maos, focinho, orelhas, boca]
pokemon3.hasDiverseTraits = [evolucao, anda_de_quatro]

# Charmander
pokemon4 = onto.Pokemon("Charmander")
pokemon4.hasType = [fogo]
pokemon4.hasColor = [laranja]
pokemon4.hasCategory = [normal]
pokemon4.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon4.hasDiverseTraits = [anda_de_dois]

# Charmaleon

pokemon5 = onto.Pokemon("Charmaleon")
pokemon5.hasType = [fogo]
pokemon5.hasColor = [laranja]
pokemon5.hasCategory = [normal]
pokemon5.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon5.hasDiverseTraits = [evolucao, anda_de_dois]

# Charizard

pokemon6 = onto.Pokemon("Charizard")
pokemon6.hasType = [fogo, voador]
pokemon6.hasColor = [laranja]
pokemon6.hasCategory = [normal]
pokemon6.hasPhysicalTrait = [pes, maos, focinho, cauda, boca, asas]
pokemon6.hasDiverseTraits = [evolucao, anda_de_dois]


# Squirtle
pokemon7 = onto.Pokemon("Squirtle")
pokemon7.hasType = [agua]
pokemon7.hasColor = [azul]
pokemon7.hasCategory = [normal]
pokemon7.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon7.hasDiverseTraits = [anda_de_dois]

# Wartortle

pokemon8 = onto.Pokemon("Wartortle")
pokemon8.hasType = [agua]
pokemon8.hasColor = [azul]
pokemon8.hasCategory = [normal]
pokemon8.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon8.hasDiverseTraits = [evolucao, anda_de_dois]

# Blastoise

pokemon9 = onto.Pokemon("Blastoise")
pokemon9.hasType = [agua]
pokemon9.hasColor = [azul]
pokemon9.hasCategory = [normal]
pokemon9.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon9.hasDiverseTraits = [evolucao, anda_de_dois]

# Caterpie

pokemon10 = onto.Pokemon("Caterpie")
pokemon10.hasType = [inseto]
pokemon10.hasColor = [verde]
pokemon10.hasCategory = [normal]
pokemon10.hasPhysicalTrait = [cauda]
pokemon10.hasDiverseTraits = []

# Metapod

pokemon11 = onto.Pokemon("Metapod")
pokemon11.hasType = [inseto]
pokemon11.hasColor = [verde]
pokemon11.hasCategory = [normal]
pokemon11.hasPhysicalTrait = []
pokemon11.hasDiverseTraits = [evolucao]

# Butterfree

pokemon12 = onto.Pokemon("Butterfree")
pokemon12.hasType = [inseto, voador]
pokemon12.hasColor = [roxo]
pokemon12.hasCategory = [normal]
pokemon12.hasPhysicalTrait = [boca, asas, pes]
pokemon12.hasDiverseTraits = [evolucao]

# Weedle

pokemon13 = onto.Pokemon("Weedle")
pokemon13.hasType = [inseto, venenoso]
pokemon13.hasColor = [marrom]
pokemon13.hasCategory = [normal]
pokemon13.hasPhysicalTrait = [cauda, chifres]
pokemon13.hasDiverseTraits = []

# Kakuna

pokemon14 = onto.Pokemon("Kakuna")
pokemon14.hasType = [inseto, venenoso]
pokemon14.hasColor = [amarelo]
pokemon14.hasCategory = [normal]
pokemon14.hasPhysicalTrait = []
pokemon14.hasDiverseTraits = [evolucao]

# Beedrill

pokemon15 = onto.Pokemon("Beedrill")
pokemon15.hasType = [inseto, venenoso, voador]
pokemon15.hasColor = [amarelo]
pokemon15.hasCategory = [normal]
pokemon15.hasPhysicalTrait = [asas, chifres]
pokemon15.hasDiverseTraits = [evolucao]

# Pidgey

pokemon16 = onto.Pokemon("Pidgey")
pokemon16.hasType = [normal, voador]
pokemon16.hasColor = [marrom]
pokemon16.hasCategory = [normal]
pokemon16.hasPhysicalTrait = [asas, bico, pes]
pokemon16.hasDiverseTraits = [anda_de_dois]

# Pidgeotto

pokemon17 = onto.Pokemon("Pidgeotto")
pokemon17.hasType = [normal, voador]
pokemon17.hasColor = [marrom]
pokemon17.hasCategory = [normal]
pokemon17.hasPhysicalTrait = [asas, bico, pes]
pokemon17.hasDiverseTraits = [evolucao, anda_de_dois]

# Pidgeot

pokemon18 = onto.Pokemon("Pidgeot")
pokemon18.hasType = [normal, voador]
pokemon18.hasColor = [marrom]
pokemon18.hasCategory = [normal]
pokemon18.hasPhysicalTrait = [asas, bico, pes]
pokemon18.hasDiverseTraits = [evolucao, anda_de_dois]

# Rattata

pokemon19 = onto.Pokemon("Rattata")
pokemon19.hasType = [normal]
pokemon19.hasColor = [roxo]
pokemon19.hasCategory = [normal]
pokemon19.hasPhysicalTrait = [cauda, boca, orelhas]
pokemon19.hasDiverseTraits = [anda_de_quatro]

# Raticate

pokemon20 = onto.Pokemon("Raticate")
pokemon20.hasType = [normal]
pokemon20.hasColor = [marrom]
pokemon20.hasCategory = [normal]
pokemon20.hasPhysicalTrait = [cauda, boca, orelhas, pes]
pokemon20.hasDiverseTraits = [evolucao, anda_de_quatro]

# Spearow

pokemon21 = onto.Pokemon("Spearow")
pokemon21.hasType = [normal, voador]
pokemon21.hasColor = [marrom]
pokemon21.hasCategory = [normal]
pokemon21.hasPhysicalTrait = [asas, bico]
pokemon21.hasDiverseTraits = []

# Fearow

pokemon22 = onto.Pokemon("Fearow")
pokemon22.hasType = [normal, voador]
pokemon22.hasColor = [marrom]
pokemon22.hasCategory = [normal]
pokemon22.hasPhysicalTrait = [asas, bico]
pokemon22.hasDiverseTraits = [evolucao]

# Ekans

pokemon23 = onto.Pokemon("Ekans")
pokemon23.hasType = [venenoso]
pokemon23.hasColor = [roxo]
pokemon23.hasCategory = [normal]
pokemon23.hasPhysicalTrait = [cauda, boca]
pokemon23.hasDiverseTraits = []

# Arbok

pokemon24 = onto.Pokemon("Arbok")
pokemon24.hasType = [venenoso]
pokemon24.hasColor = [roxo]
pokemon24.hasCategory = [normal]
pokemon24.hasPhysicalTrait = [cauda, boca]
pokemon24.hasDiverseTraits = [evolucao]

# Pikachu

pokemon25 = onto.Pokemon("Pikachu")
pokemon25.hasType = [eletrico]
pokemon25.hasColor = [amarelo]
pokemon25.hasCategory = [normal]
pokemon25.hasPhysicalTrait = [cauda, pes, maos, focinho, orelhas, boca]
pokemon25.hasDiverseTraits = [anda_de_dois, anda_de_quatro]

# Raichu

pokemon26 = onto.Pokemon("Raichu")
pokemon26.hasType = [eletrico]
pokemon26.hasColor = [laranja]
pokemon26.hasCategory = [normal]
pokemon26.hasPhysicalTrait = [cauda, pes, maos, focinho, orelhas, boca]
pokemon26.hasDiverseTraits = [anda_de_dois, anda_de_quatro]

# Sandslash

pokemon27 = onto.Pokemon("Sandslash")
pokemon27.hasType = [solo]
pokemon27.hasColor = [amarelo]
pokemon27.hasCategory = [normal]
pokemon27.hasPhysicalTrait = [pes, maos, focinho, cauda, boca]
pokemon27.hasDiverseTraits = [evolucao]

# Nidoran f

pokemon28 = onto.Pokemon("Nidoran_f")
pokemon28.hasType = [venenoso]
pokemon28.hasColor = [roxo]
pokemon28.hasCategory = [normal]
pokemon28.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon28.hasDiverseTraits = [anda_de_quatro]

# Nidorina

pokemon29 = onto.Pokemon("Nidorina")
pokemon29.hasType = [venenoso]
pokemon29.hasColor = [roxo]
pokemon29.hasCategory = [normal]
pokemon29.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon29.hasDiverseTraits = [evolucao, anda_de_quatro, anda_de_dois]

# Nidoqueen

pokemon30 = onto.Pokemon("Nidoqueen")
pokemon30.hasType = [venenoso, solo]
pokemon30.hasColor = [roxo]
pokemon30.hasCategory = [normal]
pokemon30.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon30.hasDiverseTraits = [evolucao, anda_de_quatro, anda_de_dois]

# Nidoran m

pokemon31 = onto.Pokemon("Nidoran_m")
pokemon31.hasType = [venenoso]
pokemon31.hasColor = [roxo]
pokemon31.hasCategory = [normal]
pokemon31.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon31.hasDiverseTraits = [anda_de_quatro]

# Nidorino

pokemon32 = onto.Pokemon("Nidorino")
pokemon32.hasType = [venenoso]
pokemon32.hasColor = [roxo]
pokemon32.hasCategory = [normal]
pokemon32.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon32.hasDiverseTraits = [evolucao, anda_de_quatro]

# Nidoking

pokemon33 = onto.Pokemon("Nidoking")
pokemon33.hasType = [venenoso, solo]
pokemon33.hasColor = [roxo]
pokemon33.hasCategory = [normal]
pokemon33.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon33.hasDiverseTraits = [evolucao, anda_de_quatro]

# Clefairy

pokemon34 = onto.Pokemon("Clefairy")
pokemon34.hasType = [normal]
pokemon34.hasColor = [rosa]
pokemon34.hasCategory = [normal]
pokemon34.hasPhysicalTrait = [pes, maos, orelhas, boca]
pokemon34.hasDiverseTraits = [anda_de_dois]

# Clefable

pokemon35 = onto.Pokemon("Clefable")
pokemon35.hasType = [normal]
pokemon35.hasColor = [rosa]
pokemon35.hasCategory = [normal]
pokemon35.hasPhysicalTrait = [pes, maos, orelhas, boca]
pokemon35.hasDiverseTraits = [anda_de_dois, evolucao]

# Vulpix

pokemon36 = onto.Pokemon("Vulpix")
pokemon36.hasType = [fogo]
pokemon36.hasColor = [laranja]
pokemon36.hasCategory = [normal]
pokemon36.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon36.hasDiverseTraits = [anda_de_quatro]

# Ninetales

pokemon37 = onto.Pokemon("Ninetales")
pokemon37.hasType = [fogo]
pokemon37.hasColor = [laranja]
pokemon37.hasCategory = [normal]
pokemon37.hasPhysicalTrait = [pes, maos, focinho, orelhas, cauda, boca]
pokemon37.hasDiverseTraits = [anda_de_quatro, evolucao]

# Jigglypuff

pokemon38 = onto.Pokemon("Jigglypuff")
pokemon38.hasType = [normal]
pokemon38.hasColor = [rosa]
pokemon38.hasCategory = [normal]
pokemon38.hasPhysicalTrait = [pes, maos, orelhas, boca]
pokemon38.hasDiverseTraits = [anda_de_dois, redondo]

# Wigglytuff

pokemon39 = onto.Pokemon("Wigglytuff")
pokemon39.hasType = [normal]
pokemon39.hasColor = [rosa]
pokemon39.hasCategory = [normal]
pokemon39.hasPhysicalTrait = [pes, maos, orelhas, boca]
pokemon39.hasDiverseTraits = [anda_de_dois, evolucao]

# Zubat
pokemon40 = onto.Pokemon("Zubat")
pokemon40.hasType = [venenoso, voador]
pokemon40.hasColor = [roxo]
pokemon40.hasCategory = [normal]
pokemon40.hasPhysicalTrait = [asas, boca]
pokemon40.hasDiverseTraits = []

# Golbat
pokemon41 = onto.Pokemon("Golbat")
pokemon41.hasType = [venenoso, voador]
pokemon41.hasColor = [roxo]
pokemon41.hasCategory = [normal]
pokemon41.hasPhysicalTrait = [asas, boca]
pokemon41.hasDiverseTraits = [evolucao]

# Oddish
pokemon42 = onto.Pokemon("Oddish")
pokemon42.hasType = [grama, venenoso]
pokemon42.hasColor = [azul]
pokemon42.hasCategory = [normal]
pokemon42.hasPhysicalTrait = [boca]
pokemon42.hasDiverseTraits = []

# Gloom
pokemon43 = onto.Pokemon("Gloom")
pokemon43.hasType = [grama, venenoso]
pokemon43.hasColor = [azul]
pokemon43.hasCategory = [normal]
pokemon43.hasPhysicalTrait = [boca]
pokemon43.hasDiverseTraits = [evolucao]

# Vileplume
pokemon44 = onto.Pokemon("Vileplume")
pokemon44.hasType = [grama, venenoso]
pokemon44.hasColor = [azul]
pokemon44.hasCategory = [normal]
pokemon44.hasPhysicalTrait = [boca]
pokemon44.hasDiverseTraits = [evolucao]

# Paras
pokemon45 = onto.Pokemon("Paras")
pokemon45.hasType = [inseto, grama]
pokemon45.hasColor = [vermelho]
pokemon45.hasCategory = [normal]
pokemon45.hasPhysicalTrait = [boca]
pokemon45.hasDiverseTraits = []

# Parasect
pokemon46 = onto.Pokemon("Parasect")
pokemon46.hasType = [inseto, grama]
pokemon46.hasColor = [vermelho]
pokemon46.hasCategory = [normal]
pokemon46.hasPhysicalTrait = [boca]
pokemon46.hasDiverseTraits = [evolucao]

# Venonat
pokemon47 = onto.Pokemon("Venonat")
pokemon47.hasType = [inseto, venenoso]
pokemon47.hasColor = [roxo]
pokemon47.hasCategory = [normal]
pokemon47.hasPhysicalTrait = [boca]
pokemon47.hasDiverseTraits = []

# Venomoth
pokemon48 = onto.Pokemon("Venomoth")
pokemon48.hasType = [inseto, venenoso]
pokemon48.hasColor = [roxo]
pokemon48.hasCategory = [normal]
pokemon48.hasPhysicalTrait = [boca]
pokemon48.hasDiverseTraits = [evolucao]

# Diglet

pokemon50 = onto.Pokemon("Dugtrio")
pokemon50.hasType = [solo]
pokemon50.hasColor = [marrom]
pokemon50.hasCategory = [normal]
pokemon50.hasPhysicalTrait = [focinho, cauda, boca]
pokemon50.hasDiverseTraits = []

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

pokemon101 = onto.Pokemon("Electrode")
pokemon101.hasType = [eletrico]
pokemon101.hasColor = [vermelho]
pokemon101.hasCategory = [normal]
pokemon101.hasPhysicalTrait = [boca]
pokemon101.hasDiverseTraits = [parece_objeto, redondo, evolucao]

# Exeggcute

pokemon102 = onto.Pokemon("Exeggcute")
pokemon102.hasType = [grama, psiquico]
pokemon102.hasColor = [rosa]
pokemon102.hasCategory = [normal]
pokemon102.hasPhysicalTrait = [boca]
pokemon102.hasDiverseTraits = [redondo, cabecas]

# Exeggutor

pokemon103 = onto.Pokemon("Exeggutor")
pokemon103.hasType = [grama, psiquico]
pokemon103.hasColor = [marrom_claro]
pokemon103.hasCategory = [normal]
pokemon103.hasPhysicalTrait = [pes, boca]
pokemon103.hasDiverseTraits = [anda_de_dois, evolucao, cabecas]

# Cubone

pokemon104 = onto.Pokemon("Cubone")
pokemon104.hasType = [solo]
pokemon104.hasColor = [marrom_claro]
pokemon104.hasCategory = [normal]
pokemon104.hasPhysicalTrait = [pes, maos, cauda, focinho, chifres]
pokemon104.hasDiverseTraits = [anda_de_dois, segura_objeto]

# Marowak

pokemon105 = onto.Pokemon("Marowak")
pokemon105.hasType = [solo]
pokemon105.hasColor = [marrom_claro]
pokemon105.hasCategory = [normal]
pokemon105.hasPhysicalTrait = [pes, maos, cauda, focinho, chifres]
pokemon105.hasDiverseTraits = [anda_de_dois, segura_objeto, evolucao]

# Hitmonlee

pokemon106 = onto.Pokemon("Hitmonlee")
pokemon106.hasType = [lutador]
pokemon106.hasColor = [marrom_claro]
pokemon106.hasCategory = [normal]
pokemon106.hasPhysicalTrait = [pes, maos]
pokemon106.hasDiverseTraits = [anda_de_dois]

# Hitmonchan

pokemon107 = onto.Pokemon("Hitmonchan")
pokemon107.hasType = [lutador]
pokemon107.hasColor = [marrom_claro]
pokemon107.hasCategory = [normal]
pokemon107.hasPhysicalTrait = [pes, maos, boca]
pokemon107.hasDiverseTraits = [anda_de_dois, evolucao]

# Lickitung

pokemon108 = onto.Pokemon("Lickitung")
pokemon108.hasType = [normal]
pokemon108.hasColor = [rosa]
pokemon108.hasCategory = [normal]
pokemon108.hasPhysicalTrait = [pes, maos, cauda, boca]
pokemon108.hasDiverseTraits = [anda_de_dois]

# Koffing

pokemon109 = onto.Pokemon("Koffing")
pokemon109.hasType = [venenoso]
pokemon109.hasColor = [roxo]
pokemon109.hasCategory = [normal]
pokemon109.hasPhysicalTrait = [boca]
pokemon109.hasDiverseTraits = [redondo]

# Weezing

pokemon110 = onto.Pokemon("Weezing")
pokemon110.hasType = [venenoso]
pokemon110.hasColor = [roxo]
pokemon110.hasCategory = [normal]
pokemon110.hasPhysicalTrait = [boca]
pokemon110.hasDiverseTraits = [redondo, evolucao, cabecas]

# Rhydorn

pokemon111 = onto.Pokemon("Rhyhorn")
pokemon111.hasType = [solo, rocha]
pokemon111.hasColor = [cinza]
pokemon111.hasCategory = [normal]
pokemon111.hasPhysicalTrait = [pes, chifres, boca, focinho]
pokemon111.hasDiverseTraits = [anda_de_quatro]

# Rhydon

pokemon112 = onto.Pokemon("Rhydon")
pokemon112.hasType = [solo, rocha]
pokemon112.hasColor = [cinza]
pokemon112.hasCategory = [normal]
pokemon112.hasPhysicalTrait = [pes, maos, chifres, boca, cauda, orelhas]
pokemon112.hasDiverseTraits = [anda_de_dois, evolucao]

# Chansey

pokemon113 = onto.Pokemon("Chansey")
pokemon113.hasType = [normal]
pokemon113.hasColor = [rosa]
pokemon113.hasCategory = [normal]
pokemon113.hasPhysicalTrait = [pes, maos, cauda, boca, orelhas]
pokemon113.hasDiverseTraits = [redondo, anda_de_dois, segura_objeto, evolucao]

# Tangela

pokemon114 = onto.Pokemon("Tangela")
pokemon114.hasType = [grama]
pokemon114.hasColor = [azul]
pokemon114.hasCategory = [normal]
pokemon114.hasPhysicalTrait = [pes]
pokemon114.hasDiverseTraits = [anda_de_dois]

# Kangaskhan

pokemon115 = onto.Pokemon("Kangaskhan")
pokemon115.hasType = [normal]
pokemon115.hasColor = [marrom_claro]
pokemon115.hasCategory = [normal]
pokemon115.hasPhysicalTrait = [pes, maos, cauda, boca, orelhas, focinho]
pokemon115.hasDiverseTraits = [anda_de_dois]

# Horsea

pokemon116 = onto.Pokemon("Horsea")
pokemon116.hasType = [agua]
pokemon116.hasColor = [azul]
pokemon116.hasCategory = [normal]
pokemon116.hasPhysicalTrait = [cauda, boca, orelhas]
pokemon116.hasDiverseTraits = []

# Seadra

pokemon117 = onto.Pokemon("Seadra")
pokemon117.hasType = [agua]
pokemon117.hasColor = [azul]
pokemon117.hasCategory = [normal]
pokemon117.hasPhysicalTrait = [cauda, boca, orelhas]
pokemon117.hasDiverseTraits = [evolucao]

# Goldeen

pokemon118 = onto.Pokemon("Goldeen")
pokemon118.hasType = [agua]
pokemon118.hasColor = [branco]
pokemon118.hasCategory = [normal]
pokemon118.hasPhysicalTrait = [cauda, boca, chifres]
pokemon118.hasDiverseTraits = []

# Seaking

pokemon119 = onto.Pokemon("Seaking")
pokemon119.hasType = [agua]
pokemon119.hasColor = [branco]
pokemon119.hasCategory = [normal]
pokemon119.hasPhysicalTrait = [cauda, boca, chifres]
pokemon119.hasDiverseTraits = [evolucao]

# Staryu

pokemon120 = onto.Pokemon("Staryu")
pokemon120.hasType = [agua]
pokemon120.hasColor = [marrom]
pokemon120.hasCategory = [normal]
pokemon120.hasPhysicalTrait = []
pokemon120.hasDiverseTraits = []

# Starmie

pokemon121 = onto.Pokemon("Starmie")
pokemon121.hasType = [agua, psiquico]
pokemon121.hasColor = [roxo]
pokemon121.hasCategory = [normal]
pokemon121.hasPhysicalTrait = []
pokemon121.hasDiverseTraits = [evolucao]

# Mr. Mime

pokemon122 = onto.Pokemon("Mr. Mime")
pokemon122.hasType = [psiquico, fada]
pokemon122.hasColor = [rosa]
pokemon122.hasCategory = [normal]
pokemon122.hasPhysicalTrait = [pes, maos, boca]
pokemon122.hasDiverseTraits = [evolucao, anda_de_dois]

# Scyther

pokemon123 = onto.Pokemon("Scyther")
pokemon123.hasType = [inseto, voador]
pokemon123.hasColor = [verde]
pokemon123.hasCategory = [normal]
pokemon123.hasPhysicalTrait = [pes, asas, focinho, boca]
pokemon123.hasDiverseTraits = [anda_de_dois]

# Jynx

pokemon124 = onto.Pokemon("Jynx")
pokemon124.hasType = [gelo, psiquico]
pokemon124.hasColor = [roxo]
pokemon124.hasCategory = [normal]
pokemon124.hasPhysicalTrait = [maos, boca]
pokemon124.hasDiverseTraits = [evolucao]

# Electabuzz

pokemon125 = onto.Pokemon("Electabuzz")
pokemon125.hasType = [eletrico]
pokemon125.hasColor = [amarelo]
pokemon125.hasCategory = [normal]
pokemon125.hasPhysicalTrait = [pes, maos, cauda, boca]
pokemon125.hasDiverseTraits = [anda_de_dois, evolucao]

# Magmar

pokemon126 = onto.Pokemon("Magmar")
pokemon126.hasType = [fogo]
pokemon126.hasColor = [laranja]
pokemon126.hasCategory = [normal]
pokemon126.hasPhysicalTrait = [pes, maos, cauda, bico]
pokemon126.hasDiverseTraits = [evolucao, anda_de_dois]

# Pinsir

pokemon127 = onto.Pokemon("Pinsir")
pokemon127.hasType = [inseto]
pokemon127.hasColor = [cinza]
pokemon127.hasCategory = [normal]
pokemon127.hasPhysicalTrait = [pes, maos, chifres, boca]
pokemon127.hasDiverseTraits = [anda_de_dois]

# Tauros

pokemon128 = onto.Pokemon("Tauros")
pokemon128.hasType = [normal]
pokemon128.hasColor = [marrom_claro]
pokemon128.hasCategory = [normal]
pokemon128.hasPhysicalTrait = [pes, cauda, focinho, chifres, boca]
pokemon128.hasDiverseTraits = [anda_de_quatro]

# Magikarp

pokemon129 = onto.Pokemon("Magikarp")
pokemon129.hasType = [agua]
pokemon129.hasColor = [laranja]
pokemon129.hasCategory = [normal]
pokemon129.hasPhysicalTrait = [cauda, boca]
pokemon129.hasDiverseTraits = []

# Gyarados

pokemon130 = onto.Pokemon("Gyarados")
pokemon130.hasType = [agua, voador]
pokemon130.hasColor = [azul]
pokemon130.hasCategory = [normal]
pokemon130.hasPhysicalTrait = [cauda, boca]
pokemon130.hasDiverseTraits = [evolucao]

# Lapras

pokemon131 = onto.Pokemon("Lapras")
pokemon131.hasType = [agua, gelo]
pokemon131.hasColor = [azul]
pokemon131.hasCategory = [normal]
pokemon131.hasPhysicalTrait = [cauda, focinho, orelhas, chifres]
pokemon131.hasDiverseTraits = []

# Ditto

pokemon132 = onto.Pokemon("Ditto")
pokemon132.hasType = [normal]
pokemon132.hasColor = [roxo]
pokemon132.hasCategory = [normal]
pokemon132.hasPhysicalTrait = [boca]
pokemon132.hasDiverseTraits = []

# Eevee

pokemon133 = onto.Pokemon("Eevee")
pokemon133.hasType = [normal]
pokemon133.hasColor = [marrom]
pokemon133.hasCategory = [normal]
pokemon133.hasPhysicalTrait = [pes, cauda, focinho, orelhas, boca]
pokemon133.hasDiverseTraits = [anda_de_quatro]

# Vaporeon

pokemon134 = onto.Pokemon("Vaporeon")
pokemon134.hasType = [agua]
pokemon134.hasColor = [azul]
pokemon134.hasCategory = [normal]
pokemon134.hasPhysicalTrait = [pes, cauda, focinho, orelhas, boca]
pokemon134.hasDiverseTraits = [evolucao, anda_de_quatro]

# Jolteon

pokemon135 = onto.Pokemon("Jolteon")
pokemon135.hasType = [eletrico]
pokemon135.hasColor = [amarelo]
pokemon135.hasCategory = [normal]
pokemon135.hasPhysicalTrait = [pes, cauda, focinho, orelhas, boca]
pokemon135.hasDiverseTraits = [evolucao, anda_de_quatro]

# Flareon

pokemon136 = onto.Pokemon("Flareon")
pokemon136.hasType = [fogo]
pokemon136.hasColor = [laranja]
pokemon136.hasCategory = [normal]
pokemon136.hasPhysicalTrait = [pes, cauda, focinho, orelhas, boca]
pokemon136.hasDiverseTraits = [evolucao, anda_de_quatro]

# Porygon

pokemon137 = onto.Pokemon("Porygon")
pokemon137.hasType = [normal]
pokemon137.hasColor = [rosa]
pokemon137.hasCategory = [normal]
pokemon137.hasPhysicalTrait = [cauda]
pokemon137.hasDiverseTraits = []

# Omanyte

pokemon138 = onto.Pokemon("Omanyte")
pokemon138.hasType = [rocha, agua]
pokemon138.hasColor = [azul]
pokemon138.hasCategory = [normal]
pokemon138.hasPhysicalTrait = []
pokemon138.hasDiverseTraits = []

# Omastar

pokemon139 = onto.Pokemon("Omastar")
pokemon139.hasType = [rocha, agua]
pokemon139.hasColor = [azul]
pokemon139.hasCategory = [normal]
pokemon139.hasPhysicalTrait = []
pokemon139.hasDiverseTraits = [evolucao]

# Kabuto

pokemon140 = onto.Pokemon("Kabuto")
pokemon140.hasType = [rocha, agua]
pokemon140.hasColor = [marrom]
pokemon140.hasCategory = [normal]
pokemon140.hasPhysicalTrait = []
pokemon140.hasDiverseTraits = [anda_de_quatro]

# Kabutops

pokemon141 = onto.Pokemon("Kabutops")
pokemon141.hasType = [rocha, agua]
pokemon141.hasColor = [marrom]
pokemon141.hasCategory = [normal]
pokemon141.hasPhysicalTrait = [cauda, pes]
pokemon141.hasDiverseTraits = [evolucao, anda_de_dois]

# Aerodactyl

pokemon142 = onto.Pokemon("Aerodactyl")
pokemon142.hasType = [rocha, voador]
pokemon142.hasColor = [roxo]
pokemon142.hasCategory = [normal]
pokemon142.hasPhysicalTrait = [pes, maos, asas, cauda, focinho, orelhas, boca]
pokemon142.hasDiverseTraits = []

# Snorlax

pokemon143 = onto.Pokemon("Snorlax")
pokemon143.hasType = [normal]
pokemon143.hasColor = [azul]
pokemon143.hasCategory = [normal]
pokemon143.hasPhysicalTrait = [pes, maos, orelhas, boca]
pokemon143.hasDiverseTraits = [evolucao, anda_de_dois]

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

# Salvar a ontologia em um arquivo RDF
onto.save("pokemon_ontology.owl", format="rdfxml")