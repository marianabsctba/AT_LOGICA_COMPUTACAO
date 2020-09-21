#Questão 04 a e b, versão 02. Por favor, insira este arquivo cna mesma pasta do arquivo home.html.

from flask import Flask, render_template, request
import json

app = Flask(__name__)

TEXT_OUTPUT = "Após {periodo} períodos(s), o montante será de R$" \
              "{valor_total:.2f}"


def get_valor_inicial():
    return float(input("Qual é o valor inicial?(R$) "))


def get_rendimento():
    return float(input("Qual é o rendimento por período?(%) "))


def get_aporte_periodo():
    return float(input("Qual é o aporte a cada período?(R$)"))


def get_total_periodos():
    return int(input("Qual é o total de períodos? "))


def calculate(aporte, total, rendimento):
    return (total * (1 + rendimento / 100)) + aporte


@app.route('/', methods=['POST'])
def posted_data():
    valor_total = float(request.values.get('valor_inicial', 0))
    rendimento = float(request.values.get('rendimento', 0))
    aporte = float(request.values.get('aporte', 0))
    periodo = int(request.values.get('periodo', 0))

    money_data = []
    for i in range(0, periodo):
        total = calculate(aporte, valor_total, rendimento)
        money_data.append(float('{:.2f}'.format(total)))
        valor_total = total

    return render_template('home.html', money_data=json.dumps(money_data))


@app.route('/', methods=['GET'])
def home():
    money_data = [0, 0, 0, 0, 0, 0, 0, 0]
    return render_template('home.html', money_data=json.dumps(money_data))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
