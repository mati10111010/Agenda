import pytest
from app import app, crear_tarea_db, listar_tareas, actualizar_tarea, eliminar_tarea, tareas_db

@pytest.fixture(autouse=True)
def limpiar_tareas():
    """Se ejecuta antes de cada test para limpiar la base de datos en memoria."""
    tareas_db.clear()

def test_crear_tarea():
    tarea = crear_tarea_db("Estudiar Python", "Alta", "Pendiente", "2025-09-10")
    assert tarea["id"] == 1
    assert tarea["titulo"] == "Estudiar Python"
    assert len(tareas_db) == 1

def test_listar_tareas():
    crear_tarea_db("Tarea 1", "Alta", "Pendiente", "2025-09-01")
    crear_tarea_db("Tarea 2", "Media", "En progreso", "2025-09-02")
    tareas = listar_tareas()
    assert len(tareas) == 2
    assert tareas[0]["titulo"] == "Tarea 1"

def test_actualizar_tarea():
    crear_tarea_db("Ir al gimnasio", "Baja", "Pendiente", "2025-09-03")
    resultado = actualizar_tarea(1, {"estado": "Completada"})
    assert resultado is True
    assert tareas_db[0]["estado"] == "Completada"

def test_eliminar_tarea():
    tarea = crear_tarea_db("Leer un libro", "Media", "Pendiente", "2025-09-04")
    assert len(tareas_db) == 1
    resultado = eliminar_tarea(tarea["id"])
    assert resultado is True
    assert len(tareas_db) == 0

def test_ruta_home():
    cliente = app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200

def test_ruta_create():
    cliente = app.test_client()
    respuesta = cliente.get("/create")
    assert respuesta.status_code == 200