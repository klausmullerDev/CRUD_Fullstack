from flask import Flask, render_template, request
from sql.banco import SQL

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/escolha')
def escolha():
    sql = SQL()
    cmd = 'SELECT * FROM tb_produto ORDER BY nme_produto'
    lista = sql.get_list(cmd)
    return render_template('escolha.html', lista=lista)

@app.route('/alt_form', methods=['GET'])
def alt_form():
    sql = SQL()
    cmd = 'SELECT * FROM tb_produto WHERE idt_produto = %s'
    obj = sql.get_object(cmd, [request.args.get('idt')])
    return render_template('alt_form.html',
                           idt_produto=obj['idt_produto'],
                           nme_produto=obj['nme_produto'],
                           qtd_estoque_produto=obj['qtd_estoque_produto'],
                           vlr_produto=obj['vlr_produto']
                           )

@app.route('/alteracao', methods=['POST'])
def alteracao():
    idt = request.form['idt_produto']
    nome = request.form['nme_produto']
    qtd_estoque = request.form['qtd_estoque_produto']
    valor = request.form['vlr_produto']
    sql = SQL()
    cmd = 'UPDATE tb_produto SET nme_produto=%s, qtd_estoque_produto=%s, vlr_produto=%s WHERE idt_produto=%s'
    num = sql.upd_del(cmd, [nome, qtd_estoque, valor, idt])
    return render_template('alteracao.html', num=num)

@app.route('/inc_form')
def inc_form():
    return render_template('inc_form.html')

@app.route('/inclusao', methods=['POST'])
def inclusao():
    nome = request.form['nme_produto']
    qtd_estoque = request.form['qtd_estoque_produto']
    valor = request.form['vlr_produto']
    sql = SQL()
    cmd = 'INSERT INTO tb_produto(nme_produto, qtd_estoque_produto, vlr_produto) VALUES (%s, %s, %s)'
    idt = sql.insert(cmd, [nome, qtd_estoque, valor])
    return render_template('inclusao.html', idt=idt)

@app.route('/exclusao', methods=['GET'])
def exclusao():
    sql = SQL()
    cmd = 'DELETE FROM tb_produto WHERE idt_produto = %s'
    num = sql.upd_del(cmd, [request.args.get('idt')])
    return render_template('exclusao.html', num=num)

@app.route('/consulta')
def consulta():
    sql = SQL()
    cmd = 'SELECT * FROM tb_produto ORDER BY nme_produto'
    lista = sql.get_list(cmd)
    return render_template('consulta.html', lista=lista)

if __name__ == '__main__':
    app.run(debug=True)
