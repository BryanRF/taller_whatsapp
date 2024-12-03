from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente, Mantenimiento, Vehiculo, Alerta, HistorialMensaje
from .forms import ClienteForm, MantenimientoForm, VehiculoForm, AlertaForm, HistorialMensajeForm
# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista genérica para listar
class GenericListView(ListView):
    template_name = 'list.html'
    paginate_by = 10  # Número de elementos por página

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
        context['verbose_name_plural'] = self.model._meta.verbose_name_plural
        return context
    
# # Cliente Views
# class ClienteListView(ListView):
#     model = Cliente
#     template_name = 'cliente_list.html'
#     context_object_name = 'clientes'

# class ClienteCreateView(CreateView):
#     model = Cliente
#     form_class = ClienteForm
#     template_name = 'cliente_form.html'
#     success_url = reverse_lazy('cliente_list')

#     def form_valid(self, form):
#         messages.success(self.request, "Cliente registrado con éxito.")
#         return super().form_valid(form)

# # Vehículo Views
# class VehiculoListView(ListView):
#     model = Vehiculo
#     template_name = 'vehiculo_list.html'
#     context_object_name = 'vehiculos'

# class VehiculoCreateView(CreateView):
#     model = Vehiculo
#     form_class = VehiculoForm
#     template_name = 'vehiculo_form.html'
#     success_url = reverse_lazy('vehiculo_list')

#     def form_valid(self, form):
#         messages.success(self.request, "Vehículo registrado con éxito.")
#         return super().form_valid(form)

# # Mantenimiento Views
# class MantenimientoListView(ListView):
#     model = Mantenimiento
#     template_name = 'mantenimiento_list.html'
#     context_object_name = 'mantenimientos'

# class MantenimientoCreateView(CreateView):
#     model = Mantenimiento
#     form_class = MantenimientoForm
#     template_name = 'mantenimiento_form.html'
#     success_url = reverse_lazy('mantenimiento_list')

#     def form_valid(self, form):
#         messages.success(self.request, "Mantenimiento registrado con éxito.")
#         return super().form_valid(form)

# # Alerta Views
# class AlertaListView(ListView):
#     model = Alerta
#     template_name = 'alerta_list.html'
#     context_object_name = 'alertas'

# class AlertaCreateView(CreateView):
#     model = Alerta
#     form_class = AlertaForm
#     template_name = 'alerta_form.html'
#     success_url = reverse_lazy('alerta_list')

#     def form_valid(self, form):
#         messages.success(self.request, "Alerta registrada con éxito.")
#         return super().form_valid(form)

# # Historial Mensaje Views
# class HistorialMensajeListView(ListView):
#     model = HistorialMensaje
#     template_name = 'historial_mensaje_list.html'
#     context_object_name = 'historial'

# class HistorialMensajeCreateView(CreateView):
#     model = HistorialMensaje
#     form_class = HistorialMensajeForm
#     template_name = 'historial_mensaje_form.html'
#     success_url = reverse_lazy('historial_mensaje_list')

#     def form_valid(self, form):
#         messages.success(self.request, "Mensaje registrado con éxito.")
#         return super().form_valid(form)
