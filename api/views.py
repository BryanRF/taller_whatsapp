from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from django.http import JsonResponse
# from .utils import enviar_alerta_whatsapp
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
    
def enviar_alerta(request, cliente_id):
    """
    Envia un mensaje de alerta a un cliente específico.
    """
    cliente = Cliente.objects.get(id=cliente_id)
    mensaje = f"Hola {cliente.nombre}, por favor recuerda que debes regresar al taller en 1 mes para el mantenimiento de tu vehículo."

    # Enviar el mensaje de alerta
    mensaje_sid = enviar_alerta_whatsapp(cliente.telefono, mensaje)

    if mensaje_sid:
        return JsonResponse({'status': 'success', 'message': 'Alerta enviada con éxito.'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Hubo un problema al enviar la alerta.'})