from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def crear_tarea():
    if request.method == 'POST':
        titulo = request.form['titulo']
        prioridad = request.form['prioridad']
        estado = request.form['estado']
        fecha_limite = request.form['fecha_limite']
        crear_tarea_func = crear_tarea_db(titulo, prioridad, estado, fecha_limite)
        return f"Tarea creada: {crear_tarea_func}"
    return render_template('crear_tarea.html')

tareas_db = []

def crear_tarea_db(titulo, prioridad, estado, fecha_limite):
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

def editar_tarea(id):
    tarea = next((t for t in tareas_db if t["id"] == id), None)
    if not tarea:
        return "Tarea no encontrada", 404

    if request.method == 'POST':
        tarea["titulo"] = request.form["titulo"]
        tarea["prioridad"] = request.form["prioridad"]
        tarea["estado"] = request.form["estado"]
        tarea["fecha_limite"] = request.form["fecha_limite"]
        return redirect(url_for('home'))

    return render_template('editar_tarea.html', tarea=tarea)

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
    tarea_inicial_count = len(tareas_db)
    tareas_db[:] = [tarea for tarea in tareas_db if tarea['id'] != id_tarea]
    return len(tareas_db) < tarea_inicial_count

# --- Ejemplo de uso y pruebas ---
if __name__ == "__main__":
    print("--- Probando la funcionalidad de la aplicación ---")
    crear_tarea_db("Comprar pan", "Alta", "Pendiente", "2025-09-01")
    crear_tarea_db("Estudiar para el examen", "Media", "En progreso", "2025-09-05")
    
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
