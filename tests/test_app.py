import unittest
from app import crear_tarea, listar_tareas, actualizar_tarea, eliminar_tarea

class TestFuncionalidad(unittest.TestCase):
    def setUp(self):
        # Limpia la base de datos antes de cada prueba.
        global tareas_db
        tareas_db = []

    def test_crear_tarea(self):
        tarea = crear_tarea("Limpiar la casa", "Baja", "Pendiente", "2025-09-02")
        self.assertIn(tarea, listar_tareas())
        self.assertEqual(len(listar_tareas()), 1)

    def test_listar_tareas(self):
        crear_tarea("Hacer ejercicio", "Media", "Pendiente", "2025-09-03")
        crear_tarea("Llamar al doctor", "Alta", "Pendiente", "2025-09-04")
        self.assertEqual(len(listar_tareas()), 2)
    
    def test_actualizar_tarea(self):
        crear_tarea("Pagar facturas", "Alta", "Pendiente", "2025-09-05")
        actualizacion = {"estado": "Completada", "prioridad": "Baja"}
        self.assertTrue(actualizar_tarea(1, actualizacion))
        tarea_actualizada = listar_tareas()[0]
        self.assertEqual(tarea_actualizada['estado'], "Completada")
        self.assertEqual(tarea_actualizada['prioridad'], "Baja")
    
    def test_eliminar_tarea(self):
        crear_tarea("Revisar el auto", "Media", "Pendiente", "2025-09-06")
        self.assertTrue(eliminar_tarea(1))
        self.assertEqual(len(listar_tareas()), 0)

if __name__ == '__main__':
    unittest.main()