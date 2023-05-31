from flask_restful import Resource
from flask import request
from model.models import UsuarioModel

from webhook_token import TYPEFORM_SECRET_KEY


class ListUsuario(Resource):

    def get(self):

        usuarios = UsuarioModel.list_all()

        return {'usuarios': [usuario.to_dict() for usuario in usuarios]}, 200


class Usuario(Resource):

    def get(self, usuario_id):

        usuario = UsuarioModel.find_by_id(id=usuario_id).first()

        if usuario:
            return usuario.to_dict(), 200
        
        return {'message': 'Usuario not found.'}, 404


    def post(self):

        receivedSignature = request.headers.get("typeform-signature")
    
        if receivedSignature is None:
            return {'error': 'Permission denied.'}, 403
        
        
        if(receivedSignature != TYPEFORM_SECRET_KEY):
            return {'error': 'Invalid signature. Permission Denied.'}, 403
        
        questions = request.json['form']['questions']
        answers = request.json['answer']['answers']

        for ans in answers:
            ans_id = ans['q']

            for ques in questions:
                if ques['_id'] == ans_id:
                    if 'nome' in ques['question']:
                        nome  = ans['t']
                    if 'celular' in ques['question']:
                        numero = ans['t']
                    if 'Em qual' in ques['question']:
                        regiao = ans['c'][0]['t']


        usuario = UsuarioModel(nome=nome, regiao=regiao, numero=numero)
        usuario.save()

        return usuario.to_dict(), 201


    def delete(self, usuario_id):

        usuario = UsuarioModel.query.filter_by(id=usuario_id).first()

        if usuario:
            usuario.delete()
            return {'message': 'Usuario deleted.'}, 200
        
        return {'message': 'Usuario not found.'}, 404