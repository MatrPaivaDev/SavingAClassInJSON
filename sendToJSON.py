import json

CAMINHO_ARQUIVO = 'salvar_classe.json'

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# dados_p1 = {'nome': 'Matheus', 'idade': 26}

# p1 = Pessoa(**dados_p1)
p1 = Pessoa('Matheus', 26)
p2 = Pessoa('Maria Luiza', 24)
p3 = Pessoa('Ione', 70)

pessoas = [p1.__dict__, p2.__dict__, p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as file:
        json.dump(
            pessoas,
            file,
            indent= 2,
            ensure_ascii= False
        )

# restringe a execução dessa função somente a esse arquivo. 
if __name__ == '__main__':
    fazer_dump()
    print('eu sou o ', __name__)