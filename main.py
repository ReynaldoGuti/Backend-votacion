from flask import Flask, jsonify, request
from flask_cors import CORS
from json import load
from waitress import serve
import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://reynaldog:reynaldog@cluster0.q11cs3o.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["db-registro-ciudadanos"]
print(baseDatos.list_collection_names())

app = Flask(__name__)
cors = CORS(app)

from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorResultados import ControladorResultados

miControladorResultados= ControladorResultados()
miControladorMesa = ControladorMesa()
miControladorCandidato= ControladorCandidato()

##RutasCandidato
@app.route("/candidato", methods=['GET'])
def ListarCandidatos():
    json= miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data= request.get_json()
    json= miControladorCandidato.create(data)
    return jsonify({"Nuevo candidato creado":json})

@app.route("/candidato/<string:id>", methods=['GET'])
def ListarCandidato(id):
    json= miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidato/<string:id>", methods=['PUT'])
def actualizarCandidato(id):
    data= request.get_json()
    json= miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json= miControladorCandidato.delete(id)
    return jsonify(json)

## Rutas Mesas

@app.route("/mesa", methods=['GET'])
def ListarMesas():
    json= miControladorMesa.index()
    return jsonify(json)
@app.route("/mesa", methods=['POST'])
def crearMesa():
    data= request.get_json()
    json= miControladorMesa.create(data)
    return jsonify({"Nueva mesa creada":json})

@app.route("/mesa/<string:id>", methods=['GET'])
def ListarMesa(id):
    json= miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesa/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    data= request.get_json()
    json= miControladorMesa.update(id,data)
    return jsonify({"Mesa Actualizada":json})
@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    json= miControladorMesa.delete(id)
    return jsonify(json)
@app.route("/mesa/<string:id>/resultados/<string:id_resultados>",methods=['PUT'])
def asignarResultadoaMesa(id,id_resultados):
    json= miControladorMesa.asignarResultado(id,id_resultados)
    return jsonify(json)

## Rutas Resultados
@app.route("/resultados", methods=['GET'])
def ListarResultados():
    json= miControladorResultados.index()
    return jsonify(json)
@app.route("/resultados", methods=['POST'])
def crearResultados():
    data= request.get_json()
    json= miControladorResultados.create(data)
    return jsonify({"Nuevos Resultados Creados":json})
@app.route("/resultados/<string:id>", methods=['GET'])
def ListarResultado(id):
    json= miControladorResultados.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id>", methods=['PUT'])
def actualizarResultado(id):
    data= request.get_json()
    json= miControladorResultados.update(id,data)
    return jsonify({"Resultados Actualizados":json})
@app.route("/resultados/<string:id>", methods=['DELETE'])
def eliminarResultado(id):
    json= miControladorResultados.delete(id)
    return jsonify({"Resultados Eliminados":json})
@app.route("/",methods=['GET'])
def test():
    json = {}
    json["Message"] = "Server running ..."
    return jsonify(json)
def loadFileConfig():
    with open('config.json') as f:
        data = load(f)
    return data

if __name__=='__main__':
    dataConfig= loadFileConfig()
    print("Server running : "+ "http://"+ dataConfig["url-backend"]+":"+ str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])