// Seleciona o formulário e a mensagem de sucesso
const form = document.getElementById('cadastroForm');
const mensagem = document.getElementById('mensagem');

// Adiciona o evento de envio ao formulário
form.addEventListener('submit', function (e) {
  e.preventDefault(); // Impede o comportamento padrão do formulário

  // Coleta os dados do formulário (se precisar armazená-los, veja as observações abaixo)
  const dadosProduto = {
    nome: form.nomeProduto.value,
    valor: form.valor.value,
    quantidade: form.quantidade.value,
    fornecedor: form.fornecedor.value,
    data: form.produtoData.value,
    codigo: form.codigo.value,
  };

  console.log('Produto cadastrado:', dadosProduto); // Exibe no console (pode ser adaptado para salvar em localStorage)

  // Exibe a mensagem de sucesso
  mensagem.style.display = 'block';
  mensagem.textContent = 'Produto cadastrado com sucesso!';

  // Limpa o formulário
  form.reset();

  // Esconde a mensagem após 3 segundos
  setTimeout(() => {
    mensagem.style.display = 'none';
  }, 3000);
});
