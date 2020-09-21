import matplotlib.pyplot as plt

#Questão 05 A realizada separadamente. Por favor, insira os arquivos da Questão 05 na mesma pasta do arquivo assessment_PIB.csv.


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


def get_variacao(paises, pais_digitado):
    return ((float(paises[pais_digitado][-1]) / float(paises[pais_digitado][0])) - 1) * 100


def grafico(x_axis, y_axis):
    plt.plot(x_axis, y_axis)
    plt.xlabel('Anos')
    plt.ylabel('Valor em trilhões (US$)')
    plt.title('PIB')
    plt.show()


def retorna_pib():
    paises = dados_arquivo()
    ano_digitado = digite_ano()
    pais_digitado = digite_pais()

    index = int(ano_digitado) - 2013
    pib_pais = paises[pais_digitado][index]
    print(f"O PIB do {pais_digitado.upper()} em {ano_digitado} é US$ {pib_pais} trilhões.")

retorna_pib()
