
from modelos.produtos import Products
from csv import DictReader
from modelos.resetar_tela import clear_pycharm
from time import sleep

CARRINHO = []


def escolhe_produto(choice):
    """
    Esta função recebe o parâmetro choice que é o código referente a algum produto escolhido pelo usuário e o adiciona
    no carrinho. Se o mesmo já estiver no carrinho, a função altera a quantidade, caso contrário, adiciona o produto.
    :param choice: Código escolhido pelo usuário.
    :return: Confirmação de adição no carrinho do produto escolhido por meio do parâmetro choice.
    """
    global CARRINHO
    db = Products.PRODUCTS_DATABASE
    with open(db, mode='r', encoding='utf-8', newline=None) as file:
        arquivo = DictReader(file)
        for produto in arquivo:
            if produto['Código'] == choice:
                if len(CARRINHO) > 0:
                    codigos = []
                    for lista in CARRINHO:
                        if choice == lista[0]:
                            old_qtd = lista[3]
                            lista.pop()
                            lista.append(old_qtd + 1)
                        codigos.append(lista[0])
                    if choice not in codigos:
                        CARRINHO.append([produto['Código'], produto['Nome'], float(produto['Preço/(R$)']), 1])
                else:
                    CARRINHO.append([produto['Código'], produto['Nome'], float(produto['Preço/(R$)']), 1])
                clear_pycharm()
                return f"\nO(a) produto {produto['Nome']} foi adicionado ao carrinho com sucesso!"
            else:
                pass


def visualizar_carrinho():
    """
    Esta função acessa a variável global que é uma lista chamada CARRINHO, apresenta na tela os preços dos produtos esco
    lhidos e retorna o valor total das compras.
    :return: Total (somatório) dos elementos no CARRINHO.
    """
    global CARRINHO
    total = []
    print("---------------------------------------\n            Carrinho\n---------------------------------------\n")
    for lista in CARRINHO:
        print(f"Nome do produto: {lista[1]} | Quantidade: {lista[3]} | Preço unitário: R${lista[2]}")
        total.append(lista[2] * lista[3])
    print("\n----------------------------------------")
    return print(f"Total: R${round(sum(total), 2)}")


def comprar_produto():
    """
    Esta função inicializa o procedimento de adição de produtos no carrinho. Se o código informado pelo usuário for
    inválido, ela retorna o valor 'None', senão, ela seleciona o produto do registro referente ao código informado e re
    torna a execução da função escolhe_produto.
    :return: None ou escolhe_produto()
    """
    Products.read_register()
    escolha = input("Insira um código de um produto acima ou qualquer outro valor para voltar ao menu inicial: ")
    if escolha not in Products.codigos():
        return None
    else:
        return print(escolhe_produto(escolha))


def fechar_pedido():
    """
    Esta função realiza o processo de finalização do pedido do cliente e após a devida confirmação, faz a limpeza da lis
    ta 'CARRINHO' e retorna a confirmação da compra.
    :return: Confirmação da compra ou None se não finalizada.
    """
    global CARRINHO
    total = []
    print("\n-------------")
    print("Fechar pedido")
    print("-------------\n")
    for lista in CARRINHO:
        print(f"Nome do produto: {lista[1]} | Quantidade: {lista[3]} | Preço unitário: R${lista[2]}")
        total.append(lista[2] * lista[3])
    valor_total = round(sum(total), 2)
    print(f"\nO valor total da compra é de R${valor_total}. Gostaria de finalizar o pedido?")
    option = input("Digite (s) para SIM e (n) para NÃO: ")
    print('')
    while option != 's' and option != 'n':
        option = input("Valor inválido! Digite (s) para SIM e (n) para NÃO: ")
    if option == 's':
        clear_pycharm()
        print("\nDigite 'CONFIRMAR' para finalizar o pedido.")
        confirmar = input("-> ").upper()
        sleep(2)
        if confirmar != 'CONFIRMAR':
            return print("\nOpção inserida inválida.")
        else:
            CARRINHO.clear()
            return print(f"\nCompra no valor de R${valor_total} efetuada com sucesso!")
    else:
        return None
