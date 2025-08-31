tareas_db = []

def crear_tarea(titulo, prioridad, estado, fecha_limite):
    """Crea una nueva tarea y la añade a la base de datos."""
    nueva_tarea = {
        "id": len(tareas_db) + 1,
        "titulo": titulo,
        "prioridad": prioridad,
        "estado": estado,
        "fecha_limite": fecha_limite
    }
    tareas_db.append(nueva_tarea)
    return nueva_tarea

def listar_tareas():
    """Retorna todas las tareas de la base de datos."""
    return tareas_db

def actualizar_tarea(id_tarea, nuevos_datos):
    """Actualiza una tarea existente por su ID."""
    for tarea in tareas_db:
        if tarea['id'] == id_tarea:
            tarea.update(nuevos_datos)
            return True
    return False

def eliminar_tarea(id_tarea):
    """Elimina una tarea por su ID."""
    global tareas_db
    tarea_inicial_count = len(tareas_db)
    tareas_db = [tarea for tarea in tareas_db if tarea['id'] != id_tarea]
    return len(tareas_db) < tarea_inicial_count

# --- Ejemplo de uso y pruebas ---
if __name__ == "__main__":
    print("--- Probando la funcionalidad de la aplicación ---")
    crear_tarea("Comprar pan", "Alta", "Pendiente", "2025-09-01")
    crear_tarea("Estudiar para el examen", "Media", "En progreso", "2025-09-05")
    
    print("\nLista de tareas inicial:")
    print(listar_tareas())
    
    # Actualizar una tarea
    actualizar_tarea(1, {"estado": "Completada"})
    print("\nLista de tareas después de actualizar la tarea 1:")
    print(listar_tareas())
    
    # Eliminar una tarea
    eliminar_tarea(2)
    print("\nLista de tareas después de eliminar la tarea 2:")
    print(listar_tareas())