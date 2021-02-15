"""
Criar um campo de administrador (1)
    Neste campo ele pode adicionar um novo produto / editar / excluir

atributos - senha / login

menu de adm / apos login efetuado:
1 - Adicionar um novo produto
2 - Editar produto
3 - Excluir produto
4 - Alterar senha/login
5 - Voltar ao menu inicial
"""
from resetar_tela import clear_pycharm
from time import sleep


class Adm:
    # Criar um txt para armazenar mudanças de senha

    def __init__(self):
        self.__password = "admin"
        self.__login = "admin"

    @property
    def password(self):
        return self.__password

    @property
    def login(self):
        return self.__login

    @password.setter
    def password(self, new_value):
        self.__password = new_value

    @login.setter
    def login(self, new_value):
        self.__login = new_value


def menu_adm():
    clear_pycharm()
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
              "\n(5) - Voltar ao menu inicial")
        option = input("\nSelecione uma das opções acima: ")
        while option != '1' and option != '2' and option != '3' and option != '4' and option != '5':
            print("\nA opção escolhida é inválida!")
            option = input("Selecione uma das opções acima: ")

        if option == '5':
            clear_pycharm()
            input("Pressione enter para voltar ao menu inicial: ")
            break

        elif option == '4':
            clear_pycharm()
            new_login = input("\nInsira o novo nome de usuário (login): ")
            new_password = input("Insira a nova senha: ")
            password_confirmation = input("Confirme a nova senha: ")
            if new_password != password_confirmation:
                input("As senhas nao conferem! Pressione enter para voltar ao menu principal: ")
                break
            else:
                adm.login = new_login
                adm.password = new_password
                input("\nLogin e senha atualizados com sucesso! Pressione enter para voltar ao menu do administrador: ")
                continue


if __name__ == '__main__':
    menu_adm()
