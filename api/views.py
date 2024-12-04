from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente, Mantenimiento, Vehiculo, Alerta, HistorialMensaje
from .forms import ClienteForm, MantenimientoForm, VehiculoForm, AlertaForm, HistorialMensajeForm
# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista para listar
class GenericListView(ListView):
    template_name = 'list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Obtiene el queryset del modelo dinámicamente usando la configuración del modelo.
        """
        model = self.model
        return model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.model
        context['model_name'] = model._meta.model_name
        context['verbose_name'] = model._meta.verbose_name
        context['verbose_name_plural'] = model._meta.verbose_name_plural
        context['fields'] = [field.name for field in model._meta.fields]
        return context

# Vista genérica para crear
class GenericCreateView(CreateView):
    template_name = 'create.html'

    def get_success_url(self):
        return reverse_lazy(f'{self.model._meta.model_name}_list')

    def form_valid(self, form):
        messages.success(self.request, f"{self.model._meta.verbose_name} registrado con éxito.")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.model
        context['model_name'] = model._meta.model_name
        context['verbose_name'] = model._meta.verbose_name
        context['verbose_name_plural'] = model._meta.verbose_name_plural
        context['fields'] = [field.verbose_name for field in model._meta.fields]
        return context

# Vista genérica para editar
class GenericUpdateView(UpdateView):
    template_name = 'update.html'

    def get_success_url(self):
        return reverse_lazy(f'{self.model._meta.model_name}_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.model
        context['model_name'] = model._meta.model_name
        context['verbose_name'] = model._meta.verbose_name
        context['verbose_name_plural'] = model._meta.verbose_name_plural
        context['fields'] = [field.verbose_name for field in model._meta.fields]
        return context
    def form_valid(self, form):
        messages.success(self.request, f"{self.model._meta.verbose_name} actualizado con éxito.")
        return super().form_valid(form)
    
# Vista genérica para eliminar
class GenericDeleteView(DeleteView):
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy(f'{self.model._meta.model_name}_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.model
        context['model_name'] = model._meta.model_name
        context['verbose_name'] = model._meta.verbose_name
        context['verbose_name_plural'] = model._meta.verbose_name_plural
        context['fields'] = [field.verbose_name for field in model._meta.fields]
        return context
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f"{self.model._meta.verbose_name} eliminado con éxito.")
        return super().delete(request, *args, **kwargs)
