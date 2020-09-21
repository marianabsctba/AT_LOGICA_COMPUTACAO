#Questão 03 do AT

TEXT_WARNING = "Seus gastos totais com {tipo} comprometem {atingido:.2f}% da sua renda total.\n" \
               "O máximo recomendado é de {recomendado_percent:.2f}%.\n" \
               "Portanto, idealmente, o máximo da sua renda comprometida com moradia deveria ser de R$" \
               "{recomendado_valor:.2f}."

TEXT_HEALTH = "Seus gastos totais com {tipo} comprometem {atingido:.2f}% de sua renda total.\n" \
              "O máximo recomendado é de {recomendado_percent:.2f}%.\n" \
              "Seus gastos estão dentro da margem recomendada."

FINANCIAL_RANGES = {
    'moradia': 30,
    'educacao': 20,
    'transporte': 15
}

FINANCIAL_LANG = {
    'moradia': "moradia",
    'educacao': "educação",
    'transporte': "transporte"
}


def lin():
    print("\033[1;34m=~\033[0;0m" * 40)


def menu():
    lin()
    print("\033[1;34m\nOlá, seja bem-vindo(a) ao HelpCheck, o seu simulador de orçamento!\n\033[0;0m")


def text():
    print("\033[1;35m===============\033[0;0m\033[1;34mDIAGNÓSTICO\033[0;0m\033[1;35m===============\033[0;0m")


def get_total():
    return float(input("Digite sua renda mensal total: "))


def diagnostico(total, values):
    for tipo in FINANCIAL_RANGES:
        percent = values[tipo] / total * 100
        lin()
        if percent > FINANCIAL_RANGES[tipo]:
            print(TEXT_WARNING.format(tipo=FINANCIAL_LANG[tipo],
                                      atingido=percent,
                                      recomendado_percent=FINANCIAL_RANGES[tipo],
                                      recomendado_valor=FINANCIAL_RANGES[tipo] / 100 * total))
        else:
            print(TEXT_HEALTH.format(tipo=FINANCIAL_LANG[tipo],
                                     atingido=percent,
                                     recomendado_percent=FINANCIAL_RANGES[tipo],
                                     recomendado_valor=FINANCIAL_RANGES[tipo] / 100 * total))


def get_values():
    values = {}
    for tipo in FINANCIAL_RANGES:
        values[tipo] = float(input(f"Digite seus gastos totais com {tipo}: "))
    return values


menu()
text()
diagnostico(get_total(), get_values())
lin()
print("\033[1;34m\nObrigado por usar HelpCheck! Volte sempre.\n\033[0;0m")
lin()
