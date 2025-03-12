import streamlit as st
import random

# Liste di parole
prima_lista = [
    "Dio", "Gesù", "Creatore", "Signore"]

seconda_lista = [
    "Cane puzzolente", "Gatto che miagola e muore di fame", "Porco", 
    "Maiale ricoperto di merda", "Rana depressa", "Ippopotamo da salotto", 
    "Gallina impazzita", "Cervo con l'ansia sociale", "Pinguino scocciato", 
    "Orso che ha perso il senso della vita", "Scoiattolo iperattivo", 
    "Mucca filosofa", "Polpo impiccione", "Lupo romantico e deluso", 
    "Tasso misantropo", "Ghiro con l'insonnia", "Cavallo bipolare", 
    "Serpente che fa lo psicologo", "Piccione comunista", 
    "Cane da guardia con la crisi esistenziale", "Cammello sovrappeso", 
    "Pappagallo che insulta", "Panda con il mutuo da pagare", 
    "Formica ribelle", "Koala pigro cronico", "Gabbiano cleptomane", 
    "Scimmia hacker", "Delfino sarcastico", "Cinghiale da centro commerciale", 
    "Topo con la personalità multipla", "Riccio da combattimento", 
    "Tartaruga punk", "Fenicottero con il complesso d'inferiorità", 
    "Gufo che giudica", "Anatra sociopatica", "Pesce rosso smemorato e triste", 
    "Mosca da ufficio", "Criceto imprenditore fallito", "Elefante ansioso", 
    "Cobra motivatore", "Geco con un podcast", "Granchio passivo-aggressivo", 
    "Scoiattolo truffatore", "Pavone narcisista", "Capra complottista", 
    "Pollo vegano", "Zebra confusa", "Ghiro che odia il lunedì", 
    "Talpa che non crede nella luce", "Ratto filosofo di strada", 
    "Scorfano pessimista", "Cinghiale poeta maledetto", 
    "Ornitorinco esistenzialista", "Alce da meditazione", 
    "Gatto che si sente influencer", "Corvo avvocato del diavolo"
]

# Titolo della web app
st.title("Generatore di Frasi")

# Bottone per generare la frase
if st.button("Genera Frase"):
    parola1 = random.choice(prima_lista)
    parola2 = random.choice(seconda_lista)
    frase = f"{parola1} {parola2}"
    st.success(f"✨ {frase} ✨")
