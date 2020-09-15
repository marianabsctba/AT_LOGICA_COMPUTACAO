def print_initial_data(name, salary, get_education, get_home, get_transport):
    print("\nOs dados digitados foram: \n")
    print("==" * 15)
    print(f"Nome:......................{name}")
    print(f"Salário (R$):..............{salary:.2f}")
    print(f"Custos com educação(R$):...{get_education:.2f}")
    print(f"Custos com moradia(R$:.....{get_home:.2f}")
    print(f"Custos com transporte(R$):.{get_transport:.2f}")
    print("==" * 15)


def data_dict(salary, get_home, get_education, get_transport):
    data = {"moradia": (get_home / salary) * 100,
            "educação": (get_education / salary) * 100,
            "transporte": (get_transport / salary) * 100}
    return data


def verify(data, salary, name):
    import time

    verification = {"moradia": 30, "educação": 20, "transporte": 15}

    print(f"\n{name}, aguarde. Estamos processando os seus dados...\n")
    time.sleep(2)
    print("*****====== DIAGNÓSTICO ======*****")

    for types, values_max in data.items():
        print(f"Os seus gastos totais com {str(types)} comprometem {values_max:.2f}% da sua renda.")
        print(f"O percentual máximo recomendado para {str(types)} é de {verification[types]:.2f}%.")
        print("~~" * 30)

        if values_max > verification[types]:
            print(f"Você ultrapassou o percentual recomendado.")
            print(f"O valor máximo que você pode destinar a {str(types)} "
                  f"é de R$ {verification[types] * salary:.2f}.")
            print("~~" * 30)

        else:
            print(f"Gastos com {str(types)} dentro do percentual recomendado. Fique tranquilo(a)!")
            print("~~" * 30)


print("==" * 30)
print("Olá, bem-vindo(a) ao HelpCheck, o seu simulador de orçamento!")
print("==" * 30)

name = str(input("\nDigite o seu nome: ")).upper().strip()
salary = float(input("Digite o seu salário/renda total: R$ "))
get_home = float(input("Agora, digite o valor que você gasta com aluguel/prestação de imóvel: R$ "))
get_education = float(input("Chegou o momento de inserir o valor que você gasta com escola/faculdade/outros: R$ "))
get_transport = float(input("Finalmente, digite o valor que você gasta com ônibus/metrô/outros: R$ "))

data = data_dict(salary, get_home, get_education, get_transport)
print_initial_data(name, salary, get_education, get_home, get_transport)
verify(data, salary, name)

print("Fim. Obrigado por usar Help Check! Volte sempre!")
print("==" * 30)

