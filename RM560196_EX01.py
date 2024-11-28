# Solução para a votação dos dias da semana

def votacao_dias(colaboradores):
    dias = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira']
    votos = {dia: 0 for dia in dias}

    for i in range(colaboradores):
        voto = input(f"Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").strip().lower()
        if voto in votos:
            votos[voto] += 1
        else:
            print("Dia inválido, tente novamente.")
            i -= 1
    
    max_votos = max(votos.values())
    dias_vencedores = [dia for dia, count in votos.items() if count == max_votos]

    if len(dias_vencedores) > 1:
        print("Há um empate entre os dias:", ', '.join(dias_vencedores))
    else:
        print(f"O dia escolhido pelos colaboradores é: {dias_vencedores[0]}")
    
# Executando a função
colaboradores = int(input("Informe o número de colaboradores: "))
votacao_dias(colaboradores)