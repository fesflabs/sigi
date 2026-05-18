import pytest
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.core.celery import celery_app
from app.core.db import get_session

# Fixture do Celery
@pytest.fixture(autouse=True)
def celery_config():
    """Força as tasks do Celery a rodarem de forma síncrona nos testes."""
    celery_app.conf.update(
        task_always_eager=True,
        task_eager_propagates=True,
    )
    yield
    # Limpeza (opcional)
    celery_app.conf.update(
        task_always_eager=False,
        task_eager_propagates=False,
    )

# Fixture do Banco de Dados
@pytest.fixture
async def async_session() -> AsyncGenerator[AsyncSession, None]:
    """Cria uma engine in-memory e provê uma sessão limpa para cada teste."""
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        poolclass=StaticPool,
        connect_args={"check_same_thread": False}
    )
    
    from sqlmodel import SQLModel
    from app.modules.fleet.models import Driver, Vehicle, Reservation, ReservationDestination, ReservationPassenger
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async_session_maker = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    
    async with async_session_maker() as session:
        yield session

# Fixture do Client HTTP
@pytest.fixture
async def client(async_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """Client HTTP injetando a sessão do banco in-memory na aplicação."""
    async def override_get_session():
        yield async_session

    app.dependency_overrides[get_session] = override_get_session
    
    # Com httpx >= 0.24.0 o ASGITransport é recomendado
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as c:
        yield c
        
    app.dependency_overrides.clear()
