"""
Campo de compra (2)
    Neste campo o usuário pode visualizar(listar) os produtos disponiveis para compra, comprar um ou mais produtos sendo
não necessário ser do mesmo tipo e caso ele escolha duas vezes o mesmo produto, aumentar a quantidade no carrinho

Campo de Listagem(3)
    Neste campo o usuário pode ver todos os produtos que estão no carrinho e excluir algo que seja do interesse do mesmo
apresentar também o total da compra
"""
from modelos.resetar_tela import clear_pycharm
from modelos.administrador import menu_adm


def menu_principal():
    """
    Esta função é a função que gera o menu inicial da aplicação.
    :return: None
    """
    while True:
        clear_pycharm()
        print("------------------------------\n  Bem-vindo a ValWare Shop\n------------------------------")
        print("\n(1) - Entrar como administrador;"
              "\n(2) - Comprar um novo produto;"
              "\n(3) - Listar os produtos no carrinho;"
              "\n(4) - Sair da aplicação;")
        option = input("\nSelecione uma das opções acima: ")
        while option != '1' and option != '2' and option != '3' and option != '4':
            print("\nA opção escolhida é inválida!")
            option = input("Selecione uma das opções acima: ")

        if option == '4':
            clear_pycharm()
            print("\nMuito obrigado e até a próxima!")
            input("Pressione enter para finalizar o programa: ")
            break

        elif option == '3':
            continue

        elif option == '2':
            continue

        elif option == '1':
            clear_pycharm()
            menu_adm()


if __name__ == '__main__':
    menu_principal()
