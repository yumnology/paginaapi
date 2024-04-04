# https://github.com/yumnology/paginaapi 
# https://paginaapi.onrender.com
from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
API = "https://examen-parcial-3oe5.onrender.com/videojuegos"


@app.route('/')
def index():
    response = requests.get(API)
    videojuegos = response.json()
    return render_template('index.html', videojuegos=videojuegos)


@app.route('/videojuego/nuevo', methods=['GET', 'POST'])
def nuevo_videojuego():
    if request.method == 'POST':
        nuevo_videojuego = {
            "titulo": request.form['titulo'],
            "desarrollador": request.form['desarrollador'],
            "anio_lanzamiento": request.form['anio_lanzamiento'],
            "plataforma": request.form['plataforma'],
            "clasificacion": request.form['clasificacion'],
        }
        #url, json
        requests.post(API, json=nuevo_videojuego)
        #para que no crashee y redireccione donde mismo
        return redirect(url_for('index'))

    return render_template('index.html')



@app.route('/videojuego/eliminar/<int:id>', methods=['POST'])
def eliminar_videojuego(id):
    requests.delete(f"{API}/{id}")
    #Esto para que no se crashee 
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
