from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException,status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db

app = FastAPI(title = "API Agenda")

SessionDep = Annotated[Session, Depends(get_db)]

def buscar_ou_404(session: Session, contato_id: int) -> models.Contato:
    contato = session.get(models.Contato, contato_id)
    if contato is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
              detail = "contato nao encontrado")
    return contato

@app.get("/contatos", response_model  = list[schemas.ContatoOut])
def listar_contatos(session:SessionDep):
     return session.query(models.Contato).all()

@app.get("/grupos/{grupo_id}", response_model=schemas.GrupoComContatos)
def buscar_grupo(grupo_id: int, session:SessionDep):
    grupo = session.get(models.Grupos, grupo_id)
    if grupo is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                 detail = "Grupo nao encontrado")

    return grupo
   

@app.get("/contatos/{contato_id}", response_model=schemas.ContatoOut)
def buscar_contato(contato_id: int, session:SessionDep):
    return buscar_ou_404(session,contato_id)

@app.post("/contatos", response_model = schemas.ContatoOut, 
         status_code = status.HTTP_201_CREATED)
def criar_contato(dados: schemas.CreateContato, session: SessionDep):
    contato = models.Contato(**dados.model_dump())
    session.add(contato)
    try:
        session.commit()
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail = "Email ja cadastrado")
    session.refresh(contato)
    return contato

@app.patch("/contatos/{contato_id}", response_model = schemas.ContatoOut)
def atualizar_contato(contato_id: int, dados: schemas.UpdateContato, session:SessionDep):
    contato = buscar_ou_404(session,contato_id)
    for campo,valor in dados.model_dump(exclude_unset=True).items():
        setattr(contato, campo,valor)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, 
                            detail="email ja cadastrado")
    session.refresh(contato)
    return contato

@app.delete("/contato/{contato_id}", status_code=status.HTTP_204_NO_CONTENT)
def apagar_contato(contato_id:int,session:SessionDep):
    contato = buscar_ou_404(session,contato_id)
    session.delete(contato)
    session.commit()
    