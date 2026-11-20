from flask import Flask, request, jsonify, send_file
import sqlite3

app = Flask(__name__)

def conectar_banco():
    conn = sqlite3.connect('estoque.db')
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = conectar_banco()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            estoque_minimo INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    conn = conectar_banco()
    produtos = conn.execute('SELECT * FROM produtos ORDER BY id DESC').fetchall()
    conn.close()
    return jsonify([dict(p) for p in produtos])

@app.route('/api/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.json
    if not dados.get('nome') or float(dados.get('preco') or 0) <= 0:
        return jsonify({'erro': 'Nome e preço maior que zero são obrigatórios'}), 400

    conn = conectar_banco()
    conn.execute(
        'INSERT INTO produtos (nome, preco, quantidade, estoque_minimo) VALUES (?, ?, ?, ?)',
        (
            dados['nome'],
            float(dados['preco']),
            int(dados.get('quantidade') or 0),
            int(dados.get('estoque_minimo') or 0)
        )
    )
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Produto cadastrado!'}), 201

@app.route('/api/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    conn = conectar_banco()
    conn.execute('DELETE FROM produtos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Produto removido!'})

if __name__ == '__main__':
    app.run(debug=True)
