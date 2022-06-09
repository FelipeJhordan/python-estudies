import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {"id": 0, "nome": "Rafael", "habilidades": ["Python", "Flask"]},
    {"id": 0, "nome": "Felipe", "habilidades": ["Node", "React"]},
]


@app.route("/dev/<int:id>", methods=["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
            return jsonify(response)
        except IndexError:
            response = {"status": 400, "mensagem": f"Desenvolvedor não existe {id}"}
            return jsonify(response)
        except Exception:
            response = {"status": 400, "mensagem": "Erro desconhecido"}
            return jsonify(response)

    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        if desenvolvedores[id] == None:
            return jsonify({"status": "error"})
        desenvolvedores.pop(id)
        return jsonify({"status": "sucesso", "mensagem": "Registro excluído"})


@app.route("/dev", methods=["POST", "GET"])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)

        return jsonify(desenvolvedores[posicao])
    else: 
        return jsonify(desenvolvedores)


if __name__ == "__main__":
    app.run(debug=True)
