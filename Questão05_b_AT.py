
#Essa é a segunda versão da Questão 05b, mas feita separadamente e que mostra a evolução do PIB de todos os países.

def dados_arquivo():
    arquivo = open('assessment_PIB.csv', 'r', encoding='utf-8')
    arquivo = arquivo.read()
    lista_paises = {}
    for linha in arquivo.splitlines():
        valores = linha.split(',')
        lista_paises[valores[0].strip()] = valores[1:]
    return lista_paises


def get_variacao():
    lista_paises = dados_arquivo()
    lista_paises.pop('País')
    for pais in lista_paises:
        variacao = ((float(lista_paises[pais][-1]) / float(lista_paises[pais][0])) - 1) * 100
        print(f"A variação do PIB do {pais} entre 2013 a 2020 é de US$ {variacao:.2f} trilhões.")


print("\033[1;34m\nAgora veja a variação do PIB por países: \n\033[0;0m")
print("\033[1;34m==\033[0;0m" * 40)
get_variacao()
print("\033[1;34m==\033[0;0m" * 40)
