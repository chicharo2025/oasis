
document.getElementById('searchInput').addEventListener('input', function() {
    const searchTerm = this.value.trim();
    const feedbackElement = document.getElementById('searchFeedback');
    
    if (searchTerm.length === 0) {
        this.classList.remove('is-invalid');
        feedbackElement.textContent = '';
        // Aquí podrías resetear los resultados de búsqueda si lo deseas
    } else if (searchTerm.length < 3) {
        this.classList.add('is-invalid');
        feedbackElement.textContent = 'Ingresa al menos 3 caracteres para buscar';
    } else {
        this.classList.remove('is-invalid');
        feedbackElement.textContent = '';
        // Aquí llamarías a tu función de búsqueda
        buscarProductos(searchTerm);
    }
});

function buscarProductos(searchTerm) {
    // Aquí implementarías la lógica para buscar productos
    // Puede ser una llamada AJAX a tu backend
    console.log(`Buscando productos con término: ${searchTerm}`);
    // Ejemplo con fetch:
    fetch(`/api/productos?q=${encodeURIComponent(searchTerm)}`)
        .then(response => response.json())
        .then(data => {
            if (data.length === 0) {
                // Mostrar mensaje de "no se encontraron resultados"
                console.log("No se encontraron productos");
            } else {
                // Mostrar los resultados
                console.log("Productos encontrados:", data);
            }
        })
        .catch(error => {
            console.error("Error en la búsqueda:", error);
        });
}
