import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col = 0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data




st.markdown("# FIFA23 OFFICIAL DATASET ⚽")
st.sidebar.markdown("Desenvolvido por [Geovani Lima Cardoso](https://www.linkedin.com/in/geovani-lima-cardoso-760212158/)")

btn = st.button("Acesse os dados no kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
"""
O FIFA, uma das franquias mais icônicas de videogames esportivos, não se limita apenas à diversão nos consoles, mas também se estende ao fascinante universo dos dados e estatísticas no Kaggle. Com conjuntos de dados abrangentes disponíveis na plataforma, os entusiastas do futebol e cientistas de dados têm a oportunidade de mergulhar profundamente nas complexidades do esporte virtual.

Para os amantes de ligas específicas, conjuntos de dados focados em ligas de futebol específicas também estão disponíveis. Esses conjuntos incluem informações sobre clubes, **jogadores e estatísticas de desempenho ao longo das temporadas, proporcionando uma visão holística do cenário futebolístico virtual.**

Os dados do FIFA no Kaggle não se limitam apenas aos aspectos técnicos do jogo. Também há conjuntos que exploram elementos como avaliações de equipes, popularidade de jogadores e até mesmo análises de mercado de transferências virtuais. Essas informações oferecem uma compreensão mais profunda de como as decisões dos jogadores e as dinâmicas do mercado de transferências influenciam a experiência de jogo.

Em resumo, o mundo dos dados relacionados ao FIFA no Kaggle é vasto e diversificado. Desde análises técnicas dos atributos dos jogadores até investigações sobre o desempenho durante eventos específicos, os conjuntos de dados disponíveis proporcionam uma riqueza de informações para os apaixonados pelo futebol virtual. Ao explorar esses dados, os entusiastas têm a oportunidade de unir a paixão pelo esporte com a curiosidade científica, descobrindo os segredos por trás do sucesso no mundo do FIFA.
"""
)