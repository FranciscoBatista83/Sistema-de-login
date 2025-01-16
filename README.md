# Sistema de Login e Cadastro de Produtos

Este projeto consiste em um sistema web simples de login e cadastro de produtos, desenvolvido com Flask no backend e HTML/CSS/JavaScript no frontend. O sistema permite que usuários façam login e acessem um formulário para cadastrar produtos, cujos dados são armazenados em uma planilha Excel.

## Funcionalidades
- **Login Simples**: Validação de usuário e senha.
- **Cadastro de Produtos**: Formulário para registro de produtos com campos como código, nome, peso, valor, quantidade, data de fabricação, fabricante e fornecedor.
- **Armazenamento em Excel**: Os dados cadastrados são salvos diretamente em um arquivo Excel (`produtos.xlsx`).

## Tecnologias Utilizadas
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: Planilha Excel (OpenPyXL)

## Requisitos
- Python 3.8 ou superior
- Flask
- OpenPyXL

## Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute a aplicação:
   ```bash
   python app.py
   ```

6. Acesse a aplicação no navegador em:
   ```
   http://localhost:5000
   ```

## Como Funciona
- Ao acessar a página principal (`/`), o usuário é apresentado a um formulário de login.
- Usuário padrão: `admin`  
  Senha padrão: `1234`
- Após o login bem-sucedido, o usuário é redirecionado para a página de cadastro de produtos (`/formulario_cadastro`).
- O envio do formulário salva os dados em `produtos.xlsx`.

## Estrutura do Projeto
```
/
├── templates/
│   ├── index.html  # Página de Login
│   └── formulario_cadastro.html  # Formulário de Cadastro
├── app.py  # Arquivo principal Flask
├── produtos.xlsx  # Planilha de armazenamento (criada automaticamente)
└── README.md  # Documentação
```

## Contribuição
Contribuições são bem-vindas! Fique à vontade para abrir um Pull Request ou relatar problemas.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
Desenvolvido por Francisco Carlos Batista.

