from model.sql_alchemy_flask import db



class UsuarioModel(db.Model):
    '''
    Modelo de usuário
    '''

    __tablename__ = 'usuarios'

    # colunas da tabela
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    regiao = db.Column(db.String)
    numero = db.Column(db.String)

    
    def __init__(self, nome, regiao, numero):
        # atributos do modelo
        self.nome = nome
        self.regiao = regiao
        self.numero = numero
    

    def __repr__(self):
        '''
        Função para representar o modelo como string
        '''
        return f'UsuarioModel(nome={self.nome}, regiao={self.regiao}, numero={self.numero})'
    
    
    def to_dict(self):
        '''
        Função para representar o modelo como dicionário
        '''
        return {
            'id': self.id,
            'nome': self.nome,
            'regiao': self.regiao,
            'numero': self.numero
        }
    

    def save(self):
        '''
        Função que salva uma instância na base de dados
        '''
        db.session.add(self)
        db.session.commit()
    

    def delete(self):
        '''
        Função que deleta uma instância da base de dados
        '''
        db.session.delete(self)
        db.session.commit()
    

    @classmethod
    def list_all(cls):
        '''
        Função que lista todas as instâncias da base de dados

        Returns:
            list: lista de instâncias
        '''
        return cls.query.all()


    @classmethod
    def find_by_id(cls, id):
        '''
        Função que busca uma instância pelo id

        Args:
            id (int): id da instância
        
        Returns:
            list: lista de instâncias
        '''
        return cls.query.filter_by(id=id)