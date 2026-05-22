filmes_em_cartaz = ["Homem aranha", "Vingadores", "Batman"]
precos_filmes = [20.0, 30.0, 40.0]
total_arrecadado = 0.0
total_ingressos_vendidos = 0

def cadastrar_filme(nome, preco):
    filmes_em_cartaz.append(nome)
    precos_filmes.append(preco)
    print(f"\nFilme '{nome}' cadastrado com sucesso!")

def mostrar_filmes():
    if len(filmes_em_cartaz) == 0:
        print("\nNenhum filme em cartaz no momento.")
        return False
    
    print("\n--- Filmes em Cartaz ---")
    for i in range(len(filmes_em_cartaz)):
        print(f"{i + 1}. {filmes_em_cartaz[i]} - R$ {precos_filmes[i]:.2f}")
    return True

def vender_ingresso(indice):
    global total_arrecadado, total_ingressos_vendidos
    
    if 0 <= indice < len(filmes_em_cartaz):
        filme_escolhido = filmes_em_cartaz[indice]
        valor_ingresso = precos_filmes[indice]
        
        total_arrecadado += valor_ingresso
        total_ingressos_vendidos += 1
        
        print(f"\nIngresso vendido com sucesso para o filme: {filme_escolhido}!")
        print(f"Valor cobrado: R$ {valor_ingresso:.2f}")
        return True
    else:
        print("\nOpção de filme inválida. Venda cancelada.")
        return False

def calcular_arrecadacao():
    return total_arrecadado

def mostrar_total_ingressos():
    return total_ingressos_vendidos

while True:
    print("\n================ CINEMA ================")
    print("1. Cadastrar Novo Filme")
    print("2. Mostrar Filmes em Cartaz")
    print("3. Vender Ingresso")
    print("4. Mostrar Relatório Geral")
    print("5. Sair")
    print("========================================")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    if opcao == "1":
        nome_filme = input("Digite o nome do filme: ")
        try:
            preco_filme = float(input("Digite o preço do ingresso (R$): "))
            cadastrar_filme(nome_filme, preco_filme)
        except ValueError:
            print("\nErro: Digite um valor numérico válido para o preço.")
        
    elif opcao == "2":
        mostrar_filmes()
        
    elif opcao == "3":
        if mostrar_filmes():
            try:
                escolha = int(input("\nEscolha o número do filme: ")) - 1
                vender_ingresso(escolha)
            except ValueError:
                print("\nErro: Por favor, insira um número inteiro válido.")
                
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