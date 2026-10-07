from flask import Blueprint, Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
import flask
import database


auth_bp = Blueprint("auth", __name__)
app = Flask(__name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        flash("Implemente o cadastro com hash de senha.")
        return redirect(url_for("registro"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Implemente o login com session.")
        return redirect(url_for("login"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))











#https://github.com/Lucena098/prova.iarley.git

















# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#
# - a rota /registro;
# - a rota /login;
# - a rota /logout.
