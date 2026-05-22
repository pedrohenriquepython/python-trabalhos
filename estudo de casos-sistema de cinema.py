filmes_em_cartaz = []
total_arrecadado = 0.0
total_ingressos_vendidos = 0

def cadastrar_filme(nome): 
    """Recebe o nome do filme por parâmetro e adiciona na lista."""
    filmes_em_cartaz.append(nome)
    print(f"\nFilme '{nome}' cadastrado com sucesso!")


def mostrar_filmes():
    """Usa loop 'for' para listar os filmes. Retorna False se estiver vazio."""
    if len(filmes_em_cartaz) == 0:
        print("\nNenhum filme em cartaz no momento.")
        return False
    
    print("\n--- Filmes em Cartaz ---")
    for i in range(len(filmes_em_cartaz)):
        print(f"{i + 1}. {filmes_em_cartaz[i]}")
    return True


def vender_ingresso(indice, valor):
    """Registra a venda se o índice for válido. Altera variáveis globais."""
    global total_arrecadado, total_ingressos_vendidos
    
    if 0 <= indice < len(filmes_em_cartaz):
        filme_escolhido = filmes_em_cartaz[indice]
        total_arrecadado += valor
        total_ingressos_vendidos += 1
        print(f"\nIngresso vendido com sucesso para o filme: {filme_escolhido}!")
        return True
    else:
        print("\nOpção de filme inválida. Venda cancelada.")
        return False


def calcular_arrecadacao():
    """Retorna o valor total arrecadado até o momento."""
    return total_arrecadado


def mostrar_total_ingressos():
    """Retorna a quantidade total de ingressos vendidos."""
    return total_ingressos_vendidos

while True:
    print("\n================ CINEMA ================")
    print("1. Cadastrar Filme")
    print("2. Mostrar Filmes em Cartaz")
    print("3. Vender Ingresso")
    print("4. Mostrar Relatório Geral")
    print("5. Sair")
    print("========================================")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == "1":
        nome_filme = input("Digite o nome do filme para cadastrar: ")
        cadastrar_filme(nome_filme)
        
    elif opcao == "2":
        mostrar_filmes()
        
    elif opcao == "3":
        if mostrar_filmes():
            try:
                escolha = int(input("\nEscolha o número do filme: ")) - 1
                preco = float(input("Digite o preço do ingresso (R$): "))
                vender_ingresso(escolha, preco)
            except ValueError:
                print("\nErro: Por favor, insira valores numéricos válidos para o filme e o preço.")
                
    elif opcao == "4":
        faturamento = calcular_arrecadacao()
        ingressos_total = mostrar_total_ingressos()
        
        print("\n====== RELATÓRIO DE VENDAS ======")
        print(f"Quantidade de ingressos vendidos: {ingressos_total}")
        print(f"Total arrecadado: R$ {faturamento:.2f}")
        print("=================================")
        
    elif opcao == "5":
        print("\nEncerrando o sistema do cinema. Boas sessões!")
        break
        
    else:
        print("\nOpção inválida. Escolha um número de 1 a 5.")