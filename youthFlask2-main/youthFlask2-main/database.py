from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

tursourl= 'libsql://larissa-larissamendescode.aws-us-east-1.turso.io?authToken=eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3NDYzMDM0MTgsImlkIjoiNmVkZDY1NDktODI4My00OWE3LWFmOTYtMWVlODUxNGRhNjg2IiwicmlkIjoiMThkNGFmMWEtYTZkYS00MWJjLWEyMzQtZjdjNjg4NjY5YWZmIn0.cHfe1Bz8PKpnX5YO0EoU4bZIGqna3ZwVzaS-o3wW-5P_mfVHQQNNF5LioMbjnjfaqjSCYid7sykebl3Hy2vOBg' 

engine = create_engine(tursourl, echo=True, connect_args={'check_same_thread': False})


Base = declarative_base()

class User(Base): 
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    contatos = relationship('Contato', back_populates='user')


class Contato(Base):
    __tablename__ = 'contatos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefone = Column(String(15), nullable=False)
    tags = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='contatos')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()




