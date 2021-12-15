from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def  Index():
    return render_template('index.html')

@app.route('/tabacos')
def  Tabacos():
    return render_template('tabacos.html')

@app.route('/papelillos')
def  Papelillos():
    return render_template('papelillos.html')

@app.route('/filtros')
def  Filtros():
    return render_template('filtros.html')

@app.route('/parafernalia')
def  Parafernalia():
    return render_template('parafernalia.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)