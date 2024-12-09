from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from django.http import JsonResponse
# from .utils import enviar_alerta_whatsapp
# Vista para la página de inicio
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import enviar_mensajes

class EnviarMensajesAPIView(APIView):
    """
    Vista para ejecutar la lógica de envío de mensajes
    y retornar la cantidad de mensajes enviados exitosamente.
    """

    def get(self, request, *args, **kwargs):
        try:
            # Llamar a la función
            cantidad_mensajes = enviar_mensajes()

            # Devolver la cantidad de mensajes enviados
            return Response(
                {"mensajes_enviados": cantidad_mensajes},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': 'Introduce un nombre de usuario único.',
        }
        error_messages = {
            'username': {
                'unique': 'Este nombre de usuario ya está en uso.',
            },
        }
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cuenta creada con éxito. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/register.html', {'form': form})


@login_required
def inicio(request):
    return render(request, 'inicio.html')

# Vista para listar
class GenericListView(LoginRequiredMixin, ListView):
    template_name = 'list.html'
    paginate_by = 10

    def get_queryset(self):
        """
        Obtiene el queryset del modelo dinámicamente usando la configuración del modelo.
        Se ordena por el campo ID para evitar advertencias de paginación.
        """
        model = self.model
        return model.objects.order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.model
        context['model_name'] = model._meta.model_name
        context['verbose_name'] = model._meta.verbose_name
        context['verbose_name_plural'] = model._meta.verbose_name_plural
        context['fields'] = [field.name for field in model._meta.fields]
        return context

# Vista genérica para crear
class GenericCreateView(LoginRequiredMixin, CreateView):
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
class GenericUpdateView(LoginRequiredMixin, UpdateView):
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
class GenericDeleteView(LoginRequiredMixin, DeleteView):
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
    
