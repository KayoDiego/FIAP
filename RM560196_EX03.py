# Solução para cálculo de empréstimo

def calcula_emprestimo(valor_divida, taxa_juros, num_parcelas):
    valor_final = valor_divida * (1 + taxa_juros / 100)
    valor_parcela = valor_final / num_parcelas
    print(f"Valor final da dívida: R$ {valor_final:.2f}")
    print(f"Valor da parcela em {num_parcelas}X: R$ {valor_parcela:.2f}")

# Executando a função
valor_divida = float(input("Informe o valor da dívida: "))
taxa_juros = float(input("Informe a taxa de juros (em %): "))
num_parcelas = int(input("Informe o número de parcelas: "))

calcula_emprestimo(valor_divida, taxa_juros, num_parcelas)