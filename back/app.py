from flask import Flask, request
import sqlite3
from socket import gethostname

import hashlib
import hmac
import base64
import os

app = Flask(__name__)

DATABASE = '/home/eriksoaress/flood-alert-heliopolis-main/back/database/db_alert.db'


@app.route('/usuarios', methods=['GET'])
def get_usuarios():

    conn = sqlite3.connect(DATABASE, check_same_thread=False)

    cursor = conn.execute('SELECT * FROM usuarios')

    usuarios = []

    for linha in cursor:
        usuario = {
            'id': linha[0],
            'nome': linha[1],
            'regiao': linha[2],
            'numero': linha[3]
        }
        usuarios.append(usuario)

    conn.close()

    return {'usuarios': usuarios}, 200



@app.route('/usuarios', methods=['POST'])
def post_usuarios():
  
    receivedSignature = request.headers.get("typeform-signature")
    
    if receivedSignature is None:
      return {'error': 'Permission denied.'}, 403
      
    sha_name, signature = receivedSignature.split('=', 1)
    if sha_name != 'sha256':
      return {'error': 'Operation not supported.'}, 501
    
    is_valid = verifySignature(signature, request)
    
    if(is_valid != True):
      return {'error': 'Invalid signature. Permission Denied.'}, 403
    
    conn = sqlite3.connect(DATABASE, check_same_thread=False)

    questions = request.json['form_response']['definition']['fields']
    answers = request.json['form_response']['answers']

    for ans in answers:
       ans_id = ans['field']['id']

       for ques in questions:
          if ques['id'] == ans_id:
            if 'nome' in ques['title']:
               nome  = ans['text']
            if 'celular' in ques['title']:
               numero = ans['text']
            if 'região' in ques['title']:
               regiao = ans['choice']['label']


    conn.execute('INSERT INTO usuarios (nome, regiao, numero) VALUES (?, ?, ?)', (nome, regiao, numero))

    conn.commit()
    conn.close()

    return {'mensagem': 'Usuário cadastrado com sucesso!'}, 201
    
    
def verifySignature(receivedSignature: str, payload):
    WEBHOOK_SECRET = os.environ.get('TYPEFORM_SECRET_KEY')
    digest = hmac.new(WEBHOOK_SECRET.encode('utf-8'), payload, hashlib.sha256).digest()
    e = base64.b64encode(digest).decode()
    
    if(e == receivedSignature):
      return True
    return False



@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuarios(id):

    conn = sqlite3.connect(DATABASE, check_same_thread=False)

    conn.execute('DELETE FROM usuarios WHERE id = ?', (id,))

    conn.commit()
    conn.close()

    return {'mensagem': 'Usuário excluído com sucesso!'}, 200





if __name__ == '__main__':
    if 'liveconsole' not in gethostname():
        app.run()