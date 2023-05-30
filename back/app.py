from flask import Flask, request
import sqlite3

app = Flask(__name__)

DATABASE = 'database/db_alert.db'


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

    conn = sqlite3.connect(DATABASE, check_same_thread=False)

    nome = request.json['nome']
    regiao = request.json['regiao']
    numero = request.json['numero']

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
    app.run()


