from .forms import ProductoForm

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



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria']
        
    # Para hacer el campo de categoría opcional:
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.all(),
        required=False,
        empty_label="Seleccione una categoría"
    )