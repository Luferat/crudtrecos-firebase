from flask import flash, g, redirect, url_for
from functions.db_treco import delete_treco


def mod_apaga(mysql, id):
    if g.usuario == '':
        return redirect(url_for('login'))
    delete_treco(mysql=mysql, id=id)
    flash('<h4>Oba!</h4><p>Seu treco foi apagado com sucesso!</p>', 'success')
    return redirect(url_for('index'))
