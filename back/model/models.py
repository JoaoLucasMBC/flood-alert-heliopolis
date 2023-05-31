from model.sql_alchemy_flask import db



class UsuarioModel(db.Model):

    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    regiao = db.Column(db.String)
    numero = db.Column(db.String)

    
    def __init__(self, nome, regiao, numero):
        self.nome = nome
        self.regiao = regiao
        self.numero = numero
    

    def __repr__(self):
        return f'UsuarioModel(nome={self.nome}, regiao={self.regiao}, numero={self.numero})'
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'regiao': self.regiao,
            'numero': self.numero
        }
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    @classmethod
    def list_all(cls):
        return cls.query.all()


    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id)