import streamlit as st
from owlready2 import *

# Carregar a ontologia
onto = get_ontology("./pokemon_ontology.owl").load()

with onto:
    pokemons = onto.search(is_a = onto.Pokemon)

st.image('./img/whosthatpokemon.png')

st.image('./img/titulo.png')


st.header("Qual o tipo?")
tipo1 = st.selectbox("", [
    "", "Grama", "Fogo", "Água", "Inseto", "Normal", "Lutador", "Voador", "Venenoso",
    "Elétrico", "Solo", "Psíquico", "Rocha", "Fantasma", "Dragão", "Aço", "Gelo", "Fada"
], key=0)

st.header("Qual a cor dele?")
cor = st.selectbox("", [
    "", "Verde", "Laranja", "Azul", "Roxo", "Marrom", "Amarelo", "Rosa", "Vermelho",
    "Marrom claro", "Lilás", "Cinza", "Branco"
], key=2)

st.header("Qual a categoria?")
categoria = st.radio("", ["Não sei informar", "Normal", "Lendário", "Mítico"], key=3)

traits = {"Pés": "", "Mãos": "", "Asas": "", "Cauda": "", "Bico": "",
          "Focinho": "", "Orelhas": "", "Chifres": "", "Boca": ""}

st.header("Possui pés?")
traits["Pés"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=4)

st.header("Possui mãos?")
traits["Mãos"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=5)

st.header("Possui asas?")
traits["Asas"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=6)

st.header("Possui cauda?")
traits["Cauda"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=7)

st.header("Possui bico?")
traits["Bico"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=8)

st.header("Possui focinho?")
traits["Focinho"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=9)

st.header("Possui orelhas?")
traits["Orelhas"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=10)

st.header("Possui chifres?")
traits["Chifres"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=11)

st.header("Possui boca?")
traits["Boca"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=12)

diverse_traits = {"Evolução": "", "Redondo": "", "Anda de quatro": "", "Anda de dois": "",
                  "Parece objeto": "", "Cabeças": "", "Segura objeto": ""}

st.header("É uma evolução?")
diverse_traits["Evolução"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=13)

st.header("É redondo?")
diverse_traits["Redondo"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=14)

st.header("Anda sobre quatro patas?")
diverse_traits["Anda de quatro"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=15)

st.header("Anda sobre duas patas?")
diverse_traits["Anda de dois"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=16)

st.header("Parece um objeto?")
diverse_traits["Parece objeto"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=17)

st.header("Tem mais de uma cabeça?")
diverse_traits["Cabeças"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=18)

st.header("Segura alguma coisa?")
diverse_traits["Segura objeto"] = st.radio("", ["Não sei informar", "Sim", "Não"], key=19)

####### Filtragem ##########

pokemons_validos = []

for pokemon in pokemons:
    if(pokemon.name == "Pokemon"):
        continue

    if(tipo1 != ""):
        if len(pokemon.hasType) == 2:
            if pokemon.hasType[0].name != tipo1 and pokemon.hasType[1].name != tipo1:
                continue
        else:
            if pokemon.hasType[0].name != tipo1:
                continue
    
    if cor != "":
        poke_color = onto.search(is_a = pokemon.hasColor)[0]
        if poke_color.name != cor:
            continue
    
    if categoria != "Não sei informar":
        poke_category = onto.search(is_a = pokemon.hasCategory)[0]
        if poke_category.name != categoria:
            continue

    trait_flag = False
    for trait in traits.keys():
        if traits[trait] != "Não sei informar":
            has_trait = False
            for poke_trait in pokemon.hasPhysicalTrait:
                if poke_trait.name == trait:
                    has_trait = True
            if (not has_trait and traits[trait] == "Sim") or (has_trait and traits[trait] == "Não"):
                trait_flag = True
    
    diverse_trait_flag = False
    for trait in diverse_traits.keys():
        print(trait + " " + diverse_traits[trait])
        if diverse_traits[trait] != "Não sei informar":
            has_trait = False
            for poke_trait in pokemon.hasDiverseTraits:
                if poke_trait.name == trait:
                    has_trait = True
            if (not has_trait and diverse_traits[trait] == "Sim") or (has_trait and diverse_traits[trait] == "Não"):
                diverse_trait_flag = True
    
    if trait_flag or diverse_trait_flag:
        continue

    # Se possui todas as caracerísticas acima
    pokemons_validos.append(pokemon)


###############################################################################

st.sidebar.title("O pokémon que você procura pode estar aqui:")
cont = 0
for pokemon in pokemons_validos:
    if cont == 10:
        st.sidebar.write(f"(Mais {len(pokemons_validos) - 10} pokémons)")
        break
    st.sidebar.write("- " + pokemon.name)
    if len(pokemons_validos) < 5:
        st.sidebar.image(f'img/{pokemon.name}.gif')
    cont += 1