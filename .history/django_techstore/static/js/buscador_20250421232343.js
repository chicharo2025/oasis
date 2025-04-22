document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const feedbackElement = document.getElementById('searchFeedback');
    
    if (searchInput) {  // Verifica que el elemento exista
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.trim();
            
            if (searchTerm.length === 0) {
                this.classList.remove('is-invalid');
                feedbackElement.textContent = '';
            } else if (searchTerm.length < 3) {
                this.classList.add('is-invalid');
                feedbackElement.textContent = 'Ingresa al menos 3 caracteres para buscar';
            } else {
                this.classList.remove('is-invalid');
                feedbackElement.textContent = '';
                buscarProductos(searchTerm);
            }
        });
    }
});

function buscarProductos(searchTerm) {
    // Implementación de la búsqueda (puede ser fetch a tu API)
    console.log(`Buscando: ${searchTerm}`);
    // Ejemplo con fetch:
    fetch(`/api/productos?q=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => mostrarResultados(data))
        .catch(error => console.error('Error:', error));
}

function mostrarResultados(data) {
    // Lógica para mostrar resultados en tu HTML
    console.log('Resultados:', data);
}