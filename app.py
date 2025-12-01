from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página de Inicio
@app.route('/')
def Inicio():
    return render_template('Inicio.html')

# Ruta para la página de Flask
@app.route('/flask')
def Flask_page():
    return render_template('Flask.html')

# Ruta para la página de Git
@app.route('/git')
def Git():
    return render_template('Git.html')

# Ruta para la página de Arduino
@app.route('/arduino')
def Arduino():
    return render_template('Arduino.html')

# Ruta para el contenido principal del taller
@app.route('/taller')
def Taller():
    return render_template('taller.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
