import _sqlite3

class Banco:
    def __init__(self, nome_banco):
        self.conexao = _sqlite3.connect(nome_banco, check_same_thread=False)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT NOT NULL
            )
        ''')
        self.conexao.commit()

    def adicionar_cliente(self, nome, email, telefone):
        self.cursor.execute('''
            INSERT INTO clientes (nome, email, telefone) 
            VALUES (?, ?, ?)
        ''', (nome, email, telefone))
        self.conexao.commit()

    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM clientes')
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conexao.close()
    def excluir_cliente(self, cliente_id):
        self.cursor.execute('DELETE FROM clientes WHERE id = ?', (cliente_id,))
        self.conexao.commit()
banco = Banco('clientes.db')
banco.criar_tabela()