from flask import Flask, render_template, request
from sql.banco import SQL

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/escolha')
def escolha():
    # Rodando comando SQL
    sql = SQL()
    cmd = 'SELECT * FROM tb_cliente ORDER BY nme_cliente'
    lista = sql.get_list(cmd)

    return render_template('escolha.html', lista=lista)


@app.route('/alt_form', methods=['GET'])
def alt_form():
    # Rodando comando SQL
    sql = SQL()
    cmd = 'SELECT * FROM tb_cliente WHERE idt_cliente = %s'
    obj = sql.get_object(cmd, [request.args.get('idt')])

    return render_template('alt_form.html',
                           idt_cliente=obj['idt_cliente'],
                           nme_cliente=obj['nme_cliente'],
                           dta_nasc_cliente=obj['dta_nasc_cliente']
                           )


@app.route('/alteracao', methods=['POST'])
def alteracao():
    # Pegando os dados do formulário
    idt = request.form['idt_cliente']
    nome = request.form['nme_cliente']
    data = request.form['dta_nasc_cliente']
    # Rodando comando SQL
    sql = SQL()
    cmd = 'UPDATE tb_cliente SET nme_cliente=%s, dta_nasc_cliente=%s WHERE idt_cliente=%s'
    num = sql.upd_del(cmd, [nome, data, idt])

    return render_template('alteracao.html', num=num)


@app.route('/inc_form')
def inc_form():
    return render_template('inc_form.html')


@app.route('/inclusao', methods=['POST'])
def inclusao():
    # Pegando os dados do formulário
    nome = request.form['nme_cliente']
    data = request.form['dta_nasc_cliente']
    # Rodando comando SQL
    sql = SQL()
    cmd = 'INSERT INTO tb_cliente(nme_cliente, dta_nasc_cliente) VALUES (%s, %s)'
    idt = sql.insert(cmd, [nome, data])

    return render_template('inclusao.html', idt=idt)

@app.route('/exclusao', methods=['GET'])
def exclusao():
   # Rodando comando SQL
   sql = SQL()
   cmd = 'DELETE FROM tb_cliente WHERE idt_cliente = %s'
   num = sql.upd_del(cmd, [request.args.get('idt')])


   return render_template('exclusao.html', num=num)

@app.route('/consulta')
def consulta():
    # Rodando comando SQL
    sql = SQL()
    cmd = 'SELECT * FROM tb_cliente ORDER BY nme_cliente'
    lista = sql.get_list(cmd)

    return render_template('consulta.html', lista=lista)


if __name__ == '__main__':
    app.run(debug=1)
