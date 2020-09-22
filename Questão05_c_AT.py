#Questão 05c realizada de modo separado. Favor inserir os arquivos .py da questão 05 com o arquivo assessment_PIB.csv.

import matplotlib.pyplot as plt
import time

def dados_arquivo():
    arquivo = open('assessment_PIB.csv', 'r', encoding='utf-8')
    arquivo = arquivo.read()
    lista_paises = {}
    for linha in arquivo.splitlines():
        valores = linha.split(',')
        lista_paises[valores[0].lower().strip()] = valores[1:]
    return lista_paises


def digite_pais():
    print("\033[1;34m==\033[0;0m" * 30)
    pais_usuario = str(input("Digite um país para saber a evolução do PIB pelo tempo: ")).lower().strip()
    print("\033[1;34m==\033[0;0m" * 30)

    lista_paises = dados_arquivo()
    if pais_usuario not in lista_paises:
        print("\033[1;31mPaís inválido. Programa reiniciado.\033[0;0m")
        exit(1)
    if pais_usuario == "país":
        print("\033[1;31mPaís inválido. Programa reiniciado.\033[0;0m")
        exit(1)
    return pais_usuario


def grafico(x_axis, y_axis):
    plt.plot(x_axis, y_axis, color='blue', linewidth=2.5, linestyle="-")
    plt.xlabel('Anos', color='green')
    plt.ylabel('Valor em trilhões (US$)', color='red')
    plt.title('PIB', color='blue')
    plt.show()


def retorna_grafico():
    paises = dados_arquivo()
    pais_digitado = digite_pais()
    x_axis = list(range(2013, 2020 + 1))
    y_axis = [float(valor) for valor in paises[pais_digitado]]

    time.sleep(2)
    print(f"\033[1;34mAgora veja o gráfico com a evolução do PIB do país: {pais_digitado.upper()}, "
          f"de 2013 a 2020.\033[0;0m")
    time.sleep(3)
    grafico(x_axis, y_axis)


retorna_grafico()
