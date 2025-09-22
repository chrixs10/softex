class Pessoa:
    def __init__(self, nome:str, idade:int):
        self.nome = nome
        self.idade = idade

    @property   ## me devolve o valor do atributo protegido 
    def nome(self):
        return self._nome

    @nome.setter ## modifica o valor protegido pelo @property
    def nome(self, novo_nome: str):
        if isinstance(novo_nome, str) and (novo_nome):
            self._nome = novo_nome
        else:
            print("Erro!! O nome deve ser uma string não vazia!")

    @property
    def idade (self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade:int):
        if isinstance(nova_idade, int) and nova_idade > 0:
            self._idade = nova_idade
        else:
            print("Erro! Nova idade deve ser um número positivo. ")

nova_pessoa = Pessoa("Christian", 22)
print(nova_pessoa.nome)

print(nova_pessoa.idade)
