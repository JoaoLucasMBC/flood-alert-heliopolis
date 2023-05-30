from flask import Flask, request
import sqlite3
from socket import gethostname

app = Flask(__name__)

TYPEFORM_SECRET_KEY='123'
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
    
    
    if(receivedSignature != TYPEFORM_SECRET_KEY):
     return {'error': 'Invalid signature. Permission Denied.'}, 403
    
    conn = sqlite3.connect(DATABASE, check_same_thread=False)

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


    conn.execute('INSERT INTO usuarios (nome, regiao, numero) VALUES (?, ?, ?)', (nome, regiao, numero))

    conn.commit()
    conn.close()

    return {'mensagem': 'Usuário cadastrado com sucesso!'}, 201



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