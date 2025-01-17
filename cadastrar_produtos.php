<?php
// Conexão com o banco de dados
$servername = "localhost";
$username = "Francisco";  // ou o seu usuário do banco de dados
$password = "Fcb180583.";      // ou a sua senha do banco de dados
$dbname = "cadastro_produtos"; // substitua pelo nome do seu banco de dados

// Criando conexão
$conn = new mysqli($servername, $username, $password, $dbname);

// Verificando a conexão
if ($conn->connect_error) {
    die("Falha na conexão: " . $conn->connect_error);
}

// Receber dados do formulário
$nomeProduto = $_POST['nomeProduto'];
$valor = $_POST['valor'];
$quantidade = $_POST['quantidade'];
$fornecedor = $_POST['fornecedor'];
$produtoData = $_POST['produtoData'];
$codigo = $_POST['codigo'];

// Query para inserir os dados na tabela Produtos
$sql = "INSERT INTO Produtos (nome, valor, quantidade, fornecedor, data, codigo)
        VALUES ('$nomeProduto', '$valor', '$quantidade', '$fornecedor', '$produtoData', '$codigo')";

if ($conn->query($sql) === TRUE) {
    echo "Novo produto cadastrado com sucesso!";
} else {
    echo "Erro ao cadastrar produto: " . $conn->error;
}

$conn->close();
?>
