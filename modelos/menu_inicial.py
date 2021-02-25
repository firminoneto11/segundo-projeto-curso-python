
from modelos.resetar_tela import clear_pycharm
from modelos.administrador import menu_adm
from modelos.clientes import comprar_produto, visualizar_carrinho, CARRINHO, fechar_pedido
from modelos.produtos import Products


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
              "\n(3) - Listar os produtos do carrinho;"
              "\n(4) - Fechar pedido;"
              "\n(5) - Sair da aplicação;")
        option = input("\nSelecione uma das opções acima: ")
        while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
            print("\nA opção escolhida é inválida!")
            option = input("Selecione uma das opções acima: ")

        # Option == '5' / Sair
        if option == '5':
            clear_pycharm()
            print("\nMuito obrigado e até a próxima!")
            input("Pressione enter para finalizar o programa: ")
            break

        # Option == '4' / Fechar pedido
        elif option == '4':
            clear_pycharm()
            if len(CARRINHO) > 0:
                fechar_pedido()
                input("\nPressione enter para voltar ao menu inicial: ")
            else:
                print("\nAinda não foram adicionados produtos ao carrinho. Vá comprar um pouco!")
                input("Pressione enter para voltar ao menu inicial: ")

        # Option == '3' / Listar produtos do carrinho
        elif option == '3':
            clear_pycharm()
            if Products.check_existance is False:
                print("\nNão existem produtos cadastrados no momento!")
                input("Pressione enter para voltar ao menu inicial: ")
            else:
                if len(CARRINHO) > 0:
                    visualizar_carrinho()
                    input("\nPressione enter para voltar ao menu inicial: ")
                else:
                    print("\nAinda não foram adicionados produtos ao carrinho. Vá comprar um pouco!")
                    input("Pressione enter para voltar ao menu inicial: ")

        # Option == '2' / Comprar um novo produto
        elif option == '2':
            clear_pycharm()
            if Products.check_existance() is False:
                print("\nNão existem produtos cadastrados no momento!")
            else:
                comprar_produto()
            input("\nPressione enter para voltar ao menu inicial: ")

        # Option == '1' / Entrar como administrador
        else:
            clear_pycharm()
            menu_adm()


if __name__ == '__main__':
    menu_principal()
