from flask import Flask, render_template, url_for
import requests

app= Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    API_KEYS='763a0d3c' #api key qque consigue los datos de omdb.com
    titulo='Avengers'
    URL= 'https://www.omdbapi.com/?apikey='+API_KEYS+'&t='+titulo
    datosPeliculas=requests.get(URL) # se ingresa los datos de respuestas
    datosPeliculas=datosPeliculas.json()#se convierte a JSOSN
    tituloPelicula=datosPeliculas['Title']
    directorPelicula=datosPeliculas['Director']
    datosFiltrados={'titulo':tituloPelicula,'director':directorPelicula}
    return render_template('contacto.html',datosPeliculas=datosFiltrados)


if __name__ == '__main__':
    app.run(debug=True)
