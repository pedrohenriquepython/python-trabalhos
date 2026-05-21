# trabalho passado no teams, no dia 15 de maio de 2026
MENU_VHS = {
    "Carros 1": 150.0,
    "Toy Story 2": 20.0,
    "As Tranças do Careca": 300.0
}

carrinho = []

desconto_cadastrado = 0.0

def mostrar_menu():
    """Exibe as fitas VHS disponíveis e seus preços."""
    print("\n=================================")
    print("      CATÁLOGO DE FITAS VHS      ")
    print("=================================")
    for fita, preco in MENU_VHS.items():
        print(f" * {fita:<20} -> R$ {preco:.2f}")
    print("=================================")

def cadastrar_produto(nome_vhs, quantidade):
    """Adiciona uma fita e sua quantidade ao carrinho se ela existir no catálogo."""
    nome_formatado = nome_vhs.strip().title()
    
    if "Carros" in nome_formatado or "Carros 1" in nome_formatado:
        nome_formatado = "Carros 1"
    elif "Toy" in nome_formatado or "Toy Story" in nome_formatado:
        nome_formatado = "Toy Story 2"
    elif "Tranças" in nome_formatado or "Careca" in nome_formatado:
        nome_formatado = "As Tranças do Careca"

    if nome_formatado in MENU_VHS:
        preco_unitario = MENU_VHS[nome_formatado]
        
        item = {
            "produto": nome_formatado,
            "quantidade": quantidade,
            "preco_unitario": preco_unitario
        }
        carrinho.append(item)
        print(f"\n✅ {quantidade}x '{nome_formatado}' adicionada(s) ao carrinho!")
    else:
        print("\n❌ Erro: Esta fita VHS não existe no catálogo.")

def cadastrar_desconto(porcentagem):
    """Define e valida a porcentagem de desconto que será aplicada na venda."""
    global desconto_cadastrado
    if 0 <= porcentagem <= 100:
        desconto_cadastrado = porcentagem
        print(f"\n Desconto de {desconto_cadastrado}% cadastrado com sucesso!")
    else:
        print("\n Porcentagem inválida! Insira um valor entre 0 e 100.")

def calcular_total():
    """Calcula o subtotal, aplica o desconto cadastrado e mostra o resumo da venda."""
    if not carrinho:
        print("\n🛒 O carrinho está vazio. Adicione produtos antes de fechar a venda.")
        return

    subtotal = 0.0
    print("\n=================================")
    print("        RESUMO DA VENDA          ")
    print("=================================")
    
    for item in carrinho:
        total_item = item["quantidade"] * item["preco_unitario"]
        subtotal += total_item
        print()