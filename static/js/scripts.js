document.addEventListener('DOMContentLoaded', () => {
    const deleteLinks = document.querySelectorAll('a[data-action="delete"]');

    deleteLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            const confirmDelete = confirm('¿Estás seguro de que quieres eliminar esta tarea? Esta acción no se puede deshacer.');
            if (!confirmDelete) {
                event.preventDefault(); // Previene la navegación si el usuario cancela
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');

    forms.forEach(form => {
        form.addEventListener('submit', (event) => {
            const titulo = form.querySelector('input[name="titulo"]').value;
            const fechaLimite = form.querySelector('input[name="fecha_limite"]').value;

            if (titulo.trim() === '') {
                alert('El título de la tarea no puede estar vacío.');
                event.preventDefault(); // Evita que el formulario se envíe
                return;
            }

            if (fechaLimite === '') {
                alert('Debes seleccionar una fecha límite.');
                event.preventDefault();
                return;
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const filtroPrioridad = document.getElementById('filtro-prioridad');
    const filtroEstado = document.getElementById('filtro-estado');
    const filasTareas = document.querySelectorAll('tbody tr');

    function filtrarTareas() {
        const prioridadSeleccionada = filtroPrioridad.value;
        const estadoSeleccionado = filtroEstado.value;

        filasTareas.forEach(fila => {
            const prioridadTarea = fila.cells[1].textContent.trim();
            const estadoTarea = fila.cells[2].textContent.trim();

            const coincidePrioridad = prioridadSeleccionada === '' || prioridadTarea === prioridadSeleccionada;
            const coincideEstado = estadoSeleccionado === '' || estadoTarea === estadoSeleccionado;

            if (coincidePrioridad && coincideEstado) {
                fila.style.display = ''; // Muestra la fila
            } else {
                fila.style.display = 'none'; // Oculta la fila
            }
        });
    }

    if (filtroPrioridad) filtroPrioridad.addEventListener('change', filtrarTareas);
    if (filtroEstado) filtroEstado.addEventListener('change', filtrarTareas);
});

