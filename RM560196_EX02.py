# Solução para cálculo das parcelas de compra de veículo

def calcula_parcelas(valor_carro):
    parcelas_acrescimo = {
        6: 3, 12: 6, 18: 9, 24: 12, 30: 15, 36: 18, 42: 21, 
        48: 24, 54: 27, 60: 30
    }
    
    preco_vista = valor_carro * 0.8
    print(f"O preço final à vista com desconto 20% é: R$ {preco_vista:.2f}")
    
    for parcelas, acrescimo in parcelas_acrescimo.items():
        preco_final = valor_carro * (1 + acrescimo / 100)
        valor_parcela = preco_final / parcelas
        print(f"O preço final parcelado em {parcelas}X é de R$ {preco_final:.2f} com parcelas de R$ {valor_parcela:.2f}")
        
# Executando a função
valor_carro = float(input("Digite o preço do carro: "))
calcula_parcelas(valor_carro)