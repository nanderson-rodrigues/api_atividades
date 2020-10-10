from models import Pessoas, Atividades


def insere_pessoas():
    pessoa = Pessoas(nome="Nanderson", idade=23)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Rafael").first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Nanderson').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoas()
    altera_pessoa()
    consulta_pessoas()