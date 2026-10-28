from sqlalchemy import Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship
from .database import Base

class Grupos(Base):
    __tablename__ = "grupos"
    id = Column(Integer, primary_key = True)
    nome = Column(String[50],unique = True, nullable = False)

    contatos = relationship("Contato", back_populates ="grupo")

class Contato(Base):
    __tablename__ = "contatos"
    id = Column(Integer, primary_key = True)
    nome = Column(String(100), nullable = False,index = True)
    telefone = Column(String(20), nullable = False)
    email = Column(String(150), nullable = False, unique=True)
    grupo_id = Column(Integer, ForeignKey(Grupos.id))

    grupo = relationship("Grupos", back_populates="contatos")