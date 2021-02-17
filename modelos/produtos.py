"""
Na classe produtos, eles podem apenas ter os seguintes atributos:

Os métodos de CADASTRAR, EDITAR E EXCLUIR PRODUTO devem ser disponíveis apenas para administrador / Apenas atualizar o
registro de dados se for fornecida o login e senha do Administrador
"""
from csv import DictReader, DictWriter
from resetar_tela import clear_pycharm
from os.path import exists


class Products:

    PRODUCTS_DATABASE = r"..\database_files\products.csv"
    ID = None

    # Implementar a estrutura de código de produto
    @staticmethod
    def code_manager():
        if exists(Products.PRODUCTS_DATABASE) is False:
            Products.ID = 1
        else:
            with open(Products.PRODUCTS_DATABASE, mode='r', encoding='utf-8') as file:
                arquivo = DictReader(file)
                next(arquivo)
                pass

    def __init__(self, preco, nome, desc):
        self.__codigo = Products.ID + 1
        self.__preco = preco
        self.__nome = nome
        self.__descricao = desc
        Products.ID = self.__codigo + 1

    @property
    def preco(self):
        return self.__preco

    @property
    def nome(self):
        return self.__nome

    @property
    def descricao(self):
        return self.__descricao

    @property
    def codigo(self):
        return self.__codigo

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @preco.setter
    def preco(self, value):
        self.__preco = value

    @classmethod
    def check_db(cls):
        if exists(cls.PRODUCTS_DATABASE) is False:
            with open(cls.PRODUCTS_DATABASE, mode='w', encoding='utf-8') as file:
                header = "Código", "Nome", "Descrição", "Preço"
                writer = DictWriter(file, fieldnames=header)
                writer.writeheader()


def adicionar_produto():
    Products.check_db()
    print("\nInsira o preço para o novo produto.")
    price = input("Preço: ")
    if ',' in price:
        price = price.replace(',', '.')
    try:
        float(price)
    except ValueError:
        return "O valor atribuido para o preço é inválido! Tente novamente."

    clear_pycharm()
    print("\nInsira o nome para o novo produto.")
    name = input("Nome: ")

    clear_pycharm()
    print("\nInsira a descrição do novo produto.")
    description = input("Descrição: ")


if __name__ == '__main__':
    pass
