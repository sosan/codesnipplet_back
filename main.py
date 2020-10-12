from flask import Flask, Response
import os
import settings
settings.readconfig()

from flask import Flask
# from flask_cors import CORS
# from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
# from flask import session
from flask.json import jsonify
# import json
from flask.helpers import make_response

from notion.client import NotionClient
from notion.block import CodeBlock
from notion.block import PageBlock

from ModuloLogica.Logica import ManagerLogica
managerlogica = ManagerLogica()

app = Flask(__name__)

# env_produccion = os.getenv("FLASK_ENV", "production")
# app.config("ENV", env_produccion)
# app.config("FLASK_APP", "main.py")

@app.route("/", methods=["get"])
def home():
    return jsonify({"resultado": "ok"})


@app.route("/api", methods=["get"])
def api_get():
    return redirect(url_for("home"))


@app.route("/api", methods=["post"])
def api_post():
    try:
        if request.data == None or request.data == "":
            return redirect(url_for("home"))

        data = managerlogica.convertirJsonObjecto(request.data)

        if data == None:
            return redirect(url_for("home"))

        uuid = managerlogica.getUUIdPage(data["idPage"])
        if uuid == None:
            return jsonify({"resultado": "error"})

        client = NotionClient(data["apiToken"])
        page = client.get_block(uuid)

        print("titulo antiguo" + page.title)

        # page.title += " (Cambiado)"
        bloquecodigo = page.children.add_new(CodeBlock, title=data["codigo"])
        response = None
        print(bloquecodigo)

        

        if bloquecodigo.id != None:
            response = make_response( jsonify({"resultado": "ok"}))
        else:
            response = make_response( jsonify({"resultado": "error"}))
            # response = jsonify({"resultado": "error"})

        response.headers["content-type"] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response

        # return jsonify({"resultado": "ok"})
        # return redirect(url_for("home"))

    except IndexError as error:
        return jsonify({"resultado": error.message })
    

if __name__ == "__main__":
    
    env_host = os.environ.get("HOST", "0.0.0.0")
    env_port = int(os.environ.get("PORT", 5000))
    env_debug = os.environ.get("FLASK_DEBUG", False)
    

    app.run(host=env_host, port=env_port, debug=env_debug, load_dotenv=True)
