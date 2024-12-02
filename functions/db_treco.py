from flask import g


def get_all_trecos(mysql):
    sql = '''
        SELECT t_id, t_foto, t_nome, t_descricao, t_localizacao
        FROM treco
        WHERE t_usuario = %s AND t_status = 'on'
        ORDER BY t_data DESC
    '''
    cur = mysql.connection.cursor()
    cur.execute(sql, (g.usuario['id'],))
    rows = cur.fetchall()
    cur.close()
    return rows


def create_treco(mysql, form):
    sql = '''
        INSERT INTO treco (
            t_usuario, t_foto, t_nome, t_descricao, t_localizacao
        ) VALUES (
            %s, %s, %s, %s, %s
        )
    '''
    cur = mysql.connection.cursor()
    cur.execute(sql, (
        g.usuario['id'],
        form['foto'],
        form['nome'],
        form['descricao'],
        form['localizacao'],
    ))
    mysql.connection.commit()
    cur.close()
    return True


def get_one_treco(mysql, id):
    sql = "SELECT * FROM treco WHERE t_id = %s AND t_usuario = %s AND t_status = 'on'"
    cur = mysql.connection.cursor()
    cur.execute(sql, (id, g.usuario['id'],))
    row = cur.fetchone()
    cur.close()
    return row


def update_treco(mysql, form, id):
    sql = '''
        UPDATE treco 
        SET t_foto = %s,
            t_nome = %s,
            t_descricao = %s,
            t_localizacao = %s
        WHERE t_id = %s
    '''
    cur = mysql.connection.cursor()
    cur.execute(sql, (
        form['foto'],
        form['nome'],
        form['descricao'],
        form['localizacao'],
        id,
    ))
    mysql.connection.commit()
    cur.close()

    return True


def delete_treco(mysql, id):
    sql = "UPDATE treco SET t_status = 'del' WHERE t_id = %s"
    cur = mysql.connection.cursor()
    cur.execute(sql, (id,))
    mysql.connection.commit()
    cur.close()
    return True


def get_count_user_trecos(mysql):
    sql = "SELECT count(t_id) AS total FROM treco WHERE t_usuario = %s AND t_status = 'on'"
    cur = mysql.connection.cursor()
    cur.execute(sql, (g.usuario['id'],))
    row = cur.fetchone()
    cur.close()
    return row


def delete_item(mysql):
    sql = "UPDATE treco SET t_status = 'del' WHERE t_usuario = %s"
    cur = mysql.connection.cursor()
    cur.execute(sql, (g.usuario['id'],))
    mysql.connection.commit()
    cur.close()
    return True
