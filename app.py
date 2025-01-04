from flask import Flask, render_template, request
import openpyxl
import os

app = Flask(__name__)

# Caminho para o arquivo Excel
EXCEL_FILE = 'produtos.xlsx'

# Cria o arquivo Excel se não existir
def create_excel_file():
    if not os.path.exists(EXCEL_FILE):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.append(['Código', 'Nome', 'Peso', 'Valor', 'Quantidade', 'Data', 'Fabricante', 'Fornecedor'])
        wb.save(EXCEL_FILE)

# Rota para exibir o formulário de login
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir o formulário de cadastro
@app.route('/formulario_cadastro')
def formulario_cadastro():
    return render_template('formulario_cadastro.html')

# Rota para processar o envio do formulário de cadastro
@app.route('/submit', methods=['POST'])
def submit():
    # Coletando os dados do formulário
    codigo = request.form['produtoCodigo']
    nome = request.form['produtoNome']
    peso = request.form['produtoPeso']
    valor = request.form['produtoValor']
    quantidade = request.form['produtoQuantidade']
    data = request.form['produtoData']
    fabricante = request.form['produtoFabricante']
    fornecedor = request.form['produtoFornecedor']

    # Abrindo a planilha Excel
    wb = openpyxl.load_workbook(EXCEL_FILE)
    sheet = wb.active

    # Adicionando os dados na planilha
    sheet.append([codigo, nome, peso, valor, quantidade, data, fabricante, fornecedor])

    # Salvando a planilha
    wb.save(EXCEL_FILE)

    return 'Produto cadastrado com sucesso!'

if __name__ == '__main__':
    create_excel_file()
    app.run(debug=True)
