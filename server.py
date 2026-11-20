from flask import Flask, render_template

app= Flask(__name__)

@app.route("/")
def index():
    return(render_template("prueba columna"))

@app.route('/formulario', methods =['GET', 'POST']) 
def registro():
    return render_template('formulario.html')

if "__main__" =="__name__":
    app.run(host="0.0.0.0", port=8088, debug=True)
