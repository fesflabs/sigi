import pytest
from httpx import AsyncClient
from datetime import datetime, timedelta

@pytest.mark.asyncio
async def test_driver_registration(client: AsyncClient):
    # Cadastro de motorista com Perfil Gestor de Logística
    headers = {"role": "Gestor de Logistica"}
    payload = {
        "name": "João Motorista",
        "registrationNumber": "MOT-1234",
        "costCenter": "Transporte Matriz"
    }
    response = await client.post("/fleet/drivers", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["name"] == "João Motorista"

@pytest.mark.asyncio
async def test_vehicle_registration(client: AsyncClient):
    # Cadastro de Carro com Perfil Gestor de Logística
    headers = {"role": "Gestor de Logistica"}
    payload = {
        "brand": "Toyota",
        "modelName": "Corolla",
        "manufactureYear": 2022,
        "modelYear": 2023,
        "initialMileage": 15000,
        "driverId": None
    }
    response = await client.post("/fleet/vehicles", json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["brand"] == "Toyota"

@pytest.mark.asyncio
async def test_reservation_flow(client: AsyncClient):
    # Preparação: Datas com pelo menos 12h de antecedência para passar na validação
    start_dt = datetime.now() + timedelta(hours=14)
    end_dt = start_dt + timedelta(hours=2)

    # 1. Realizar uma reserva com perfil Trabalhador FESF
    headers_fesf = {"role": "Trabalhador FESF"}
    reservation_payload = {
        "startDatetime": start_dt.isoformat(),
        "endDatetime": end_dt.isoformat(),
        "origin": "Sede FESF",
        "destinations": [{"destination": "Posto de Saúde Central"}],
        "activity": "Reunião de alinhamento",
        "passengerCount": 2,
        "passengers": [{"passengerName": "Maria"}],
        "observation": "Levar projetor"
    }
    
    response = await client.post("/fleet/reservations", json=reservation_payload, headers=headers_fesf)
    assert response.status_code == 200
    reservation_data = response.json()
    assert reservation_data["id"] is not None
    assert reservation_data["status"] == "PENDING"
    
    # 2. Consultar Reservas como Trabalhador FESF
    resp_fesf_list = await client.get("/fleet/reservations", headers=headers_fesf)
    assert resp_fesf_list.status_code == 200
    assert len(resp_fesf_list.json()) > 0
    
    # 3. Consultar Reservas como Gestor de Logística
    headers_gestor = {"role": "Gestor de Logistica"}
    resp_gestor_list = await client.get("/fleet/reservations", headers=headers_gestor)
    assert resp_gestor_list.status_code == 200
    assert len(resp_gestor_list.json()) > 0
    
    # 4. Consultar agenda de reserva como Motorista
    headers_motorista = {"role": "Motorista"}
    # Endpoint /reservations retorna tudo para Motorista neste mock inicial (poderia filtrar)
    resp_motorista_list = await client.get("/fleet/reservations", headers=headers_motorista)
    assert resp_motorista_list.status_code == 200
    
    # 5. Dashboard Metrics do Gestor
    resp_metrics = await client.get("/fleet/reservations/metrics", headers=headers_gestor)
    assert resp_metrics.status_code == 200
    metrics = resp_metrics.json()
    assert metrics["totalReservations"] >= 1
