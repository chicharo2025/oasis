document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const feedbackElement = document.getElementById('searchFeedback');
    const resultsContainer = document.getElementById('searchResults');

    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const searchTerm = this.value.trim();
            
            if (searchTerm.length === 0) {
                this.classList.remove('is-invalid');
                feedbackElement.textContent = '';
                resultsContainer.innerHTML = '';
            } else if (searchTerm.length < 3) {
                this.classList.add('is-invalid');
                feedbackElement.textContent = 'Ingresa al menos 3 caracteres para buscar';
                resultsContainer.innerHTML = '';
            } else {
                this.classList.remove('is-invalid');
                feedbackElement.textContent = '';
                buscarProductos(searchTerm);
            }
        });
    }
});

function buscarProductos(searchTerm) {
    // Limpia resultados anteriores
    const resultsContainer = document.getElementById('searchResults');
    resultsContainer.innerHTML = '<div class="text-center">Buscando...</div>';
    
    // Simulación de datos - REEMPLAZA ESTO CON TU LLAMADA REAL A LA API
    const mockProductos = [
        {id: 1, nombre: 'Laptop HP', precio: 1200},
        {id: 2, nombre: 'Teclado mecánico', precio: 80},
        {id: 3, nombre: 'Mouse inalámbrico', precio: 35}
    ];
    
    // Filtrado simulado (esto debería hacerse en el backend)
    const resultados = mockProductos.filter(producto => 
        producto.nombre.toLowerCase().includes(searchTerm.toLowerCase())
    );
    
    mostrarResultados(resultados);
    
    // PARA PRODUCCIÓN: Descomenta esto y adapta a tu endpoint real
    /*
    fetch(`/api/productos?q=${encodeURIComponent(searchTerm)}`)
        .then(response => {
            if (!response.ok) throw new Error('Error en la búsqueda');
            return response.json();
        })
        .then(data => mostrarResultados(data))
        .catch(error => {
            console.error('Error:', error);
            resultsContainer.innerHTML = `<div class="alert alert-danger">${error.message}</div>`;
        });
    */
}

function mostrarResultados(productos) {
    const resultsContainer = document.getElementById('searchResults');
    
    if (productos.length === 0) {
        resultsContainer.innerHTML = '<div class="alert alert-info">No se encontraron productos</div>';
        return;
    }
    
    let html = '<div class="list-group">';
    productos.forEach(producto => {
        html += `
        <a href="#" class="list-group-item list-group-item-action">
            <h5>${producto.nombre}</h5>
            <p class="mb-1">$${producto.precio.toFixed(2)}</p>
        </a>
        `;
    });
    html += '</div>';
    
    resultsContainer.innerHTML = html;
}