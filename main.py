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
miControladorCandidato= ControladorCandidato()

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