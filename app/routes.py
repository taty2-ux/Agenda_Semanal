from . import site 
from .apk.gerar_zip import pasta_zip
from .services.api_client import envia_prompt
from .services.data_processing import baixar_csv
from flask import render_template, request, redirect, url_for, send_file

@site.route("/")
def homepage():
        return render_template("index.html", msg=request.args.get("msg"))

@site.route("/enviar", methods=["POST"])
def envia():
    try:
        texto = request.form["mensagem"]
        resposta = envia_prompt(texto)
        baixar_csv(resposta)
        return redirect(url_for("homepage", msg = "Rotina gerada!! Disponível para download."))
    except:
        return redirect(url_for("homepage", msg = "Não foi possível gerar sua rotina!"))

@site.route("/download")
def download():
    try:
        return send_file("apk/horarios.csv", as_attachment=True)
    except:
        return redirect(url_for("homepage", msg = "Arquivo não encontrado!!"))

@site.route("/downloadApp")
def build():
    try:
        pasta_zip()
        return send_file("../AppAgenda.zip", as_attachment=True)
    except Exception as e:
        return redirect(url_for("homepage", msg = e))
    #"Arquivo não encontrado!!",