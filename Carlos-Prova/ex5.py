def criar_produto(nome,codigo,preco,estoque):
    produto = ( nome , codigo , preco, estoque)
    return produto

def atualizar_estoque(produto, quantidade):
    estoque_atualizado = (produto[0],produto[1],produto[2],(produto[3] + quantidade))
    return estoque_atualizado

def listar_produtos(lista_produtos):
    for produto in lista_produtos:
        print(produto)

encerrar = False
lista_produtos = []
while encerrar != True:
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        lista_produtos.append(criar_produto(input("Digite o nome do produto: "), int(input("digite o codigo do produto: "), float(input("Digite o preço do produto: "), int(input("Digite o estoque disponivel: "))))))
    elif opcao == 2:
        x = int(input("digite o numero do produto na lista que sera atualizado: "))
        lista_produtos[x] = atualizar_estoque(x,int(input("Digite a quantidade a ser adicionada: ")))
    elif opcao == 3:
        listar_produtos(lista_produtos)
    else:
        encerrar = True