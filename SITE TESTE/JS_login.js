document.getElementById('aumentarCursor').addEventListener('click', function() {
  var cursorPersonalizado = document.getElementById('cursorPersonalizado');
  
  var tamanhoAtual = parseInt(cursorPersonalizado.style.width) || 16; /* Obtém o tamanho atual da imagem do cursor */
  var novoTamanho = tamanhoAtual * 1.5; /* Calcula o novo tamanho aumentando em 50% */
  
  cursorPersonalizado.style.width = novoTamanho + 'px'; /* Define o novo tamanho para a imagem do cursor */
  cursorPersonalizado.style.height = novoTamanho + 'px'; /* Define o novo tamanho para a imagem do cursor */
});
