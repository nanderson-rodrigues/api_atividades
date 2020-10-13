from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

#USUARIOS = {
#   'nanderson': '123',
#    'maria': '456'
#}
#@auth.verify_password
#def verification(login, senha):
#    if not (login, senha):
#        return False
#    return USUARIOS.get(login) == senha

@auth.verify_password
def verification(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):

    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'mesagem': 'Pessoa nao encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

    def delete(self, id):
        pessoa = Pessoas.query.filter_by(id=id).first()
        mensagem = "Pessoa {} excluida com sucesso".format(pessoa.nome)
        pessoa.delete()
        return {'status': 'Sucesso', 'mensagem': mensagem}

class ListaPessoas(Resource):

    @auth.login_required 
    def get(self):
        pessoas = Pessoas.query.all()
        response = [ {'id':i.id, 'nome': i.nome, 'idade': i.idade}  for i in pessoas]
        return response
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

class Atividade(Resource):
    def get(self, nome_pessoa):
        pessoa = Pessoas.query.filter_by(nome=nome_pessoa).first()
        print(pessoa)
        atividades = Atividades.query.filter_by(pessoa_id=pessoa.id)
        try :
            response = [{'pessoa': atividade.pessoa.nome, 'nome': atividade.nome, 'id': atividade.id, 'status': atividade.status}  for atividade in atividades]
        except Exception:
            response = {'status': 'Erro', 'mensagem': 'Erro ao tentar recuperar as atividades vinculadas a pessoa informada!'}

        return response

class AtividadeStatus(Resource):
    def get(self, id_atividade):
        atividade = Atividades.query.filter_by(id=id_atividade).first()
        try:
            response = {'status': atividade.status}
        except Exception:
            response = {'status': 'Erro', 'mensagem': 'Erro ao tentar recuperar status da atividade!'}
        return response

    def put(self, id_atividade):
        dados = request.json
        atividade = Atividades.query.filter_by(id=id_atividade).first()
        if 'status' in dados:
            atividade.status = dados['status']
        atividade.save()
        response = { 'status': atividade.status}

        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id' : i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome, "status": i.status} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']['nome']).first()
        atividade = Atividades(nome=dados["nome"], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id,
            'status': atividade.status
        }
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(Atividade, '/atividades/<string:nome>/')
api.add_resource(AtividadeStatus, '/atividades/<int:id_atividade>/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
