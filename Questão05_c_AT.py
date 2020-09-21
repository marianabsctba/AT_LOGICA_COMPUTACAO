mport matplotlib.pyplot as plt
import time


def dados_arquivo():
    arquivo = open('assessment_PIB.csv', 'r', encoding='utf-8')
    arquivo = arquivo.read()
    lista_paises = {}
    for linha in arquivo.splitlines():
        valores = linha.split(',')
        lista_paises[valores[0].lower().strip()] = valores[1:]
    return lista_paises


def digite_ano():
    ano_usuario = str(input("Digite um ano (entre 2013 e 2020): ")).strip()
    lista_paises = dados_arquivo()
    if ano_usuario not in lista_paises['país']:
        print("Ano inválido. Programa reiniciado.")
        exit(1)
    return ano_usuario


def digite_pais():
    pais_usuario = str(input("Digite um país: ")).lower().strip()
    lista_paises = dados_arquivo()
    if pais_usuario not in lista_paises:
        print("País inválido.")
        exit(1)
    if pais_usuario == "país":
        print("País inválido.Programa reiniciado.")
        exit(1)
    return pais_usuario


def grafico(x_axis, y_axis):
    plt.plot(x_axis, y_axis)
    plt.xlabel('Anos')
    plt.ylabel('Valor em trilhões (US$)')
    plt.title('PIB')
    plt.show()


def retorna_grafico():
    paises = dados_arquivo()
    pais_digitado = digite_pais()
    x_axis = list(range(2013, 2020 + 1))
    y_axis = [float(valor) for valor in paises[pais_digitado]]

    time.sleep(2)
    print(f"Agora veja o gráfico com a evolução do PIB do país {pais_digitado.upper()}, de 2013 a 2020.")
    time.sleep(3)
    grafico(x_axis, y_axis)



retorna_grafico()
