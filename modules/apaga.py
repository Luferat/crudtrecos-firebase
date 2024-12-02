from flask import g, redirect, url_for
from functions.db_treco import delete_treco


def mod_apaga(mysql, id):
    if g.usuario == '':
        return redirect(url_for('login'))
    delete_treco(mysql=mysql, id=id)
    return redirect(url_for('index', a='apagado'))
