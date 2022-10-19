from flask import Flask, jsonify, request
from flask_cors import CORS
from json import load
from waitress import serve
import pymongo
import certifi

ca = certifi.where()

client = pymongo.MongoClient("mongodb+srv://reynaldog:reynaldog@cluster0.qfgmf.mongodb.net/bd-registro-ciudados?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["bd-registro-ciudadanos"]
#print(baseDatos.list_collection_names())

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCiudadano import ControladorCiudadano
miControladorCiudadano= ControladorCiudadano()

@app.route("/ciudadano", methods=['GET'])
def getCiudadanos():
    json= miControladorCiudadano.index()
    return jsonify(json)


@app.route("/ciudadano", methods=['POST'])
def crearCiudadano():
    data= request.get_json()
    json= miControladorCiudadano.create(data)
    return jsonify({"Usuario creado":json})

@app.route("/ciudadano/<string:id>", methods=['GET'])
def getCiudadano(id):
    json= miControladorCiudadano.show(id)
    return jsonify(json)

@app.route("/ciudadano/<string:id>", methods=['PUT'])
def actualizarCiudadano(id):
    data= request.get_json()
    json= miControladorCiudadano.update(id,data)
    return jsonify(json)

@app.route("/ciudadano/<string:id>", methods=['DELETE'])
def eliminarCiudadano(id):
    json= miControladorCiudadano.delete(id)
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