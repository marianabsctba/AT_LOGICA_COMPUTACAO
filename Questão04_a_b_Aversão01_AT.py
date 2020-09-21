import matplotlib.pyplot as plt
import time


def dados_usuario():
    valor_inicial = float(input("Qual é o capital inicial: R$ "))
    rendimento = float(input("Qual é o percentual de rendimento? "))
    aporte = float(input("Qual é o aporte que será dado por período? "))
    periodos = int(input("Por quantos períodos a operação será realizada? "))

    valor_final_periodo = valor_inicial

    eixo_x = []
    eixo_y = []
    for periodo in range(1, periodos + 1):
        valor_inicio_periodo = valor_final_periodo
        aporte_periodo = aporte

        rendimento_periodo = valor_inicio_periodo * rendimento / 100
        valor_final_periodo = valor_inicio_periodo + rendimento_periodo + aporte_periodo

        eixo_x.append(periodo)
        eixo_y.append(valor_final_periodo)
        print(f"Após {periodo} períodos(s), o montante será de R$ {round(valor_final_periodo, 2)}.")


    return [eixo_x, eixo_y]


def criar_grafico(x, y):
    time.sleep(2)
    print("\nAgora, veja o gráfico com a evolução do seu dinheiro pelo período solicitado.\n")
    print("Processando suas informações. Aguarde...")
    time.sleep(3)
    plt.plot(x, y)
    plt.xlabel('Periodos (meses)')
    plt.ylabel('Valor (R$)')
    plt.title('Projeção dos Juros Compostos')

    plt.show()


dados = dados_usuario()
criar_grafico(dados[0], dados[1])
