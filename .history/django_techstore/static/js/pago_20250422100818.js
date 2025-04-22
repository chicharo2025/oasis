document.addEventListener('DOMContentLoaded', function() {
    // Variables
    const checkoutBtn = document.getElementById('checkout-btn');
    const paymentModal = document.getElementById('payment-modal');
    const closeModal = document.querySelector('.close-modal');
    const paymentMethods = document.querySelectorAll('.payment-method');
    const confirmPaymentBtn = document.getElementById('confirm-payment');
    
    // Abrir modal al hacer clic en "Proceder al Pago"
    checkoutBtn.addEventListener('click', function() {
      paymentModal.style.display = 'block';
    });
    
    // Cerrar modal
    closeModal.addEventListener('click', function() {
      paymentModal.style.display = 'none';
    });
    
    // Cerrar modal al hacer clic fuera del contenido
    window.addEventListener('click', function(event) {
      if (event.target === paymentModal) {
        paymentModal.style.display = 'none';
      }
    });
    
    // Seleccionar método de pago
    paymentMethods.forEach(method => {
      method.addEventListener('click', function() {
        paymentMethods.forEach(m => m.classList.remove('active'));
        this.classList.add('active');
      });
    });
    
    // Confirmar pago
    confirmPaymentBtn.addEventListener('click', function() {
      // Aquí iría la lógica real de procesamiento de pago
      alert('Pago procesado exitosamente! Gracias por su compra.');
      paymentModal.style.display = 'none';
      
      // Redirigir a página de confirmación (simulado)
      setTimeout(() => {
        window.location.href = 'confirmacion.html';
      }, 1000);
    });
    
    // Actualizar total cuando cambia la cantidad
    const quantityInput = document.querySelector('.quantity-input');
    quantityInput.addEventListener('change', function() {
      const unitPrice = 10000;
      const quantity = parseInt(this.value);
      const subtotal = unitPrice * quantity;
      
      document.querySelector('.cart-subtotal').textContent = `$${subtotal.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`;
      document.getElementById('total-amount').textContent = `$${subtotal.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`;
    });
    
    // Eliminar producto
    const removeBtn = document.querySelector('.remove-btn');
    removeBtn.addEventListener('click', function() {
      if (confirm('¿Estás seguro de eliminar este producto de tu carrito?')) {
        this.closest('.cart-row').remove();
        document.getElementById('total-amount').textContent = '$0.00';
        alert('Producto eliminado del carrito');
      }
    });
    
    // Limpiar carrito
    document.getElementById('clear-cart').addEventListener('click', function() {
      if (confirm('¿Estás seguro de vaciar tu carrito?')) {
        document.querySelector('.cart-row').remove();
        document.getElementById('total-amount').textContent = '$0.00';
      }
    });
  });