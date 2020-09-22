# Essa é a questão 04 do AT, contendo as letras A e B do enunciado.

import matplotlib.pyplot as plt
import time


def lin():
    print("\033[1;34m==\033[0;0m" * 30)


def menu():
    lin()
    print(f"\033[1;33mOlá, seja bem-vindo(a) ao YOURBANK, o seu simulador de riquezas!\033[0;0m")
    lin()


def dados_usuario():
    valor_inicial = float(input("Qual é o capital inicial:(R$) "))
    rendimento = float(input("Qual é o percentual de rendimento?(%) "))
    aporte = float(input("Qual é o aporte que será dado por período?(R$) "))
    periodos = int(input("Por quantos períodos a operação será realizada? "))

    valor_final_periodo = valor_inicial

    eixo_x = []
    eixo_y = []

    lin()
    print("\033[1;33m\nRelatório sobre a evolução do seu dinheiro:\n\033[0;0m")

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

    lin()
    print(f"\n\033[33mAgora, veja o gráfico com a evolução do seu dinheiro pelo período solicitado.\n\033[0;0m")
    print("\033[33mEstamos processando as suas informações. Por favor, aguarde...\n\033[0;0m")
    lin()
    time.sleep(3)
    plt.plot(x, y, color="green")
    plt.xlabel("Periodos (meses)", color="green")
    plt.ylabel("Valor (R$)", color="red")
    plt.title("Projeção dos Juros Compostos", color="blue")

    plt.show()


menu()
dados = dados_usuario()
criar_grafico(dados[0], dados[1])

print("\033[1;34mObrigado por usar YOURBANK. Volte sempre!\033[0;0m")
lin()

