from flask import Flask, render_template, request, redirect, url_for
import random
import time

app = Flask(__name__)

# Datos de los participantes y preguntas
participantes = []
preguntas_banco = {
    'peliculas': [
        {'pregunta': '¿Quién dirigió la película "Inception"?',
         'opciones': ['Christopher Nolan', 'Steven Spielberg', 'Quentin Tarantino', 'James Cameron'],
         'respuesta': 'Christopher Nolan'},
        # Agrega más preguntas de películas según sea necesario
    ],
    'libros': [
        {'pregunta': '¿Quién escribió "Cien años de soledad"?',
         'opciones': ['Gabriel García Márquez', 'Julio Cortázar', 'Mario Vargas Llosa', 'Isabel Allende'],
         'respuesta': 'Gabriel García Márquez'},
        # Agrega más preguntas de libros según sea necesario
    ],
    'ciudades_capitales': [
        {'pregunta': '¿Cuál es la capital de Francia?',
         'opciones': ['Berlín', 'Madrid', 'París', 'Londres'],
         'respuesta': 'París'},
        # Agrega más preguntas de ciudades capitales según sea necesario
    ],
    'paises': [
        {'pregunta': '¿En qué continente se encuentra Australia?',
         'opciones': ['Asia', 'Oceanía', 'Europa', 'América'],
         'respuesta': 'Oceanía'},
        # Agrega más preguntas de países según sea necesario
    ],
}

# Función para generar una trivia aleatoria
def generar_trivia(categoria):
    trivia = random.sample(preguntas_banco[categoria], k=1)
    return trivia

# Ruta de inicio
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        edad = request.form['edad']
        documento = request.form['documento']
        participante = {'nombre': nombre, 'fecha': fecha, 'edad': edad, 'documento': documento}
        participantes.append(participante)
        return redirect(url_for('elegir_categoria'))
    return render_template('inicio.html')

# Ruta para elegir la categoría
@app.route('/elegir_categoria')
def elegir_categoria():
    return render_template('elegir_categoria.html')

# Ruta para jugar la trivia
@app.route('/jugar_trivia/<categoria>')
def jugar_trivia(categoria):
    trivia = generar_trivia(categoria)
    return render_template('jugar_trivia.html', categoria=categoria, trivia=trivia, time=time)

# Ruta para mostrar el resultado
@app.route('/resultado', methods=['POST'])
def resultado():
    tiempo_inicio = float(request.form['tiempo_inicio'])
    tiempo_final = time.time()
    tiempo_total = round(tiempo_final - tiempo_inicio, 2)
    return render_template('resultado.html', participantes=participantes, tiempo_total=tiempo_total)

if __name__ == '__main__':
    app.run(debug=True)
