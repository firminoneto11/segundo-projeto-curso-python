"""
Criar um campo de administrador (1)
    Neste campo ele pode adicionar um novo produto / editar / excluir

atributos - senha / login

menu de adm / apos login efetuado:
1 - Adicionar um novo produto
2 - Editar produto
3 - Excluir produto
4 - Alterar senha/login | done
5 - Voltar ao menu inicial | done
"""
from resetar_tela import clear_pycharm
import pickle as pck
from os.path import exists
from time import sleep


class Perfil:
    
    def __init__(self):
        self.__login = 'admin'
        self.__password = 'admin'
    
    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password


class Adm:

    @staticmethod
    def password_manager():
        file = r"..\database_files\adm.pickle"
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
        file = r"..\database_files\adm.pickle"
        with open(file, mode='wb') as fl:
            self.__login = new_value
            pck.dump(self, fl)

    @password.setter
    def password(self, new_value):
        file = r"..\database_files\adm.pickle"
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
        print("\n(1) - Adicionar um novo produto;"
              "\n(2) - Editar produto;"
              "\n(3) - Excluir produto;"
              "\n(4) - Trocar senha ou login;"
              "\n(5) - Voltar ao menu principal;")
        option = input("\nSelecione uma das opções acima: ")
        while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
            print("\nA opção escolhida é inválida!")
            option = input("Selecione uma das opções acima: ")

        if option == '5':
            input("\nPressione enter para voltar ao menu principal: ")
            break

        elif option == '4':
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

        elif option == '1':
            clear_pycharm()

        elif option == '2':
            pass

        else:
            pass


if __name__ == '__main__':
    menu_adm()
