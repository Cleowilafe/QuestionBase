let visibleCount = 6; // Número inicial de posts visíveis

document.getElementById('loadMoreBtn').addEventListener('click', function() {
    // Exibe os próximos 6 posts
    let hiddenPosts = document.querySelectorAll('.post-item.d-none');
    
    // Exibe os próximos 6 posts ocultos
    for (let i = 0; i < 6; i++) {
        if (hiddenPosts[i]) {
            hiddenPosts[i].classList.remove('d-none');
        }
    }
    
    visibleCount += 6; // Atualiza o contador de posts visíveis

    // Se não houver mais posts para exibir, oculta o botão "Mostrar Mais"
    if (visibleCount >= document.querySelectorAll('.post-item').length) {
        document.getElementById('loadMoreBtn').style.display = 'none';
    }
});