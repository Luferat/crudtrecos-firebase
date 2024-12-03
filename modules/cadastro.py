from flask import flash, g, redirect, render_template, request, url_for


def mod_cadastro(mysql):
    jatem = ''
    if g.usuario != '':
        return redirect(url_for('perfil'))
    if request.method == 'POST':
        form = dict(request.form)
        sql = "SELECT u_id, u_status FROM usuario WHERE u_email = %s AND u_status != 'del'"
        cur = mysql.connection.cursor()
        cur.execute(sql, (form['email'],))
        rows = cur.fetchall()
        cur.close()
        if len(rows) > 0:
            if rows[0]['u_status'] == 'off':
                flash(
                    'Este e-mail já está cadastrado para um usuário inativo. Entre em contato para saber mais.', 'error')
            else:
                flash(
                    'Este e-mail já está cadastrado. Tente fazer login ou solicitar uma nova senha.', 'error')
        else:
            sql = "INSERT INTO usuario (u_nome, u_nascimento, u_email, u_senha) VALUES (%s, %s, %s, SHA1(%s))"
            cur = mysql.connection.cursor()
            cur.execute(
                sql, (
                    form['nome'],
                    form['nascimento'],
                    form['email'],
                    form['senha'],
                )
            )
            mysql.connection.commit()
            cur.close()
            flash(
                '<h4>Oba!</h4><p>Usuário cadastrado com sucesso! Faça login...</p>', 'success')
    pagina = {
        'titulo': 'CRUDTrecos - Cadastre-se',
    }
    return render_template('cadastro.html', **pagina)
