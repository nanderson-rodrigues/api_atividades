from models import Pessoas, Atividades, Usuarios

def insere_atividade(nome, status, pessoa_id):
    atividade = Atividades(nome=nome, status=status, pessoa_id=pessoa_id)
    print(atividade)
    atividade.save()

def consulta_atividades():
    atividades = Atividades.query.all()
    print(atividades)

def altera_atividade(nome, novo_nome, status, pessoa_id):
    pessoa = Pessoas.query.filter_by(id=pessoa_id)
    atividade = Atividades.query.filter_by(nome=nome).first()
    atividade.nome = novo_nome
    atividade.status = status
    atividade.pessoa_id = pessoa.id
    print(atividade)
    atividade.save()

def exclui_atividade(id):
    atividade = Atividades.query.filter_by(id=id).first()
    print(atividade)
    atividade.delete()

#-------------------

def insere_pessoa(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)

def altera_pessoa(nome, novo_nome, idade):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    pessoa.idade = idade
    pessoa.nome = novo_nome
    print(pessoa)
    pessoa.save()

def exclui_pessoa(nome):
    pessoa = Pessoas.query.filter_by(nome=nome).first()
    print(pessoa)
    pessoa.delete()

#------------------------

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    print(usuario)
    usuario.save()

def consulta_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)

if __name__ == '__main__':
    #insere_usuario('nanderson', '123')
    #insere_usuario('maria', '456')
    consulta_usuarios()

    #exclui_pessoa("Maheus")
    #insere_pessoa("Matheus", 15)
    #altera_pessoa()
    #consulta_pessoas()

    #exclui_atividade(1)
    #insere_atividade("Desenvolver o Back-end", "concluido", 3)
    #altera_atividade()
    #consulta_atividades()