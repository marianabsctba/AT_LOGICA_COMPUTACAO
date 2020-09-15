#Questão 01 AT

TEXT_WARNING = "Seus gastos totais com {tipo} comprometem {atingido:.2f}% desua renda total. " \
               "O máximo recomendado é de {recomendado_percent:.2f}%. " \
               "Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$" \
               "{recomendado_valor:.2f}."

TEXT_HEALTH = "Seus gastos totais com {tipo} comprometem {atingido:.2f}% de sua renda total. " \
              "O máximo recomendado é de {recomendado_percent:.2f}%. " \
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


def get_total():
    return float(input("Renda mensal total: "))


def diagnostico(total, values):
    for tipo in FINANCIAL_RANGES:
        percent = values[tipo]/total*100
        if percent > FINANCIAL_RANGES[tipo]:
            print(TEXT_WARNING.format(tipo=FINANCIAL_LANG[tipo],
                  atingido=percent,
                  recomendado_percent=FINANCIAL_RANGES[tipo],
                  recomendado_valor=FINANCIAL_RANGES[tipo]/100*total))
        else:
            print(TEXT_HEALTH.format(tipo=FINANCIAL_LANG[tipo],
                  atingido=percent,
                  recomendado_percent=FINANCIAL_RANGES[tipo],
                  recomendado_valor=FINANCIAL_RANGES[tipo]/100*total))


def get_values():
    values = {}
    for tipo in FINANCIAL_RANGES:
        values[tipo] = float(input(f"Gastos totais com {tipo}: "))
    return values


diagnostico(get_total(), get_values())
