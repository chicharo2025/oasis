from .forms import ProductoForm
from django import forms


from django.shortcuts import render,redirect
def agregar_producto(request):
   if request.method == 'POST':
       form = ProductoForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('listen_productos')
   else:
       form = ProductoForm()
   return render(request, 'agregar_producto.html', {'form': form})


class ProductSearchForm(forms.Form):
    query = forms.CharField(
        label='Buscar producto',
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese nombre del producto...',
            'class': 'form-control'
        })
    )