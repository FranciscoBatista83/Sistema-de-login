document
  .getElementById('formularioLogin')
  .addEventListener('submit', function (event) {
    event.preventDefault();
    const username = document.getElementById('usuario').value;
    const password = document.getElementById('senha').value;
    const errorMessage = document.getElementById('mensagemErro');

    if (username === 'admin' && password === '1234') {
      window.location.href = './html/formulario_cadastro.html';
      errorMessage.textContent = '';
    } else {
      errorMessage.textContent = 'Usuário ou senha incorretos.';
    }
  });
