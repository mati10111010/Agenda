from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', tareas=tareas_db)

@app.route('/create', methods=['GET', 'POST'])
def crear_tarea():
    if request.method == 'POST':
        titulo = request.form['titulo']
        prioridad = request.form['prioridad']
        estado = request.form['estado']
        fecha_limite = request.form['fecha_limite']
        crear_tarea_db(titulo, prioridad, estado, fecha_limite)
        return redirect(url_for('home'))
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

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
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

@app.route('/delete/<int:id>')
def eliminar_tarea(id):
    global tareas_db
    tareas_db[:] = [tarea for tarea in tareas_db if tarea["id"] != id]
    return redirect(url_for('home'))

# --- Ejemplo de uso y pruebas ---
if __name__ == "__main__":
    app.run(debug=True)
