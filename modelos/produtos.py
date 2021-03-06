
from csv import DictReader, DictWriter
from modelos.resetar_tela import clear_pycharm
from os.path import exists


class Counter:
    """
    Essa classe faz o registro do código dos produtos do sistema e os grava em um arquivo pickle, que codifica o conteú
    do de forma natural.
    """
    ID_COUNTER = r".\database_files\counting_id.pickle"
    COUNTER = None

    @classmethod
    def counting(cls):
        if exists(cls.ID_COUNTER) is False:
            with open(cls.ID_COUNTER, mode='w') as file:
                cls.COUNTER = 1
                file.write(str(cls.COUNTER))
                return cls.COUNTER
        else:
            with open(cls.ID_COUNTER, mode='r') as file:
                cls.COUNTER = int(file.read())
            with open(cls.ID_COUNTER, mode='w') as file:
                file.write(str(cls.COUNTER + 1))
                return int(cls.COUNTER + 1)


class Products:

    PRODUCTS_DATABASE = r".\database_files\products.csv"

    def __init__(self, nome, preco, desc):
        code = Counter.counting()
        self.__codigo = code

        self.__nome = nome
        self.__preco = preco
        self.__descricao = desc

    # Getters

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @property
    def descricao(self):
        return self.__descricao

    # Setters

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @preco.setter
    def preco(self, value):
        self.__preco = value

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    # Este método retorna valores booleanos para verificar a existência do registro de produtos
    @staticmethod
    def check_existance():
        db = Products.PRODUCTS_DATABASE
        if exists(db) is False:
            return False
        return True

    # Este método faz uma verificação do arquivo csv onde serão inseridos os produtos
    @classmethod
    def check_db(cls):
        """
        Faz uma verificação no arquivo csv onde serão inseridos os produtos
        :return: None
        """
        if exists(cls.PRODUCTS_DATABASE) is False:
            with open(cls.PRODUCTS_DATABASE, mode='w', encoding='utf-8', newline=None) as file:
                header = "Código", "Nome", "Preço/(R$)", "Descrição"
                writer = DictWriter(file, fieldnames=header)
                writer.writeheader()

    # Este método faz o registro do produto no arquivo csv
    def save_on_register(self):
        """
        Efetua o cadastro do novo produto no registro (aqruivo csv)
        :return: None
        """
        header = "Código", "Nome", "Preço/(R$)", "Descrição"
        with open(Products.PRODUCTS_DATABASE, mode='a', encoding='utf-8') as file:
            writer = DictWriter(file, fieldnames=header)
            writer.writerow({
                "Código": self.codigo,
                "Nome": self.nome,
                "Preço/(R$)": self.preco,
                "Descrição": self.descricao
            })

    # Este método faz a leitura do registro e conta a quantidade de elementos no mesmo
    @classmethod
    def read_register(cls):
        registro = cls.PRODUCTS_DATABASE
        contador = 0
        with open(registro, mode='r', encoding='utf-8', newline=None) as file:
            print("-------------------------------------------------------------------\n"
                  "              Código | Nome | Preço/(R$) | Descrição"
                  "\n-------------------------------------------------------------------")
            reader = DictReader(file)
            for product in reader:
                contador = contador + 1
                print(f"{product['Código']} | {product['Nome']} | R${product['Preço/(R$)']} | {product['Descrição']}")
        print(f"\nTotal de produtos cadastrados: {contador}")

    @classmethod
    def remove_product(cls, codigo):
        conteudo_antigo = []
        with open(cls.PRODUCTS_DATABASE, mode='r', encoding='utf-8', newline=None) as file:
            for line in file.readlines():
                conteudo_antigo.append(line)
        with open(cls.PRODUCTS_DATABASE, mode='w', encoding='utf-8', newline=None) as file:
            for line in conteudo_antigo:
                if line.startswith(codigo):
                    pass
                else:
                    file.write(line)

    @classmethod
    def codigos(cls):
        registro = cls.PRODUCTS_DATABASE
        codigos = []
        with open(registro, mode='r', encoding='utf-8', newline=None) as file:
            leitor = DictReader(file)
            for produto in leitor:
                codigos.append(produto['Código'])
        return codigos

    @classmethod
    def update(cls, code, v1, v2, v3):
        register = cls.PRODUCTS_DATABASE
        old_content = []
        with open(register, mode='r', encoding='utf-8', newline=None) as file:
            for line in file.readlines():
                old_content.append(line)
        with open(register, mode='w', encoding='utf-8', newline=None) as file:
            for line in old_content:
                if line.startswith(code):
                    file.write(f"{code},{v1},{v2},{v3}")
                else:
                    file.write(line)


# Cadastrar Produtos
def adicionar_produto():
    """
    Esta função realiza o processo do cadastro de um produto no sistema
    :return: None
    """
    # Checando o registro de dados
    Products.check_db()
    print("\nInsira o preço para o novo produto.")
    price = input("Preço: ")
    if ',' in price:
        price = price.replace(',', '.')
    try:
        float(price)
    except ValueError:
        return print("O valor atribuido para o preço é inválido! Tente novamente.")

    # Solicitando um nome para o novo produto
    clear_pycharm()
    print("\nInsira o nome para o novo produto.")
    name = input("Nome: ")

    # Solicitando uma descrição para o novo produto
    clear_pycharm()
    print("\nInsira a descrição do novo produto.")
    description = input("Descrição: ")

    # Instânciando o novo produto e salvando no registro
    clear_pycharm()
    new_product = Products(nome=name, preco=price, desc=description)
    new_product.save_on_register()
    print("\nProduto cadastrado com sucesso!")


# Editar produtos
def editar_produto(new_code):
    """
    Esta função realiza o processo de edição de um produto no sistema
    :return: None
    """
    clear_pycharm()
    # Solicitando um novo preço para o produto
    print("\nInsira o novo preço do produto.")
    new_price = input("Preço: ")
    if ',' in new_price:
        new_price = new_price.replace(',', '.')
    try:
        float(new_price)
    except ValueError:
        return print("O valor atribuido para o preço é inválido! Tente novamente.")

    # Solicitando um novo nome para o produto
    clear_pycharm()
    print("\nInsira o novo nome do produto.")
    new_name = input("Nome: ")

    # Solicitando uma nova descrição para o produto
    clear_pycharm()
    print("\nInsira a nova descrição do produto.")
    new_description = input("Descrição: ")

    # Aplicando a atualização/edição
    Products.update(code=new_code, v1=new_name, v2=new_price, v3=new_description)

    clear_pycharm()
    print("\nProduto atualizado com sucesso!")


if __name__ == '__main__':
    pass
