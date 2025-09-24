from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '<h1>¡Hola Mundo desde Flask!</h1>'

@app.route('/yami')
def hola_mundo2():
    return '<h1>¡yami!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
    
