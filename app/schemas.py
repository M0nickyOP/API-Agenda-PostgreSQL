from pydantic import BaseModel, ConfigDict

class CreateContato(BaseModel):
    nome: str
    telefone: str
    email: str

class UpdateContato(BaseModel):
    nome: str | None = None
    telefone: str | None = None
    email: str | None = None

class ContatoOut(BaseModel):
    id: int
    nome: str
    telefone: str
    email: str
    model_config = ConfigDict(from_attributes = True)

class GrupoComContatos(BaseModel):
    contatos: list[ContatoOut] = []
