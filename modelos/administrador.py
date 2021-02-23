"""
Campo de Administrador totalmente funcional!
"""
from modelos.resetar_tela import clear_pycharm
import pickle as pck
from os.path import exists
from time import sleep
from modelos.produtos import adicionar_produto
from modelos.profile import Perfil
from modelos.produtos import Products
from modelos.produtos import editar_produto


class Adm:

    @staticmethod
    def password_manager():
        file = r".\database_files\adm.pickle"
        if exists(file) is False:
            with open(file, mode='wb') as fl:
                ad = Perfil()
                ad_ = ad.login, ad.password
                pck.dump(ad, fl)
                return ad_
        else:
            with open(file, mode='rb') as fl:
                ad = pck.load(fl)
                ad_ = ad.login, ad.password
                return ad_

    def __init__(self):
        init = Adm.password_manager()
        self.__login = init[0]
        self.__password = init[1]

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self, new_value):
        file = r".\database_files\adm.pickle"
        with open(file, mode='wb') as fl:
            self.__login = new_value
            pck.dump(self, fl)

    @password.setter
    def password(self, new_value):
        file = r".\database_files\adm.pickle"
        with open(file, mode='wb') as fl:
            self.__password = new_value
            pck.dump(self, fl)


def menu_adm():
    adm = Adm()
    print("\nPara continuar, Insira o login e senha do perfil de administrador.")
    log = input("Login: ")
    pas = input("Senha: ")
    sleep(1)
    if log != adm.login or pas != adm.password:
        input("\nLogin ou senha incorretos! Pressione enter para voltar ao menu principal: ")
        return None

    while True:
        clear_pycharm()
        print("------------------------------\n  Administrador\n------------------------------")
        print("\n(1) - Listar produtos;"
              "\n(2) - Adicionar um novo produto;"
              "\n(3) - Editar produto;"
              "\n(4) - Excluir produto;"
              "\n(5) - Trocar senha e login;"
              "\n(6) - Voltar ao menu principal;")
        option = input("\nSelecione uma das opções acima: ")
        while option != '1' and option != '2' and option != '3' and option != '4' and option != '5' and option != '6':
            print("\nA opção escolhida é inválida!")
            option = input("Selecione uma das opções acima: ")

        # Option == 6
        if option == '6':
            input("\nPressione enter para voltar ao menu principal: ")
            break

        # Option == 5
        elif option == '5':
            clear_pycharm()
            new_login = input("\nInsira o novo nome de usuário (login): ")
            new_password = input("Insira a nova senha: ")
            password_confirmation = input("Confirme a nova senha: ")
            sleep(1)
            if new_password != password_confirmation:
                input("\nAs senhas nao conferem! Pressione enter para voltar ao menu principal: ")
                break
            else:
                adm.login = new_login
                adm.password = new_password
                input("\nLogin e senha atualizados com sucesso! Pressione enter para voltar ao menu do administrador: ")
                continue

        # Option == 4
        elif option == '4':
            clear_pycharm()
            if Products.check_existance() is False:
                print("\nNão há produtos cadastrados!")
                input("Pressione enter para voltar ao menu do administrador: ")
                continue
            Products.read_register()
            print("\nQual dos produtos gostaria de remover?")
            escolha = input("Insira um código de um produto acima ou qualquer outro valor para cancelar a remoção: ")
            if escolha in Products.codigos():
                print("\nConfirme sua senha e login para continuar.")
                login = input("Login: ")
                senha = input("Senha: ")
                if login != adm.login or senha != adm.password:
                    sleep(1)
                    clear_pycharm()
                    input("\nLogin ou senha incorretos! Pressione enter para voltar ao menu do administrador: ")
                    continue
                else:
                    sleep(1)
                    clear_pycharm()
                    Products.remove_product(escolha)
                    print(f"Produto de código {escolha} removido com sucesso!")
                    input("\nPressione enter para voltar ao menu do administrador: ")
            else:
                input("\nPressione enter para voltar ao menu do administrador: ")

        # Option == 3
        elif option == '3':
            clear_pycharm()
            if Products.check_existance() is False:
                print("\nNão há produtos cadastrados!")
                input("Pressione enter para voltar ao menu do administrador: ")
                continue
            else:
                Products.read_register()
                print("\nQual dos produtos acima gostaria de editar?")
                code = input(
                    "Insira o código de um dos elementos acima ou qualquer outro valor para voltar ao menu de administr"
                    "ador: ")
                if code in Products.codigos():
                    editar_produto(code)
                    input("\nPressione enter para voltar ao menu do administrador: ")
                    continue
                else:
                    input("\nPressione enter para voltar ao menu do administrador: ")
                    continue

        # Option == 2
        elif option == '2':
            clear_pycharm()
            adicionar_produto()
            input("\nPressione enter para voltar ao menu do administrador: ")
            continue

        # Option == 1
        else:
            clear_pycharm()
            if Products.check_existance() is False:
                print("\nNão há produtos cadastrados!")
                input("Pressione enter para voltar ao menu do administrador: ")
                continue
            else:
                Products.read_register()
                input("\nPressione enter para voltar ao menu de administrador: ")
                continue


if __name__ == '__main__':
    menu_adm()
