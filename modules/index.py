from flask import g, redirect, render_template, request, url_for
from functions.db_treco import get_all_trecos


def mod_index(mysql):
    if g.usuario == '':
        return redirect(url_for('login'))
    acao = request.args.get('a')
    rows = get_all_trecos(mysql)
    pagina = {
        'titulo': 'CRUDTrecos',
        'usuario': g.usuario,
        'items': rows,
        'acao': acao,
    }
    return render_template('index.html', **pagina)
