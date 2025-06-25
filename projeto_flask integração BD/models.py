from tokenize import String
from databse import db

class usuario(db.model):
    __tablename__='usuario'
    id = db.column(db.integer, primary_key=True)
    nome = db.column(db.String(100))
    email = db.column(db.String(100))
    senha = db.column(db.String(100))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __repr__(self):
        return "usuario:{}".format(self.nome)
    