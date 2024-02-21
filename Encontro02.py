import requests
from bs4 import BeautifulSoup
# import pandas as pd

def acessar_pagina(link):
    """responsável por acessar as páginas da internet"""
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs

def extrair_infos():
    """responsável por extrair as informações das páginas"""
    link = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa"
    pagina = acessar_pagina(link)
    titulo_geral = pagina.h2
    print(titulo_geral)

def main(): 
    coletar_dados = extrair_infos()

if __name__ == "__main__":
    main()