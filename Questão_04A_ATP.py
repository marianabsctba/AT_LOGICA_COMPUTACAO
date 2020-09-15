
TEXT_OUTPUT = "Após {periodo} períodos(s), o montante será de R$"\
              "{valor_total:.2f}"


def get_valor_inicial():
    return float(input("Valor inicial: R$ "))


def get_rendimento():
    return float(input("Rendimento por período (%): "))


def get_aporte_periodo():
    return float(input("Aporte a cada período: R$ "))


def get_total_periodos():
    return int(input("Total de períodos: "))


def calculate(aporte, total, rendimento):
    return (total*(1+rendimento/100))+aporte


def run(step, max, aporte, total, rendimento):
    if step > max:
        return None

    valor_total = calculate(aporte, total, rendimento)
    print(TEXT_OUTPUT.format(valor_total=valor_total, periodo=step))

    return run(step+1, max, aporte, valor_total, rendimento)


valor_inicial = get_valor_inicial()
rendimento = get_rendimento()
aporte = get_aporte_periodo()
periodo = get_total_periodos()

run(1, periodo, aporte, valor_inicial, rendimento)
