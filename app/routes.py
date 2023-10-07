from init import app
from config import cursor, connection
from flask import render_template, request, redirect, url_for

# Ruta principal para mostrar tareas


@app.route('/')
def TaskBD():
    cursor.execute('SELECT * FROM Tareas')
    tasks = cursor.fetchall()
    return render_template('TaskBD.html', tasks=tasks)

# Ruta para agregar una nueva tarea


@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task_name']
    cursor.execute(
        'INSERT INTO Tareas (Descripcion, Estado) VALUES (?, ?)', (task_name, False))
    connection.commit()
    return redirect(url_for('TaskBD'))

# Ruta para marcar una tarea como hecha o no hecha


@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    cursor.execute('SELECT Estado FROM Tareas WHERE Id = ?', (task_id,))
    task = cursor.fetchone()
    if task:
        new_done = not task[0]
        cursor.execute(
            'UPDATE Tareas SET Estado = ? WHERE Id = ?', (new_done, task_id))
        connection.commit()
    return redirect(url_for('TaskBD'))

# Ruta para eliminar una tarea


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    cursor.execute('DELETE FROM Tareas WHERE id = ?', (task_id,))
    connection.commit()
    return redirect(url_for('TaskBD'))
