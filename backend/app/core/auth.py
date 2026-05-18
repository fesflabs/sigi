from fastapi import Depends, Header, HTTPException, status
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    role: str

async def get_current_user(role: str = Header("Trabalhador FESF")) -> User:
    """
    Mock dependency para simular um usuário logado.
    Em um cenário real, isso extrairia o JWT do header de Authorization.
    Usamos um header customizado 'role' apenas para facilitar testes.
    """
    valid_roles = ["Gestor de Logistica", "Motorista", "Trabalhador FESF"]
    if role not in valid_roles:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Role inválida",
        )
    
    # Mock user id depending on role
    user_id = 1
    if role == "Gestor de Logistica":
        user_id = 2
    elif role == "Motorista":
        user_id = 3
        
    return User(id=user_id, name=f"Usuário Teste - {role}", role=role)
