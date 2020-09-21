#Questão 05 A realizada separadamente. Por favor, insira os arquivos da Questão 05 na mesma pasta do arquivo assessment_PIB.csv.

import matplotlib.pyplot as plt


def dados_arquivo():
    arquivo = open('assessment_PIB.csv', 'r', encoding='utf-8')
    arquivo = arquivo.read()
    lista_paises = {}
    for linha in arquivo.splitlines():
        valores = linha.split(',')
        lista_paises[valores[0].lower().strip()] = valores[1:]
    return lista_paises


def lin():
    print("\033[1;34m==\033[0;0m" * 40)


def menu():
    lin()
    print("\033[1;33m\nOlá, seja bem-vindo(a) ao WorldPIB. "
          "Você poderá checar o PIB de alguns países do mundo. Vamos lá?\n\033[0;0m")
    lin()


def digite_ano():
    ano_usuario = str(input("Digite um ano (entre 2013 e 2020): ")).strip()
    lista_paises = dados_arquivo()
    if ano_usuario not in lista_paises['país']:
        print("\033[1;31mAno inválido. Programa reiniciado.\033[0;0m")
        exit(1)
    return ano_usuario


def digite_pais():
    pais_usuario = str(input("Digite um país: ")).lower().strip()
    lista_paises = dados_arquivo()
    if pais_usuario not in lista_paises:
        lin()
        print("\033[1;31mPaís inválido. Programa reiniciado.\033[0;0m")
        lin()
        exit(1)
    if pais_usuario == "país":
        lin()
        print("\033[1;31mPaís inválido.Programa reiniciado.\033[0;0m")
        lin()
        exit(1)
    return pais_usuario


def get_variacao(paises, pais_digitado):
    return ((float(paises[pais_digitado][-1]) / float(paises[pais_digitado][0])) - 1) * 100


def retorna_pib():
    paises = dados_arquivo()
    ano_digitado = digite_ano()
    pais_digitado = digite_pais()

    index = int(ano_digitado) - 2013
    pib_pais = paises[pais_digitado][index]
    lin()
    print(f"O PIB do {pais_digitado.upper()} em {ano_digitado} é US$ {pib_pais} trilhões.")
    lin()


menu()
retorna_pib()
